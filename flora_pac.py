#!/usr/bin/env python
#
# Flora_Pac by @leaskh
# www.leaskh.com, i@leaskh.com
#
# based on chnroutes project (by Numb.Majority@gmail.com)
#

import re
import urllib2
import argparse
import math


def generate_pac(proxy):
    results  = fetch_ip_data()
    pacfile  = 'flora_pac.pac'
    rfile    = open(pacfile, 'w')
    strLines = (
        "// Flora_Pac by @leaskh"
        "\n// www.leaskh.com, i@leaskh.com"
        "\n"
        "\nfunction FindProxyForURL(url, host)"
        "\n{"
        "\n"
        "\n    var list = ["
        "\n        ['192.168.0.0', '255.255.255.0'],"
        "\n        ['192.168.1.0', '255.255.255.0'],"
    )
    intLines = 0
    for ip,mask,_ in results:
        if intLines > 0:
            strLines = strLines + ','
        intLines = intLines + 1
        strLines = strLines + "\n        ['%s', '%s']"%(ip, mask)    
    strLines = strLines + (
        "\n    ];"
        "\n"
		"\n    var urls = ["
		"\n        '*.168xs.com/*',"
		"\n        '*.shoudian.org/*',"
		"\n        '*.xiuzhenba.com/*',"
		"\n        '*.shuax.com/*',"
		"\n        '*.mzxzx.com/*',"
		"\n        '*.oko.co/*',"
		"\n        '*hioo*',"
		"\n        '*.gg.ma/*',"
		"\n        '*.qs99w.com/*',"
		"\n        '*.unkzone.net/*',"
		"\n        '*bipics.net/*',"
		"\n        '*pen.io*',"
		"\n        '*cl.orc.st*',"
		"\n        '*.5917.me/*',"
		"\n        '*.dmxf.com/*',"
		"\n        '*.www.galbus.us/*',"
		"\n        '*.animex9.com/*',"
		"\n        '*.h5gal.net/*',"
		"\n        '*.2tu.me/*',"
		"\n        '*.tumblr.com/*',"
		"\n        '*35xs*',"
		"\n        '*.hkpic.net/*',"
		"\n        '*.myforum.com.hk/*',"
		"\n        '*.sankakucomplex.com/*',"
		"\n        '*.sankakustatic.com/*',"
		"\n        '*chrislin2k.com/*',"
		"\n        '*setianshi.org/*',"
		"\n        '*bipics.net/*',"
		"\n        '*hkbisi.com/*',"
		"\n        '*hkbc.net/*',"
		"\n        '*pornhub*',"
		"\n        '*bisi-forum.com/*',"
		"\n    ];"
        "\n    var PROXY ='%s';"
        "\n    var DIRECT ='DIRECT';"
        "\n"
        "\n   for (i=0;i<urls.length;i++) {"
        "\n   if (shExpMatch(url,urls[i])) { return DIRECT;}"
        "\n   }"
        "\n"
        "\n   var ip = dnsResolve(host);"
        "\n   for (i=0;i<list.length;i++) {"
        "\n       if (isInNet(ip, list[i][0], list[i][1])) {"
        "\n           if (! isInNet('202.106.199.39', list[i][0], list[i][1])) return direct;} "
        "\n   }"
        "\n"
        "\n   return PROXY;"
        "\n"
        "\n}"
        "\n"%(proxy)
    )
    rfile.write(strLines)
    rfile.close()
    print ("Rules: %d items.\n"
           "Usage: Use the newly created %s as your web browser's automatic "
           "proxy configuration (.pac) file."%(intLines, pacfile))


def fetch_ip_data():
    #fetch data from apnic
    print "Fetching data from apnic.net, it might take a few minutes, please wait..."
    url=r'http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest'
    data=urllib2.urlopen(url).read()

    cnregex=re.compile(r'apnic\|cn\|ipv4\|[0-9\.]+\|[0-9]+\|[0-9]+\|a.*',re.IGNORECASE)
    cndata=cnregex.findall(data)

    results=[]

    for item in cndata:
        unit_items=item.split('|')
        starting_ip=unit_items[3]
        num_ip=int(unit_items[4])

        imask=0xffffffff^(num_ip-1)
        #convert to string
        imask=hex(imask)[2:]
        mask=[0]*4
        mask[0]=imask[0:2]
        mask[1]=imask[2:4]
        mask[2]=imask[4:6]
        mask[3]=imask[6:8]

        #convert str to int
        mask=[ int(i,16 ) for i in mask]
        mask="%d.%d.%d.%d"%tuple(mask)

        #mask in *nix format
        mask2=32-int(math.log(num_ip,2))

        results.append((starting_ip,mask,mask2))

    return results


if __name__=='__main__':
    parser=argparse.ArgumentParser(description="Generate proxy auto-config rules.")
    parser.add_argument('-x', '--proxy',
                        dest = 'proxy',
                        default = 'PROXY 127.0.0.1:1998',
                        nargs = '?',
                        help = "Proxy Server, examples: "
                               "SOCKS 127.0.0.1:8964; "
                               "SOCKS5 127.0.0.1:8964; "
                               "PROXY 127.0.0.1:8964")

    args = parser.parse_args()

    generate_pac(args.proxy)
