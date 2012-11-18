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
import os, re, socket, struct, threading, traceback, sys, select, urlparse, signal, urllib, urllib2, time, hashlib, binascii, zlib, httplib, errno, string, logging, random, heapq
import DNS

import socks
import config

gConfig = config.gConfig

dnsHeap = []

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

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer): pass
class ProxyHandler(BaseHTTPRequestHandler):
    remote = None
    dnsCache = {}
    dnsCacheLock = 0
    now = 0
    depth = 0

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
            return self.getRemoteResolve(host)

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
                    return self.getRemoteResolve(host)
                return ip
        except:
            logging.error ("DNS system resolve Error: " + host)
            ip = ""
        return self.getRemoteResolve(host)

    def getRemoteResolve(self, host):
        dnsserver = dnsHeap[0][1] #heap top

        logging.info ("remote resolve " + host + " by " + dnsserver)
        reqProtocol = "udp"
        if "DNS_PROTOCOL" in gConfig:
            if gConfig["DNS_PROTOCOL"] in ["udp", "tcp"]:
                reqProtocol = gConfig["DNS_PROTOCOL"]
        try:
            response = DNS.Request().req(name=host, qtype="A", protocol=reqProtocol, port=gConfig["DNS_PORT"], server=dnsserver)
        except:
            d = heapq.heappop(dnsHeap)
            heapq.heappush(dnsHeap, (d[0]+1, d[1]))
            logging.error(host + " resolve fail by " + dnsserver)
            return host

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
        doProxy = False
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
            #TODO: pac
            for key in gConfig:
                if type(gConfig[key]) in [str,int] :
                    html = html.replace("{"+key+"}", str(gConfig[key]))
                else :
                    html = html.replace("{" + key + "}", str(gConfig[key]))
            self.wfile.write(status + "\r\n\r\n" + html)
            return
        try:
            
            if (gConfig["ADSHOSTON"] and host in gConfig["ADSHOST"]):
                status = "HTTP/1.1 404 Not Found"
                self.wfile.write(status + "\r\n\r\n")
                return

            # Remove http://[host] , for google.com.hk
            path = self.path[self.path.find(netloc) + len(netloc):]

            connectHost = self.getip(host)
            logging.info ("Resolved " + host + " => " + connectHost)

            if isDomainBlocked(host) or isIpBlocked(connectHost):
                self.remote = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
                logging.info("connect to " + host + ":" + str(port) + " var socks5 proxy")
                self.remote.connect((connectHost, port))
                doProxy = True
            else:
                self.remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                logging.debug( "connect to " + host + ":" + str(port))
                self.remote.connect((connectHost, port))

            # Send requestline
            if path == "":
                path = "/"
            print (" ".join((self.command, path, self.request_version)) + "\r\n")
            self.remote.send(" ".join((self.command, path, self.request_version)) + "\r\n")
                
            self.remote.send(str(self.headers) + "\r\n")
            # Send Post data
            if(self.command=='POST'):
                self.remote.send(self.rfile.read(int(self.headers['Content-Length'])))
            response = HTTPResponse(self.remote, method=self.command)
            response.begin()
            print (host + " response: %d"%(response.status))

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

            exc_type, exc_value, exc_traceback = sys.exc_info()

            if exc_type == socket.error:
                code = exc_value[0]
                if code == errno.EPIPE: #errno.EPIPE, 10053 is for Windows
                    logging.info ("Detected remote disconnect: " + host)
                    return
                if code == errno.ECONNREFUSED:
                    logging.info ("Detected ECONNREFUSED: " + host)
                    return
                if code in errno.ECONNRESET: #reset
                    logging.info(host + ": reset from " + connectHost)

            if not doProxy:
                gConfig["BLOCKED_IPS"][connectHost] = True
                return self.proxy()

            print ("error in proxy: ", self.requestline)
            print (exc_type)
            print (str(exc_value) + " " + host)
    
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
        try:
            if not (isDomainBlocked(host) or isIpBlocked(ip)):
                self.remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                logging.info ("SSL: connect " + host + " ip:" + ip)
                self.remote.connect((ip, int(port)))

                Agent = 'WCProxy/1.0'
                self.wfile.write('HTTP/1.1'+' 200 Connection established\n'+
                         'Proxy-agent: %s\n\n'%Agent)
                self._read_write()
                return
        except:
            logging.info ("SSL: connect " + ip + " failed.")
            gConfig["BLOCKED_IPS"][ip] = True

        self.remote = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
        print ("SSL: connect " + host + " ip:" + ip + " var socks5 proxy")
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
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, gConfig["SOCKS_HOST"], gConfig["SOCKS_PORT"])

    for d in gConfig["REMOTE_DNS_LIST"]:
        heapq.heappush(dnsHeap, (1,d))
 

    print ("Set your browser's HTTP/HTTPS proxy to 127.0.0.1:%d"%(gOptions.port))
    print ("You can configure your proxy var http://127.0.0.1:%d"%(gOptions.port))
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
            parser.add_argument('--pidfile', default='socks-proxy.pid', help='pid file')
            parser.add_argument('--logfile', default='socks-proxy.log', help='log file')
            gOptions = parser.parse_args()
        else:
            import optparse
            parser = optparse.OptionParser()
            parser.add_option("-p", "--port", action="store", type="int", dest="port", default=gConfig["LOCAL_PORT"], help="local port")
            parser.add_option("-l", "--log", action="store", type="int", dest="log", default=2, help="log level, 0-5")
            parser.add_option("-f", "--pidfile", dest="pidfile", default="socks-proxy.pid", help="pid file")
            parser.add_option("-o", "--logfile", dest="logfile", default="socks-proxy.log", help="log file")
            (gOptions, args)=parser.parse_args()

    except :
        #arg parse error
        print ("arguments parse error")
        class option:
            def __init__(self): 
                self.log = 2
                self.port = gConfig["LOCAL_PORT"]
                self.pidfile = ""
        gOptions = option()

    if gOptions.pidfile != "":
        pid = str(os.getpid())
        f = open(gOptions.pidfile,'w')
        print ("Writing pid " + pid + " to "+gOptions.pidfile)
        f.write(pid)
        f.close()

    logging.basicConfig(filename=gOptions.logfile, level = gOptions.log*10, format='%(asctime)-15s %(message)s')
    
    start()