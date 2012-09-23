#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    westchamberproxy by liruqi@gmail.com
    Based on:
    PyGProxy by gdxxhg@gmail.com 
    GoAgent by {phus.lu,hewigovens}@gmail.com (Phus Lu and Hewig Xu)
'''

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
from httplib import HTTPResponse, BadStatusLine
import os, re, socket, struct, threading, traceback, sys, select, urlparse, signal, urllib, urllib2, time, hashlib, binascii, zlib, httplib, errno, string, logging, random, ssl
import DNS

try:
    import OpenSSL
except ImportError:
    OpenSSL = None

import socks
import config

gConfig = config.gConfig


gConfig["BLACKHOLES"] = [
    '243.185.187.30', 
    '243.185.187.39', 
    '46.82.174.68', 
    '78.16.49.15', 
    '93.46.8.89', 
    '37.61.54.158', 
    '159.24.3.173', 
    '203.98.7.65', 
    '8.7.198.45', 
    '159.106.121.75', 
    '59.24.3.173'
]

gOriginalCreateConnection = socket.create_connection

class SimpleMessageClass(object):
    def __init__(self, fp, seekable = 0):
        self.dict = dict = {}
        self.headers = headers = []
        readline = getattr(fp, 'readline', None)
        headers_append = headers.append
        if readline:
            while 1:
                line = readline(8192)
                if not line or line == '\r\n':
                    break
                key, _, value = line.partition(':')
                if value:
                    headers_append(line)
                    dict[key.title()] = value.strip()
        else:
            for key, value in fp:
                key = key.title()
                dict[key] = value
                headers_append('%s: %s\r\n' % (key, value))

    def getheader(self, name, default=None):
        return self.dict.get(name.title(), default)

    def getheaders(self, name, default=None):
        return [self.getheader(name, default)]

    def addheader(self, key, value):
        self[key] = value

    def get(self, name, default=None):
        return self.dict.get(name.title(), default)

    def iteritems(self):
        return self.dict.iteritems()

    def iterkeys(self):
        return self.dict.iterkeys()

    def itervalues(self):
        return self.dict.itervalues()

    def keys(self):
        return self.dict.keys()

    def values(self):
        return self.dict.values()

    def items(self):
        return self.dict.items()

    def __getitem__(self, name):
        return self.dict[name.title()]

    def __setitem__(self, name, value):
        name = name.title()
        self.dict[name] = value
        headers = self.headers
        try:
            i = (i for i, line in enumerate(headers) if line.partition(':')[0].title() == name).next()
            headers[i] = '%s: %s\r\n' % (name, value)
        except StopIteration:
            headers.append('%s: %s\r\n' % (name, value))

    def __delitem__(self, name):
        name = name.title()
        del self.dict[name]
        headers = self.headers
        for i in reversed([i for i, line in enumerate(headers) if line.partition(':')[0].title() == name]):
            del headers[i]

    def __contains__(self, name):
        return name.title() in self.dict

    def __len__(self):
        return len(self.dict)

    def __iter__(self):
        return iter(self.dict)

    def __str__(self):
        return ''.join(self.headers)

gOptions = {}

gipWhiteList = []
domainWhiteList = [
    ".cn",
    "renren.com",
    "baidu.com",
    "mozilla.org",
    "mozilla.net",
    "mozilla.com",
    "wp.com",
    "qstatic.com",
    "serve.com",
    "qq.com",
    "qqmail.com",
    "soso.com",
    "weibo.com",
    "youku.com",
    "tudou.com",
    "ft.net",
    "ge.net",
    "no-ip.com",
    "nbcsandiego.com",
    "unity3d.com",
    "opswat.com",
    "126.net",
    "163.com",
    ]

def isIpBlocked(ip):
    if "BLOCKED_IPS" in gConfig:
        if ip in gConfig["BLOCKED_IPS"]:
            return True
    if "BLOCKED_IPS_M16" in gConfig:
        ipm16 = ".".join(ip.split(".")[:2])
        if ipm16 in gConfig["BLOCKED_IPS_M16"]:
            return True
    if "BLOCKED_IPS_M24" in gConfig:
        ipm24 = ".".join(ip.split(".")[:3])
        if ipm24 in gConfig["BLOCKED_IPS_M24"]:
            return True
    return False

def isDomainBlocked(host):
    rootDomain = string.join(host.split('.')[-2:], '.')
    if (host in gConfig["BLOCKED_DOMAINS"]):
        return True
    if rootDomain not in ["nicovideo.jp", "facebook.com", "twitter.com"]:
        return rootDomain in gConfig["BLOCKED_DOMAINS"]
    return False

def urlfetch(url, payload, method, headers, fetchhost, fetchserver, password=None, dns=None, on_error=None):
    errors = []
    params = {'url':url, 'method':method, 'headers':headers, 'payload':payload}
    params['fetchmax'] = '3'
    logging.debug('urlfetch params %s', params)
    if password:
        params['password'] = password
    if dns:
        params['dns'] = dns
    params =  '&'.join('%s=%s' % (k, binascii.b2a_hex(v)) for k, v in params.iteritems())
    for i in xrange(3):
        try:
            logging.debug('urlfetch %r by %r', url, fetchserver)
            request = urllib2.Request(fetchserver, zlib.compress(params, 9))
            request.add_header('Content-Type', '')
            request.add_header('Host', fetchhost)
            response = urllib2.urlopen(request)
            compressed = response.read(1)

            data = {}
            if compressed == '0':
                data['code'], hlen, clen = struct.unpack('>3I', response.read(12))
                data['headers'] = SimpleMessageClass((k, binascii.a2b_hex(v)) for k, _, v in (x.partition('=') for x in response.read(hlen).split('&')))
                data['response'] = response
            elif compressed == '1':
                rawdata = zlib.decompress(response.read())
                data['code'], hlen, clen = struct.unpack('>3I', rawdata[:12])
                data['headers'] = SimpleMessageClass((k, binascii.a2b_hex(v)) for k, _, v in (x.partition('=') for x in rawdata[12:12+hlen].split('&')))
                data['content'] = rawdata[12+hlen:12+hlen+clen]
                response.close()
            else:
                raise ValueError('Data format not match(%s)' % url)

            return (0, data)
        except Exception, e:
            if on_error:
                logging.info('urlfetch error=%s on_error=%s', str(e), str(on_error))
                data = on_error(e)
                if data:
                    newfetch = (data.get('fetchhost'), data.get('fetchserver'))
                    if newfetch != (fetchhost, fetchserver):
                        (fetchhost, fetchserver) = newfetch
            errors.append(str(e))
            time.sleep(i+1)
            continue
    return (-1, errors)

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer): pass
class ProxyHandler(BaseHTTPRequestHandler):
    remote = None
    dnsCache = {}
    dnsCacheLock = 0
    now = 0
    depth = 0
    MessageClass = SimpleMessageClass

    def enableInjection(self, host, ip):
        self.depth += 1
        if self.depth > 3:
            logging.error(host + " looping, exit")
            return

        global gipWhiteList;
        
        for c in ip:
            if c!='.' and (c>'9' or c < '0'):
                logging.error ("recursive ip "+ip)
                return True

        for r in gipWhiteList:
            ran,m2 = r.split("/");
            dip = struct.unpack('!I', socket.inet_aton(ip))[0]
            dran = struct.unpack('!I', socket.inet_aton(ran))[0]
            shift = 32 - int(m2)
            if (dip>>shift) == (dran>>shift):
                logging.info (ip + " (" + host + ") is in China, matched " + r)
                return False
        return True

    def isIp(self, host):
        return re.match(r'^([0-9]+\.){3}[0-9]+$', host) != None

    def getip(self, host):
        if self.isIp(host):
            return host

        if host in gConfig["HOST"]:
            logging.info ("Rule resolve: " + host + " => " + gConfig["HOST"][host])
            return gConfig["HOST"][host]

        self.now = int( time.time() )
        if host in self.dnsCache:
            if self.now < self.dnsCache[host]["expire"]:
                logging.debug( "Cache: " + host + " => " + self.dnsCache[host]["ip"] + " / expire in %d (s)" %(self.dnsCache[host]["expire"] - self.now))
                return self.dnsCache[host]["ip"]

        if gConfig["SKIP_LOCAL_RESOLV"]:
            return self.getRemoteResolve(host, gConfig["REMOTE_DNS"])

        try:
            ip = socket.gethostbyname(host)
            ChinaUnicom404 = {
                "202.106.199.37" : 1,
                "202.106.195.30" : 1,
            }
            if ip in gConfig["BLACKHOLES"]:
                print ("Fake IP " + host + " => " + ip)
            elif ip in ChinaUnicom404:
                print ("ChinaUnicom404 " + host + " => " + ip + ", ignore")
            else:
                logging.debug ("DNS system resolve: " + host + " => " + ip)
                if isIpBlocked(ip):
                    print (host + " => " + ip + " blocked, try remote resolve")
                    return self.getRemoteResolve(host, gConfig["REMOTE_DNS"])
                return ip
        except:
            print "DNS system resolve Error: " + host
            ip = ""
        return self.getRemoteResolve(host, gConfig["REMOTE_DNS"])

    def getRemoteResolve(self, host, dnsserver):
        logging.info ("remote resolve " + host + " by " + dnsserver)
        reqProtocol = "udp"
        if "DNS_PROTOCOL" in gConfig:
            if gConfig["DNS_PROTOCOL"] in ["udp", "tcp"]:
                reqProtocol = gConfig["DNS_PROTOCOL"]

        response = DNS.Request().req(name=host, qtype="A", protocol=reqProtocol, port=gConfig["DNS_PORT"], server=dnsserver)
        #response.show()
        #print "answers: " + str(response.answers)
        ip = ""
        blockedIp = ""
        cname = ""
        ttl = 0
        for a in response.answers:
            if a['typename'] == 'CNAME':
                cname = a["data"]
            else:
                ttl = a["ttl"]
                if isIpBlocked(a["data"]): 
                    print (host + " => " + a["data"]+" is blocked. ")
                    blockedIp = a["data"]
                    continue
                ip = a["data"]
        if (ip != ""):
            if len(self.dnsCache) >= gConfig["DNS_CACHE_MAXSZ"] and self.dnsCacheLock <=0 :
                self.dnsCacheLock = 1
                logging.debug("purge DNS cache...")
                for h in self.dnsCache:
                    if self.now >= self.dnsCache[h]["expire"]:
                        del self.dnsCache[h]
                logging.debug("purge DNS cache done, now %d" % len(self.dnsCache))
                self.dnsCacheLock = 0

            if len(self.dnsCache) < gConfig["DNS_CACHE_MAXSZ"]: self.dnsCache[host] = {"ip":ip, "expire":self.now + ttl*2 + 60}
            return ip
        if (blockedIp != ""):
            return blockedIp
        if (cname != ""):
            return self.getip(cname)

        logging.info ("authority: "+ str(response.authority))
        for a in response.authority:
            if a['typename'] != "NS":
                continue
            if type(a['data']) == type((1,2)):
                return self.getRemoteResolve(host, a['data'][0])
            else :
                return self.getRemoteResolve(host, a['data'])
        print ("DNS remote resolve failed: " + host)
        return host
    
    def proxy(self):
        doInject = False
        inWhileList = False
        logging.info (self.requestline)
        port = 80
        host = self.headers["Host"]
        
        if host.find(":") != -1:
            port = int(host.split(":")[1])
            host = host.split(":")[0]
        (scm, netloc, path, params, query, _) = urlparse.urlparse(self.path)

        if host in ["127.0.0.1", "localhost"]:
            basedir = os.path.dirname(__file__)
            htmlTemplate = os.path.join(basedir, "index.html")
            htmlFile = open(htmlTemplate)
            html = htmlFile.read()
            htmlFile.close()
            status = "HTTP/1.1 200 OK"
            if path == "/save":
                postData = self.rfile.read(int(self.headers['Content-Length']))
                data = urlparse.parse_qs(postData)
                logging.info(str(data))
                key = data["id"][0]
                value = data["value"][0]
                if key in gConfig:
                    if type(gConfig[key]) == type(True):
                        if value == "true": gConfig[key] = True
                        if value == "false": gConfig[key] = False
                    else:
                        gConfig[key] = type(gConfig[key]) (value)
                    hookInit()
                self.wfile.write(status + "\r\n\r\n" + value)
                return
            if path == "/add":
                postData = self.rfile.read(int(self.headers['Content-Length']))
                data = urlparse.parse_qs(postData)
                if "BLOCKED_DOMAINS" in data:
                    domain = data["BLOCKED_DOMAINS"][0]
                    if domain[:4] == "http":
                        (scm, netloc, path, params, query, _) = urlparse.urlparse(domain)
                        domain = netloc
                    gConfig["BLOCKED_DOMAINS"][domain] = True
                    
                self.wfile.write("HTTP/1.1 302 FOUND\r\n" + "Location: /\r\n\r\n" + domain)
                return
				
            for key in gConfig:
                if type(gConfig[key]) in [str,int] :
                    html = html.replace("{"+key+"}", str(gConfig[key]))
                else :
                    html = html.replace("{" + key + "}", str(gConfig[key]))
            self.wfile.write(status + "\r\n\r\n" + html)
            return
        try:
            if (host in gConfig["HSTS_DOMAINS"]):
                redirectUrl = "https://" + self.path[7:]
                #redirect 
                status = "HTTP/1.1 302 Found"
                self.wfile.write(status + "\r\n")
                self.wfile.write("Location: " + redirectUrl + "\r\n\r\n")
                return
            
            if (gConfig["ADSHOSTON"] and host in gConfig["ADSHOST"]):
                status = "HTTP/1.1 404 Not Found"
                self.wfile.write(status + "\r\n\r\n")
                return

            # Remove http://[host] , for google.com.hk
            path = self.path[self.path.find(netloc) + len(netloc):]

            for d in domainWhiteList:
                if host.endswith(d):
                    logging.info (host + " in domainWhiteList: " + d)
                    inWhileList = True

            connectHost = self.getip(host)
            if not inWhileList:
                doInject = self.enableInjection(host, connectHost)
                logging.info ("Resolved " + host + " => " + connectHost)

            if not isDomainBlocked(host) or not isIpBlocked(connectHost):
                self.remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                logging.debug( "connect to " + host + ":" + str(port))
                self.remote.connect((connectHost, port))
                if doInject: 
                    logging.info ("inject http for "+host)
                    self.remote.send("\r\n\r\n")

            # Send requestline
            if path == "":
                path = "/"
            print " ".join((self.command, path, self.request_version)) + "\r\n"
            self.remote.send(" ".join((self.command, path, self.request_version)) + "\r\n")
                
            self.remote.send(str(self.headers) + "\r\n")
            # Send Post data
            if(self.command=='POST'):
                self.remote.send(self.rfile.read(int(self.headers['Content-Length'])))
            response = HTTPResponse(self.remote, method=self.command)
            badStatusLine = False
            msg = "http405"
            try :
                response.begin()
                print host + " response: %d"%(response.status)
                msg = "http%d"%(response.status)
            except BadStatusLine:
                print host + " response: BadStatusLine"
                msg = "badStatusLine"
                badStatusLine = True
            except:
                raise

            if doInject and (response.status == 400 or response.status == 405 or badStatusLine):
                self.remote.close()
                self.remote = None
                logging.info (host + " seem not support inject, " + msg)
                return self.proxy()

            # Reply to the browser
            status = "HTTP/1.1 " + str(response.status) + " " + response.reason
            self.wfile.write(status + "\r\n")
            h = ''
            for hh, vv in response.getheaders():
                if hh.upper()!='TRANSFER-ENCODING':
                    h += hh + ': ' + vv + '\r\n'
            self.wfile.write(h + "\r\n")

            dataLength = 0
            while True:
                response_data = response.read(8192)
                if(len(response_data) == 0): break
                if dataLength == 0 and (len(response_data) <= 501):
                    if response_data.find("<title>400 Bad Request") != -1 or response_data.find("<title>501 Method Not Implemented") != -1:
                        logging.error( host + " not supporting injection")
                        domainWhiteList.append(host)
                        response_data = gConfig["PAGE_RELOAD_HTML"]
                self.wfile.write(response_data)
                dataLength += len(response_data)
                logging.debug( "data length: %d"%dataLength)
        except:
            if self.remote:
                self.remote.close()
                self.remote = None

            (scm, netloc, path, params, query, _) = urlparse.urlparse(self.path)
            status = "HTTP/1.1 302 Found"
            if host in gConfig["HSTS_ON_EXCEPTION_DOMAINS"]:
                redirectUrl = "https://" + self.path[7:]
                self.wfile.write(status + "\r\n")
                self.wfile.write("Location: " + redirectUrl + "\r\n")

            exc_type, exc_value, exc_traceback = sys.exc_info()

            if exc_type == socket.error:
                code, msg = str(exc_value).split('] ')
                code = code[1:].split(' ')[1]
                if code in ["32", "10053"]: #errno.EPIPE, 10053 is for Windows
                    logging.info ("Detected remote disconnect: " + host)
                    return
                if code in ["54", "11004", "10051", "timed out", "10054"]:
				    return self.proxy()
                if code in ["61"]: #server not support injection
                    if doInject:
                        logging.info("try not inject " + host)
                        domainWhiteList.append(host)
                        return self.proxy()
 
            print "error in proxy: ", self.requestline
            print exc_type
            print str(exc_value) + " " + host
            if exc_type == socket.timeout or (exc_type == socket.error and code in ["60", "110", "10060", "11001"]): #timed out, 10060 is for Windows
                if not inWhileList:
                    logging.info ("add "+host+" to blocked domains")
                    gConfig["BLOCKED_DOMAINS"][host] = True
                    return self.proxy()
    
    def do_GET(self):
        #some sites(e,g, weibo.com) are using comet (persistent HTTP connection) to implement server push
        #after setting socket timeout, many persistent HTTP requests redirects to web proxy, waste of resource
        #socket.setdefaulttimeout(18)
        self.proxy()

    def do_POST(self):
        self.proxy()
    
    def do_CONNECT(self):
        host, _, port = self.path.rpartition(':')
        ip = self.getip(host)
        logging.info ("[Connect] Resolved " + host + " => " + ip)
        if not (isDomainBlocked(host) or isIpBlocked(ip)):
            self.remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            logging.info ("SSL: connect " + host + " ip:" + ip)
            self.remote.connect((ip, int(port)))

            Agent = 'WCProxy/1.0'
            self.wfile.write('HTTP/1.1'+' 200 Connection established\n'+
                    'Proxy-agent: %s\n\n'%Agent)
            self._read_write()
            return

    # reslove ssl from http://code.google.com/p/python-proxy/
    def _read_write(self):
        BUFLEN = 8192
        time_out_max = 60
        count = 0
        socs = [self.connection, self.remote]
        while 1:
            count += 1
            (recv, _, error) = select.select(socs, [], socs, 3)
            if error:
                logging.error ("select error")
                break
            if recv:
                for in_ in recv:
                    data = in_.recv(BUFLEN)
                    if in_ is self.connection:
                        out = self.remote
                    else:
                        out = self.connection
                    if data:
                        out.send(data)
                        count = 0
            if count == time_out_max:
                logging.debug( "select timeout")
                break

def start():
    cnt = {}
    for x in range(16):
        dnsserver = gConfig['REMOTE_DNS']
        try:
            logging.info("DNS: " + dnsserver + " - %d"%x)
            response = DNS.Request().req(name="www.twitter.com", qtype="A", protocol="udp", port=gConfig["DNS_PORT"], server=dnsserver, drop_blackholes=False)
            for a in response.answers:
                if a["typename"]=="CNAME":
                    continue
                ip = a["data"]
                if ip not in cnt: cnt[ip] = 0
                cnt[ip] += 1
                if (ip not in gConfig["BLACKHOLES"]):
                    if ip.split(".")[0] == "199": 
                        continue
                    print "### new fake ip: " + ip 
                    gConfig["BLACKHOLES"].append(ip)
                break
        except:
            print sys.exc_info()
    print "DNS hijack test:" + str(cnt)

    # Read Configuration
    try :
        import json
        param = "?version=" + gConfig["VERSION"]
        url = (gConfig["ONLINE_CONFIG_URI"] + param)
        logging.info("Load online config: " + url)
        s = urllib2.urlopen(url)
        jsonConfig = json.loads( s.read() )
        for k in jsonConfig:
            logging.info( "read online json config " + k + " => " + str(jsonConfig[k]))
            if (k in gConfig) and (type(gConfig[k])==dict):
                gConfig[k].update(jsonConfig[k])
            gConfig[k] = jsonConfig[k]
    except:
        logging.info("Load online json config failed")

    try:
        s = urllib2.urlopen(gConfig["BLOCKED_DOMAINS_URI"])
        for line in s.readlines():
            line = line.strip()
            gConfig["BLOCKED_DOMAINS"][line] = True
        s.close()
    except:
        logging.info("load blocked domains failed")

    httplib.HTTPMessage = SimpleMessageClass
    print "Loaded", len(gConfig["HOST"]), " dns rules."
    print "Set your browser's HTTP/HTTPS proxy to 127.0.0.1:%d"%(gOptions.port)
    print "You can configure your proxy var http://127.0.0.1:%d"%(gOptions.port)
    if gConfig['CONFIG_ON_STARTUP']:
        try: 
            import webbrowser
            webbrowser.open("http://127.0.0.1:%d"%gOptions.port)
        except:
            pass

    server = ThreadingHTTPServer(("0.0.0.0", gOptions.port), ProxyHandler)
    try: server.serve_forever()
    except KeyboardInterrupt: exit()
    
if __name__ == "__main__":
    try :
        if sys.version[:3] in ('2.7', '3.0', '3.1', '3.2', '3.3'):
            import argparse
            parser = argparse.ArgumentParser(description='west chamber proxy')
            parser.add_argument('--port', default=gConfig["LOCAL_PORT"], type=int,
                   help='local port')
            parser.add_argument('--log', default=2, type=int, help='log level, 0-5')
            parser.add_argument('--pidfile', default='wcproxy.pid', help='pid file')
            parser.add_argument('--logfile', default='wcproxy.log', help='log file')
            gOptions = parser.parse_args()
        else:
            import optparse
            parser = optparse.OptionParser()
            parser.add_option("-p", "--port", action="store", type="int", dest="port", default=gConfig["LOCAL_PORT"], help="local port")
            parser.add_option("-l", "--log", action="store", type="int", dest="log", default=2, help="log level, 0-5")
            parser.add_option("-f", "--pidfile", dest="pidfile", default="wcproxy.pid", help="pid file")
            parser.add_option("-o", "--logfile", dest="logfile", default="wcproxy.log", help="log file")
            (gOptions, args)=parser.parse_args()

    except :
        #arg parse error
        print "arg parse error"
        class option:
            def __init__(self): 
                self.log = 2
                self.port = gConfig["LOCAL_PORT"]
                self.pidfile = ""
        gOptions = option()

    if gOptions.pidfile != "":
        pid = str(os.getpid())
        f = open(gOptions.pidfile,'w')
        print "Writing pid " + pid + " to "+gOptions.pidfile
        f.write(pid)
        f.close()

    logging.basicConfig(filename=gOptions.logfile, level = gOptions.log*10, format='%(asctime)-15s %(message)s')
    
    start()
