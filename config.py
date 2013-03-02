#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
GOAGENT_FETCHHOST_LIST = ["azlyfox-test.appspot.com","careyproxy.appspot.com","crossgfw2011.appspot.com","crossgfw2012.appspot.com","crossgfw2013.appspot.com","crossgfw2014.appspot.com","crossgfw2015.appspot.com","dghabc.appspot.com","dghabc1.appspot.com","gaehostport.appspot.com","galaxy-yp-g1.appspot.com","ghostflyinggo.appspot.com","gfw22222.appspot.com","gfw33333.appspot.com","gfw44444.appspot.com","gfw55555.appspot.com","gfw66666.appspot.com","gfw77777.appspot.com","gfw88888.appspot.com","gfw99999.appspot.com","goagent00.appspot.com","goagent03.appspot.com","goagent04.appspot.com","goagent06.appspot.com","goagent08.appspot.com","goagent09.appspot.com","goagent13.appspot.com","goagent14.appspot.com","goagent18.appspot.com","goagent19.appspot.com","goagent20.appspot.com","goagent21.appspot.com","goagent24.appspot.com","goagent25.appspot.com","goagent26.appspot.com","goagent31.appspot.com","goagent33.appspot.com","goagent36.appspot.com","goagent37.appspot.com","goagent38.appspot.com","goagent39.appspot.com","goagent40.appspot.com","goagent41.appspot.com","goagent42.appspot.com","goagent43.appspot.com","goagent48.appspot.com","goagent49.appspot.com","goagent53.appspot.com","goagent57.appspot.com","goagent59.appspot.com","goagent60.appspot.com","goagent61.appspot.com","goagent62.appspot.com","goagent63.appspot.com","goagent64.appspot.com","goagent65.appspot.com","goagent66.appspot.com","goagent69.appspot.com","goagent70.appspot.com","goagent72.appspot.com","goagent73.appspot.com","goagent74.appspot.com","goagent75.appspot.com","goagent77.appspot.com","goagent78.appspot.com","goagent79.appspot.com","goagent81.appspot.com","goagent85.appspot.com","goagent89.appspot.com","goagent90.appspot.com","goagent91.appspot.com","goagent93.appspot.com","goagent94.appspot.com","goagent95.appspot.com","goagent96.appspot.com","goagent97.appspot.com","goagent98.appspot.com","goagent99.appspot.com","goagent100.appspot.com","goagent107.appspot.com","goagent2166.appspot.com","goagent2177.appspot.com","goagent2188.appspot.com","goagent2199.appspot.com","goagent-hrd.appspot.com","gongxiang1900.appspot.com","gongxiang1901.appspot.com","gongxiang1902.appspot.com","gongxiang1903.appspot.com","gongxiang1904.appspot.com","gongxiang1905.appspot.com","gongxiang1906.appspot.com","gongxiang1907.appspot.com","gongxiang1912.appspot.com","gongxiang1913.appspot.com","gongxiang1914.appspot.com","gongxiang1915.appspot.com","gongxiang1916.appspot.com","gongxiang1917.appspot.com","gongxiang1918.appspot.com","gxfclql.appspot.com","houliapp.appspot.com","ianbhullar.appspot.com","iphonegae1.appspot.com","iphonegae2.appspot.com","iphonegae3.appspot.com","jndtydl005.appspot.com","laoliannanapp1.appspot.com","laoliannanapp2.appspot.com","lawshermanproxy1.appspot.com","lawshermanproxy2.appspot.com","lingyanshanxia.appspot.com","lingyanshanxia1.appspot.com","lingyanshanxia2.appspot.com","lingyanshanxia3.appspot.com","lingyanshanxia4.appspot.com","lingyanshanxia5.appspot.com","lingyanshanxia6.appspot.com","lingyanshanxia7.appspot.com","lingyanshanxia8.appspot.com","lingyanshanxia9.appspot.com","mengqin1-hrd.appspot.com","mysblxjbs.appspot.com","my-xberry00.appspot.com","my-xberry01.appspot.com","my-xberry10.appspot.com","my-xberry12.appspot.com","onyourheart89.appspot.com","pandafacegoagent.appspot.com","phmpui.appspot.com","pvotw01.appspot.com","pvotw02.appspot.com","pvotw03.appspot.com","pvotw04.appspot.com","pvotw05.appspot.com","pvotw06.appspot.com","pvotw07.appspot.com","pvotw08.appspot.com","r00tgfwrule.appspot.com","reedandbicgae0.appspot.com","reedandbicgae1.appspot.com","reedandbicgae2.appspot.com","reedandbicgae3.appspot.com","reedandbicgae4.appspot.com","reedandbicgae5.appspot.com","reedandbicgae6.appspot.com","reedandbicgae7.appspot.com","reedandbicgae8.appspot.com","reedandbicgae9.appspot.com","shadow-goagent.appspot.com","shadow-ma.appspot.com","spawnmhsbc1.appspot.com","spawnmhsbc2.appspot.com","sssh123451.appspot.com","sssh123452.appspot.com","sssh123453.appspot.com","sssh123454.appspot.com","sssh123455.appspot.com","tricle86.appspot.com","yong10478a1.appspot.com","vilanny2008.appspot.com","wcproxy-web.appspot.com","wcproxy1.appspot.com","whuproxy1.appspot.com","whuproxy2.appspot.com","whuproxy3.appspot.com","whuproxy4.appspot.com","whuproxy5.appspot.com","wukan2012.appspot.com","xiawei233.appspot.com","zellhuang1986.appspot.com"] # 2.1.0 :"gfw000000.appspot.com","gfw111111.appspot.com","gfw222222.appspot.com","gfw333333.appspot.com","gfw444444.appspot.com","gfw555555.appspot.com","gfw666666.appspot.com","gfw777777.appspot.com","gfw888888.appspot.com","gfw999999.appspot.com",
GOAGENT_IP_LIST = ["mail.google.com","www.google.com.hk","www.google.com"]

gConfig = {
    "VERSION" : "20121022",
    "PROXY_TYPE": "goagent",# "goagent" or "socks5", can be created by `ssh -NfD 0.0.0.0:1234 user@hostname`
    "SOCKS_HOST": "localhost",
    "SOCKS_PORT": 1234,
    "GOAGENT_FETCHHOST": GOAGENT_FETCHHOST_LIST[random.randint(0, len(GOAGENT_FETCHHOST_LIST)-1)], 
    "GOAGENT_PASSWORD": "",
    "GOAGENT_IP": GOAGENT_IP_LIST[random.randint(0, len(GOAGENT_IP_LIST)-1)],
    "AUTORANGE_HOSTS": ['.youtube.com', '.atm.youku.com', '.googlevideo.com', 'av.vimeo.com', 'smile-*.nicovideo.jp', 'video.*.fbcdn.net', 's*.last.fm', 'x*.last.fm', '.xvideos.com', '.phncdn.com', '.edgecastcdn.net'],
    "AUTORANGE_THREADS": 2,
    "AUTORANGE_BUFSIZE": 8192,
    "AUTORANGE_WAITSIZE": 524288,
    "AUTORANGE_MAXSIZE": 1048576,
    "BLOCKED_DOMAINS_URI" : "https://raw.github.com/gdwgi1225/west-chamber-season-3/master/status/timedout.txt",#"https://raw.github.com/liruqi/west-chamber-season-3/master/west-chamber-proxy/status/timedout.txt"
    #"ONLINE_CONFIG_URI" : "http://gdwgi1225.sinaapp.com/config.php",#"http://wcproxy.sinaapp.com/config.php"
    "PAC_GFWLIST" : "http://autoproxy-gfwlist.googlecode.com/svn/trunk/gfwlist.txt",
    "REMOTE_DNS_LIST" : ["168.95.1.1", "168.95.192.1","168.95.192.2", "202.181.202.140", "168.95.192.33", "205.171.2.25", "205.171.2.26", "205.171.3.25", "205.171.3.26", "205.171.3.65", "164.124.101.2", "202.181.224.2", "202.181.224.18", "202.181.224.19", "165.87.201.244", "165.87.201.244"],
    "DNS_PROTOCOL": "udp",
    "DNS_PORT": 53,
    "DNS_CACHE_MAXSZ" : 1024,
    "SKIP_LOCAL_RESOLV" : True,
    "CONFIG_ON_STARTUP" : False,
    "PAC_PORT" : 1999,
    "LOCAL_PORT" : 1998,
    "HOST" : {
        "a248.e.akamai.net" : "118.155.230.56",
        "github.com" : "207.97.227.239",
        "gist.github.com" : "204.232.175.94",
        "raw.github.com" : "207.97.227.243"
    },
    "ADSHOSTON" : True,
    "ADSHOST" : {
        "stat.youku.com" : "0.0.0.0",
        "static.lstat.youku.com" : "0.0.0.0",
        "valb.atm.youku.com" : "0.0.0.0",
        "valc.atm.youku.com" : "0.0.0.0",
        "valf.atm.youku.com" : "0.0.0.0",
        "valo.atm.youku.com" : "0.0.0.0",
        "valp.atm.youku.com" : "0.0.0.0",
        "vid.atm.youku.com" : "0.0.0.0",
        "walp.atm.youku.com" : "0.0.0.0",
        "adextensioncontrol.tudou.com" : "127.0.0.1",
        "iwstat.tudou.com" : "127.0.0.1",
        "nstat.tudou.com" : "127.0.0.1",
        "stats.tudou.com" : "127.0.0.1",
        "*.p2v.tudou.com*" : "127.0.0.1",
        "at-img1.tdimg.com" : "127.0.0.1",
        "at-img2.tdimg.com" : "127.0.0.1",
        "at-img3.tdimg.com" : "127.0.0.1",
        "adplay.tudou.com" : "127.0.0.1",
        "adcontrol.tudou.com" : "127.0.0.1",
        "stat.tudou.com" : "127.0.0.1",
        "1.allyes.com.cn" : "127.0.0.1",
        "analytics.ku6.com" : "127.0.0.1",
        "gug.ku6cdn.com" : "127.0.0.1",
        "ku6.allyes.com" : "127.0.0.1",
        "ku6afp.allyes.com" : "127.0.0.1",
        "pq.stat.ku6.com" : "127.0.0.1",
        "st.vq.ku6.cn" : "127.0.0.1",
        "stat0.888.ku6.com" : "127.0.0.1",
        "stat1.888.ku6.com" : "127.0.0.1",
        "stat2.888.ku6.com" : "127.0.0.1",
        "stat3.888.ku6.com" : "127.0.0.1",
        "static.ku6.com" : "127.0.0.1",
        "v0.stat.ku6.com" : "127.0.0.1",
        "v1.stat.ku6.com" : "127.0.0.1",
        "v2.stat.ku6.com" : "127.0.0.1",
        "v3.stat.ku6.com" : "127.0.0.1",
        "afp.qiyi.com" : "127.0.0.1",
        "focusbaiduafp.allyes.com" : "127.0.0.1",
        "a.cctv.com" : "127.0.0.1",
        "a.cntv.cn" : "127.0.0.1",
        "ad.cctv.com" : "127.0.0.1",
        "d.cntv.cn" : "127.0.0.1",
        "adguanggao.eee114.com" : "127.0.0.1",
        "cctv.adsunion.com" : "127.0.0.1",
        "dcads.sina.com.cn" : "127.0.0.1",
        "pp2.pptv.com" : "127.0.0.1",
        "pro.letv.com" : "127.0.0.1",
        "images.sohu.com" : "127.0.0.1",
        "a.cctv.com" : "127.0.0.1",
        "a.cntv.cn" : "127.0.0.1",
        "ad.cctv.com" : "127.0.0.1",
        "d.cntv.cn" : "127.0.0.1",
        "adguanggao.eee114.com" : "127.0.0.1",
        "cctv.adsunion.com" : "127.0.0.1",
        "acs.56.com" : "127.0.0.1",
        "acs.agent.56.com" : "127.0.0.1",
        "acs.agent.v-56.com" : "127.0.0.1",
        "bill.agent.56.com" : "127.0.0.1",
        "bill.agent.v-56.com" : "127.0.0.1",
        "stat.56.com" : "127.0.0.1",
        "stat2.corp.56.com" : "127.0.0.1",
        "union.56.com" : "127.0.0.1",
        "uvimage.56.com" : "127.0.0.1",
        "v16.56.com" : "127.0.0.1",
        "pole.6rooms.com" : "127.0.0.1",
        "shrek.6.cn" : "127.0.0.1",
        "simba.6.cn" : "127.0.0.1",
        "union.6.cn" : "127.0.0.1",
        "86file.megajoy.com" : "127.0.0.1",
        "86get.joy.cn" : "127.0.0.1",
        "86log.joy.cn" : "127.0.0.1",
        "casting.openv.com" : "127.0.0.1",
        "m.openv.tv" : "127.0.0.1",
        "uniclick.openv.com" : "127.0.0.1",
        "mcfg.sandai.net" : "127.0.0.1",
        "biz5.sandai.net" : "127.0.0.1",
        "server1.adpolestar.net" : "127.0.0.1",
        "advstat.xunlei.com" : "127.0.0.1",
        "mpv.sandai.net" : "127.0.0.1",
        "asimgs.pplive.cn" : "127.0.0.1"
    },
    "HSTS_DOMAINS" : {
        "developers.facebook.com": 1,
        "groups.google.com": 1,
        "www.paypal.com" : 1,
        "www.elanex.biz" : 1,
        "jottit.com" : 1,
        "sunshinepress.org" : 1,
        "www.noisebridge.net" : 1,
        "neg9.org" : 1,
        "riseup.net" : 1,
        "factor.cc" : 1,
        "splendidbacon.com" : 1,
        "aladdinschools.appspot.com" : 1,
        "ottospora.nl" : 1,
        "www.paycheckrecords.com" : 1,
        "market.android.com" : 1,
        "lastpass.com" : 1,
        "www.lastpass.com" : 1,
        "keyerror.com" : 1,
        "entropia.de" : 1,
        "romab.com" : 1,
        "logentries.com" : 1,
        "stripe.com" : 1,
        "facebook.com": 1,
    },
    #collect domains that support HTTPS, to reduce usage of web proxy
    "HSTS_ON_EXCEPTION_DOMAINS" : {
        "s.ytimg.com": 1,
        "i1.ytimg.com": 1,
        "i2.ytimg.com": 1,
        "i3.ytimg.com": 1,
        "i4.ytimg.com": 1,
        "i1.tdimg.com": 1,
        "i2.tdimg.com": 1,
        "i3.tdimg.com": 1,
        "i4.tdimg.com": 1,
        "bits.wikimedia.org": 1,
        "www.wikipedia.org": 1,
        "www.google-analytics.com": 1,
        "apps.facebook.com": 1,
        "graph.facebook.com": 1,
        "www.youtube.com": 1,
        "m.facebook.com": 1,
    },
    "BLOCKED_DOMAINS": {
        "baidu.jp" : True,
        "search.twitter.com" : True,
        "www.baidu.jp" : True,
        "www.nicovideo.jp": True,
        "www.dailymotion.com": True,
        "ext.nicovideo.jp": True,
        "blog.roodo.com": True,
        "www.dwnews.com": True,
        "china.dwnews.com": True,
        "www.mediafire.com": True,
        "thepiratebay.org": True,
        "thepiratebay.se": True,
        "www.bbc.co.uk": True,
        "chinadigitaltimes.net": True,
        "www.wenxuecity.com": True,
        "bbs.wenxuecity.com": True,
        "www.blogger.com": True,
        "blogger.com": True,
        "plarouter.com": True,
    },
    "BLOCKED_IPS": {
        "23.21.220.40":1, "23.21.242.194":1, #dropbox
        "50.16.240.166":1, #dropbox
        "70.86.20.29" : 1, #www.bullogger.com
        "66.220.146.101": 1,
        "69.171.224.53": 1,
        "66.220.158.11": 1,
        "69.171.242.11": 1,
        "69.93.206.250": 1, #www.xys.org
        "69.163.141.215": 1, #www.zuola.com
        "174.121.98.156": 1,
        "50.22.53.157": 1,
        "50.22.53.155": 1,
        "50.63.43.1": 1,
        "72.32.231.8": 1,
        "72.52.81.24": 1,
        "72.233.2.58": 1,
        "74.125.31.141": 1,
        "74.125.39.102": 1,
        "174.121.66.230": 1,
        "107.20.170.126": 1,
        "180.235.96.30": 1,
        "204.236.224.226": 1,
        "69.163.223.11": 1, #letscorp.net
        "106.187.39.89": 1,
    },
    "BLOCKED_IPS_M16": {
        "174.129" : 1,
        "50.23": 1,
    },
    "BLOCKED_IPS_M24": {
        "199.16.156": 1,
        "66.220.149": 1,
        "66.220.156": 1,
        "69.171.224": 1,
        "74.125.127": 1,
        "208.109.6": 1,
        "199.59.148": 1,
        "199.59.149": 1,
        "199.59.150": 1,
    },
    "PAGE_RELOAD_HTML": """<html>
    <head>
        <script type="text/javascript" charset="utf-8">
            window.location.reload();
        </script>
    </head>
    <body>
    </body></html>""",
}

# 69.171.228.0/24 for facebook
blockedIpString = """69.171.228.5
69.171.228.6
69.171.228.11
69.171.228.12
69.171.228.15
69.171.228.16
69.171.228.19
69.171.228.20
69.171.228.23
69.171.228.24
69.171.228.27
69.171.228.28
69.171.228.31
69.171.228.35
69.171.228.36
69.171.228.50
69.171.228.51
69.171.228.70
69.171.228.71
69.171.228.74
69.171.228.75
69.171.228.79
69.171.228.229
69.171.228.230
69.171.228.231
69.171.228.232
69.171.228.233
69.171.228.234
69.171.228.244
69.171.228.245
69.171.228.246
69.171.228.247
69.171.228.248
69.171.228.249
69.171.228.250
69.171.228.251
69.171.228.252
69.171.228.253
69.171.228.254
"""

# 69.171.229.0/24 for facebook
blockedIpString += """69.171.229.11
69.171.229.12
69.171.229.13
69.171.229.14
69.171.229.15
69.171.229.16
69.171.229.20
69.171.229.23
69.171.229.24
69.171.229.27
69.171.229.28
69.171.229.31
69.171.229.32
69.171.229.46
69.171.229.47
69.171.229.51
69.171.229.70
69.171.229.71
69.171.229.72
69.171.229.73
69.171.229.74
69.171.229.76
69.171.229.77
69.171.229.229
69.171.229.230
69.171.229.231
69.171.229.232
69.171.229.233
69.171.229.234
69.171.229.244
69.171.229.245
69.171.229.246
69.171.229.247
69.171.229.248
69.171.229.249
69.171.229.250
69.171.229.251
69.171.229.252
69.171.229.253
69.171.229.254
"""

# 69.171.224.0/24 for facebook
blockedIpString += """69.171.224.1
69.171.224.2
69.171.224.3
69.171.224.4
69.171.224.5
69.171.224.6
69.171.224.32
69.171.224.33
69.171.224.34
69.171.224.35
69.171.224.36
69.171.224.37
69.171.224.38
69.171.224.39
69.171.224.40
69.171.224.41
69.171.224.48
69.171.224.49
69.171.224.50
69.171.224.51
69.171.224.52
69.171.224.53
69.171.224.54
69.171.224.55
69.171.224.56
69.171.224.57
69.171.224.64
69.171.224.65
69.171.224.66
69.171.224.67
69.171.224.68
69.171.224.80
69.171.224.81
69.171.224.82
69.171.224.83
69.171.224.84
69.171.224.96
69.171.224.97
69.171.224.98
69.171.224.99
69.171.224.100
69.171.224.112
69.171.224.113
69.171.224.114
69.171.224.115
69.171.224.116"""

# 69.171.234.0/24 for facebook
blockedIpString += """
69.171.234.16
69.171.234.17
69.171.234.19
69.171.234.32
69.171.234.35
69.171.234.48
69.171.234.49
69.171.234.64
69.171.234.65
69.171.234.68
69.171.234.80
69.171.234.82
69.171.234.83
69.171.234.96
69.171.234.98"""

# 74.125.0.0/16
blockedIpString += """74.125.71.88
74.125.71.89
74.125.71.99
74.125.71.100
74.125.71.101
74.125.71.106
74.125.71.113
74.125.71.116
74.125.71.121
74.125.71.128
74.125.71.138
74.125.71.139
74.125.71.150
74.125.71.160
74.125.71.161
74.125.71.162
74.125.71.163
74.125.71.188
74.125.71.192
"""

for ip in blockedIpString.split("\n"):
    if len(ip) > 0:
        gConfig["BLOCKED_IPS"][ip] = 1

blockedDomainString = """0to255.com
1-apple.com.tw
12vpn.com
173ng.com
1984bbs.org
1pondo.tv
2008xianzhang.info
213.251.145.96
301works.org
315lz.com
365singles.com.ar
36rain.com
4bluestones.biz
6park.com
7capture.com
89-64.org
9999cn.com
99bbs.com
9bis.com
9bis.net
aboutgfw.com
acgkj.com
aculo.us
adult168.com
adultfriendfinder.com
advanscene.com
advertfan.com
aenhancers.com
aftygh.gov.tw
ait.org.tw
aiweiweiblog.com
aiyori.org
alabout.com
alasbarricadas.org
alexlur.org
alkasir.com
allaboutalpha.com
alliance.org.hk
allonlinux.free.fr
alternate-tools.com
alwaysdata.net
americangreencard.com
anchorfree.com
anthonycalzadilla.com
antiwave.net
aolchannels.aol.com
api.proxlet.com
apigee.com
app.heywire.com
appledaily.com.tw
apps.hloli.net
archive.org
areca-backup.org
art-or-porn.com
asiaharvest.org
atnext.com
axureformac.com
badassjs.com
basetimesheightdividedby2.com
bbs.51.ca
bbs.kimy.com.tw
bbs.morbell.com
bbsfeed.com
bd.zhe.la
beijing1989.com
beijingspring.com
benjaminste.in
berlintwitterwall.com
bestforchina.org
beta.usejump.com
bettween.com
bfnn.org
bignews.org
bigsound.org
bill2-software.com
billywr.com
blinkx.com
blockcn.com
blog.51.ca
blog.aiweiwei.com
blog.birdhouseapp.com
blog.bitly.com
blog.boxcar.io
blog.chinatimes.com
blog.dayoneapp.com
blog.dribbble.com
blog.fizzik.com
blog.foolsmountain.com
blog.gowalla.com
blog.hotpotato.com
blog.ifttt.com
blog.instagram.com
blog.iphone-dev.org
blog.joeyrobert.org
blog.kangye.org
blog.kl.am
blog.lightbox.com
blog.mongodb.org
blog.path.com
blog.pchome.com.tw
blog.pentalogic.net
blog.pikchur.com
blog.pilotmoon.com
blog.rockmelt.com
blog.romanandreg.com
blog.sogoo.org
blog.sparrowmailapp.com
blog.usa.gov
blog.xuite.net
blogcatalog.com
blogimg.jp
bloodshed.net
boardreader.com
bobulate.com
bolin.netfirms.com
bonjourlesgeeks.com
books.com.tw
bookshelfporn.com
bot.nu
bowenpress.com
boxun.com
boxun.tv
br.st
bralio.com
brandonhutchinson.com
break.com
breakingtweets.com
brightkite.com
brizzly.com
budaedu.org
bugbeep.com
bugclub.org
bullog.org
bullogger.com
c-est-simple.com
c-spanvideo.org
c1522.mooo.com
calebelston.com
canadameet.com
caobian.info
caochangqing.com
catholic.org.hk
cbs.ntu.edu.tw
cc9007.spaces.live.com
cdjp.org
cdpweb.org
cecc.gov
changp.com
chaos.e-spacy.com
chengmingmag.com
cherrysave.com
chevronwp7.com
china101.com
chinaaffairs.org
chinacomments.org
chinadigitaltimes.net
chinaeweekly.com
chinagfw.org
chinagreenparty.org
chinainterimgov.org
chinasocialdemocraticparty.com
chinaway.org
chinaworker.info
chinesen.de
chinesenewsnet.com
chrispederick.com
chrispederick.net
christianstudy.com
chrlcg-hk.org
chuizi.net
civicparty.hk
civilhrfront.org
cl.ly
classicalguitarblog.net
clientsfromhell.net
cn.dayabook.com
cnd.org
cocoa.zonble.net
codeboxapp.com
comefromchina.com
comnews.gio.gov.tw
cookingtothegoodlife.com
coolaler.com
coolder.com
cpj.org
crd-net.org
crossthewall.net
csuchen.de
cubicle17.com
cyberghost.natado.com
cydia.ifuckgfw.com
cynscribe.com
dabr.co.uk
dabr.mobi
dadazim.com
dailymotion.com
dajiyuan.com
dalailamaworld.com
dalianmeng.org
danke4china.net
dapu-house.gov.tw
davidslog.com
default.secureserver.net
democrats.org
derekhsu.homeip.net
desc.se
deutsche-welle.de
developers.box.net
devio.us
diaoyuislands.org
digitalnomadsproject.org
dimitrik.free.fr
discuss.com.hk
dit-inc.us
dl.box.net
dojin.com
dongde.com
dongtaiwang.com
dongtaiwang.net
dongyangjing.com
dotheyfolloweachother.com
dowei.org
doxygen.org
dphk.org
dtiblog.com
dtiserv2.com
duckmylife.com
duihua.org
duoweitimes.com
duping.net
dupola.com
dupola.net
dw-world.com
dw-world.de
dwnews.com
dzze.com
eamonnbrennan.com
echofon.com
edubridge.com
eevpn.com
efksoft.com
eic-av.com
emacsblog.org
en.favotter.net
epochtimes.com
erights.net
eriversoft.com
ernestmandel.org
etizer.org
etools.ncol.com
everyday-carry.com
exploader.net
f.cl.ly
falsefire.com
fanfou.im
fangbinxing.com
fangeming.com
farwestchina.com
faststone.org
fbcdn.net
fc2.com
feer.com
fgmtv.org
fileserve.com
fillthesquare.org
firstfivefollowers.com
flecheinthepeche.fr
fourface.nodesnoop.com
fourthinternational.org
fredwilson.vc
free-ssh.com
free-vpn.info
freegateget.googlepages.com
freessh.us
freewallpaper4.me
freexinwen.com
friendfeed.com
frommel.net
fsurf.com
ftchinese.com
funp.com
furinkan.com
furl.net
futurechinaforum.org
futuremessage.org
gabocorp.com
gaoming.net
gardennetworks.com
gardennetworks.org
gartlive.com
gather.com
geek-art.net
geekmade.co.uk
generesis.com
getcloudapp.com
getsmartlinks.com
ggssl.com
ginx.com
givemesomethingtoread.com
globalmuseumoncommunism.org
globalvoicesonline.org
gmhz.org
goldwave.com
gongmeng.info
gongminliliang.com
goodreaders.com
goodreads.com
gopetition.com
gov.tw
gpass1.com
grandtrial.org
graphis.ne.jp
great-firewall.com
greatfirewall.biz
greenvpn.net
gtricks.com
guancha.org
gzone-anime.info
h-china.org
hahlo.com
hasaowall.com
hcc.gov.tw
hdtvb.net
heartyit.com
hechaji.com
hellonewyork.us
helloqueer.com
hellotxt.com
helpeachpeople.com
hen.bao.li
highrockmedia.com
hihiforum.com
hiitch.com
hjclub.info
hk.myblog.yahoo.com
hk32168.com
hkgolden.com
hkjp.org
hkreporter.com
hkzone.org
hnjhj.com
hootsuite.com
hotspotshield.com
hougaige.com
hqcdp.org
hudatoriq.web.id
huping.net
hutianyi.net
hwinfo.com
i2p2.de
ialmostlaugh.com
identi.ca
ifcss.org
illusionfactory.com
ilove80.be
im.tv
imageflea.com
imagevenue.com
imkev.com
incredibox.fr
iner.gov.tw
info.51.ca
interestinglaugh.com
internationalrivers.org
internetfreedom.org
internetpopculture.com
ipicture.ru
ippotv.com
ironicsoftware.com
ironpython.net
ithelp.ithome.com.tw
itweet.net
jayparkinsonmd.com
joachims.org
juliereyc.com
jyzj.waqn.com
k2.xrea.com
ka-wai.com
kagyuoffice.org.tw
kanzhongguo.com
khcc.gov.tw
kineox.free.fr
kinghost.com
kk.gov.tw
klccab.gov.tw
kmh.gov.tw
kompozer.net
koolsolutions.com
kt.kcome.org
kurtmunger.com
ladbrokes.com
laogai.org
laomiu.com
laptoplockdown.com
lenwhite.com
lesscss.org
letscorp.net
liaowangxizang.net
libertytimes.com.tw
linux-engineer.net
list.ly
littlebigdetails.com
liudejun.com
liujianshu.com
livevideo.com
log.riku.me
london.neighborhoodr.com
longtermly.net
lookingglasstheatre.org
lovequicksilver.com
lsforum.net
lupm.org
lvhai.org
lyricsquote.com
m.plixi.com
m.slandr.net
m.tweete.net
madmenunbuttoned.com
magazines.sina.com.tw
mail-archive.com
makemymood.com
markmilian.com
marxist.net
mashable.com
matainja.com
megurineluka.com
melon-peach.com
mesotw.com
middle-way.net
mimivip.com
minghui.org
mingpao.com
minimalmac.com
mitbbs.com
mixero.com
mizzmona.com
mk5000.com
mlcool.com
mmaaxx.com
mobileways.de
modfetish.com
mondex.org
morningsun.org
moviefap.com
mpinews.com
mrtweet.com
msguancha.com
mtw.tl
multiply.com
mvdis.gov.tw
my.keso.cn
mychinamyhome.com
mypaper.pchome.com.tw
myparagliding.com
mypopescu.com
myvlog.im.tv
n.yam.com
navigeaters.com
ncree.gov.tw
networkedblogs.com
newcenturymc.com
newchen.com
news.pchome.com.tw
news.pts.org.tw
news.sina.com.hk
news.sina.com.tw
news.yam.com
newsminer.com
newtalk.tw
nexton-net.jp
ngensis.com
nhri.gov.tw
nicovideo.jp
nmp.gov.tw
nmtl.gov.tw
notes.alexdong.com
nrk.no
ntdtv.com
nurgo-software.com
observechina.net
october-review.org
ohloh.net
olumpo.com
osfoora.com
ourdearamy.com
oursogo.com
ow.ly
pacificpoker.com
pandora.tv
paper-replika.com
pbwiki.com
pbworks.com
pbxes.com
pbxes.org
peacehall.com
peerpong.com
pekingduck.org
penchinese.com
pengyulong.com
pign.net
ping.fm
plusbb.com
popyard.org
porn2.com
post.anyu.org
powerapple.com
powercx.com
privacybox.de
prosiben.de
proxomitron.info
prozz.net
psiphon.civisec.org
ptt.cc
pulse.yahoo.com
pureconcepts.net
purepdf.com
puttycm.free.fr
qkshare.com
qoos.com
qstatus.com
qtweeter.com
quadedge.com
qvodzy.org
r.mzstatic.com
radiovaticana.org
rangzen.org
ranyunfei.com
rayfme.com
read100.com
readingtimes.com.tw
redtube.com
referer.us
renminbao.com
renyurenquan.org
retweeteffect.com
retweetrank.com
rfachina.com
rileyguide.com
rocmp.org
rsf-chinese.org
rsf.org
rthk.org.hk
rubyinstaller.org
rutube.ru
sacom.hk
salvation.org.hk
sandnoble.com
sanmin.com.tw
sapikachu.net
savetibet.org
secretchina.com
secretgarden.no
secure.wikimedia.org
seezone.net
sendoid.com
sesawe.net
sexandsubmission.com
sfileydy.com
shangfang.org
shapeservices.com
share.youthwant.com.tw
sharecool.org
sharkdolphin.com
shaunthesheep.com
shell.cjb.net
shenshou.org
shizhao.org
sitebro.tw
skimtube.com
slavasoft.com
slinkset.com
smile-cca22.nicovideo.jp
sobees.com
sod.co.jp
sogclub.com
sokamonline.com
soundofhope.org
soup.io
space-scape.com
speckleapp.com
spencertipping.com
starp2p.com
sthoo.com
stickam.com
stickeraction.com
storagenewsletter.com
strongvpn.com
subacme.rerouted.org
sugarsync.com
sytes.net
t.co
t.orzdream.com
t35.com
tagwalk.com
taiwankiss.com
taiwannation.50webs.com
taiwantt.org.tw
tangben.com
taolun.info
tbpic.info
tchb.gov.tw
tchrd.org
teamseesmic.com
techlifeweb.com
technorati.com
techparaiso.com
the-sun.on.cc
thebcomplex.com
thedw.us
thepiratebay.org
thepiratebay.se
thetibetpost.com
thetrotskymovie.com
tianhuayuan.com
tiantibooks.org
tianzhu.org
tibet.com
tibet.net
tibet.org.tw
tibetwrites.org
tncsec.gov.tw
tomayko.com
toutfr.com
transgressionism.org
travelinlocal.com
trendsmap.com
trustedbi.com
tsquare.tv
tuanzt.com
tui.orzdream.com
turbobit.net
turbotwitter.com
tv-intros.com
tv.com
tvunetworks.com
tw.news.yahoo.com
twa.sh
twbbs.org
tweepguide.com
tweeplike.me
tweete.net
tweetmeme.com
tweetree.com
tweetwally.com
twibase.com
twibs.com
twifan.com
twiffo.com
twimbow.com
twistar.cc
twisternow.com
twit2d.com
twitlonger.com
twitoaster.com
twitonmsn.com
twitpic.com
twitstat.com
twitter.com
twitter.jp
twittergadget.com
twitthat.com
twiyia.com
twstar.net
twt.fm
twtr2src.ogaoga.org
twttr.com
twyac.org
ultravpn.fr
ultraxs.com
unholyknight.com
unknownspace.org
urlparser.com
us.to
usacn.com
usinfo.state.gov
usmc.mil
uwants.net
v70.us
veempiire.com
veoh.com
views.fm
vinniev.com
voachineseblog.com
waffle1999.com
wahas.com
wanderinghorse.net
wanfang.gov.tw
wangjinbo.org
web.pts.org.tw
web2project.net
webshots.com
weigegebyc.dreamhosters.com
weijingsheng.org
wengewang.com
wengewang.org
wenku.com
wenxuecity.com
wenyunchao.com
westca.com
wexiaobo.org
wezhiyong.org
wforum.com
whereiswerner.com
whyx.org
wiki.jqueryui.com
wiki.keso.cn
wiki.oauth.net
wiki.phonegap.com
wikimedia.org.mo
wikiwiki.jp
willw.net
wiredbytes.com
wlx.sowiki.net
woeser.com
woopie.jp
wordpress.com
worldjournal.com
wpoforum.com
wqyd.org
wuerkaixi.com
wufi.org.tw
wujie.net
wukangrui.net
www.freetibet.org
www.getyouram.com
www.kanzhongguo.com
www.macrovpn.com
www.mitbbs.com
www.moztw.org
www.powerpointninja.com
www.tv.com
www.vegorpedersen.com
www.voy.com
www.vpncup.com
www.wan-press.org
www.zaurus.org.uk
x365x.com
xiezhua.com
xinsheng.net
xizang-zhiye.org
xxxx.com.au
xys.dxiong.com
xys.org
yatsen.gov.tw
yegle.net
yidio.com
yilubbs.com
yipub.com
yong.hu
youmaker.com
youpai.org
your-freedom.net
yunchao.net
yyii.org
yzzk.com
zarias.com
zeutch.com
zh.pokerstrategy.com
zhao.jinhai.de
zhongmeng.org
zhufeng.me
zlib.net
zonaeuropa.com
zuihulu.net
zuo.la"""

gConfig["BLOCKED_DOMAINS_LIST"] = blockedDomainString.split("\n")
for d in blockedDomainString.split("\n"):
    if len(d) > 0:
        gConfig["BLOCKED_DOMAINS"][d] = True

gConfig["CHINA_IP_LIST"] = ["1.0.1.0/24","1.0.2.0/23","1.0.8.0/21","1.0.32.0/19","1.1.0.0/24","1.1.2.0/23","1.1.4.0/22","1.1.8.0/21","1.1.16.0/20","1.1.32.0/19","1.2.0.0/23","1.2.2.0/24","1.2.4.0/24","1.2.5.0/24","1.2.6.0/23","1.2.8.0/24","1.2.9.0/24","1.2.10.0/23","1.2.12.0/22","1.2.16.0/20","1.2.32.0/19","1.2.64.0/18","1.3.0.0/16","1.4.1.0/24","1.4.2.0/23","1.4.4.0/24","1.4.5.0/24","1.4.6.0/23","1.4.8.0/21","1.4.16.0/20","1.4.32.0/19","1.4.64.0/18","1.8.0.0/16","1.10.0.0/21","1.10.8.0/23","1.10.11.0/24","1.10.12.0/22","1.10.16.0/20","1.10.32.0/19","1.10.64.0/18","1.12.0.0/14","1.24.0.0/13","1.45.0.0/16","1.48.0.0/15","1.50.0.0/16","1.51.0.0/16","1.56.0.0/13","1.68.0.0/14","1.80.0.0/13","1.88.0.0/14","1.92.0.0/15","1.94.0.0/15","1.116.0.0/14","1.180.0.0/14","1.184.0.0/15","1.188.0.0/14","1.192.0.0/13","1.202.0.0/15","1.204.0.0/14","14.0.0.0/21","14.0.12.0/22","14.1.0.0/22","14.16.0.0/12","14.102.128.0/22","14.102.156.0/22","14.103.0.0/16","14.104.0.0/13","14.112.0.0/12","14.130.0.0/15","14.134.0.0/15","14.144.0.0/12","14.192.60.0/22","14.192.76.0/22","14.196.0.0/15","14.204.0.0/15","14.208.0.0/12","27.8.0.0/13","27.16.0.0/12","27.34.232.0/21","27.36.0.0/14","27.40.0.0/13","27.50.40.0/21","27.50.128.0/17","27.54.72.0/21","27.54.152.0/21","27.54.192.0/18","27.98.208.0/20","27.98.224.0/19","27.99.128.0/17","27.103.0.0/16","27.106.128.0/18","27.106.204.0/22","27.109.32.0/19","27.112.0.0/18","27.112.80.0/20","27.113.128.0/18","27.115.0.0/17","27.116.44.0/22","27.121.72.0/21","27.121.120.0/21","27.128.0.0/15","27.131.220.0/22","27.144.0.0/16","27.148.0.0/14","27.152.0.0/13","27.184.0.0/13","27.192.0.0/11","27.224.0.0/14","36.0.0.0/22","36.0.8.0/21","36.0.16.0/20","36.0.32.0/19","36.0.64.0/18","36.0.128.0/17","36.1.0.0/16","36.4.0.0/14","36.16.0.0/12","36.32.0.0/14","36.36.0.0/16","36.37.0.0/19","36.37.36.0/23","36.37.39.0/24","36.37.40.0/21","36.37.48.0/20","36.40.0.0/13","36.48.0.0/15","36.51.0.0/16","36.56.0.0/13","36.96.0.0/11","36.128.0.0/10","36.192.0.0/11","36.248.0.0/14","36.254.0.0/16","39.0.0.0/24","39.0.2.0/23","39.0.4.0/22","39.0.8.0/21","39.0.16.0/20","39.0.32.0/19","39.0.64.0/18","39.0.128.0/17","39.64.0.0/11","39.128.0.0/10","42.0.0.0/22","42.0.8.0/21","42.0.16.0/21","42.0.24.0/22","42.0.32.0/19","42.0.128.0/17","42.1.0.0/19","42.1.32.0/20","42.1.48.0/21","42.1.56.0/22","42.1.128.0/17","42.4.0.0/14","42.48.0.0/15","42.50.0.0/16","42.51.0.0/16","42.52.0.0/14","42.56.0.0/14","42.62.0.0/17","42.62.128.0/19","42.62.160.0/20","42.62.180.0/22","42.62.184.0/21","42.63.0.0/16","42.80.0.0/15","42.83.64.0/20","42.83.80.0/22","42.83.88.0/21","42.83.96.0/19","42.83.128.0/17","42.84.0.0/14","42.88.0.0/13","42.96.64.0/19","42.96.96.0/21","42.96.108.0/22","42.96.112.0/20","42.96.128.0/17","42.97.0.0/16","42.99.0.0/18","42.99.64.0/19","42.99.96.0/20","42.99.112.0/22","42.99.120.0/21","42.100.0.0/14","42.120.0.0/15","42.122.0.0/16","42.123.0.0/19","42.123.36.0/22","42.123.40.0/21","42.123.48.0/20","42.123.64.0/18","42.123.128.0/17","42.128.0.0/12","42.156.0.0/19","42.156.36.0/22","42.156.40.0/21","42.156.48.0/20","42.156.64.0/18","42.156.128.0/17","42.157.0.0/16","42.158.0.0/15","42.160.0.0/12","42.176.0.0/13","42.184.0.0/15","42.186.0.0/16","42.187.0.0/18","42.187.64.0/19","42.187.96.0/20","42.187.112.0/21","42.187.120.0/22","42.187.128.0/17","42.192.0.0/15","42.194.0.0/21","42.194.8.0/22","42.194.12.0/22","42.194.16.0/20","42.194.32.0/19","42.194.64.0/18","42.194.128.0/17","42.195.0.0/16","42.196.0.0/14","42.201.0.0/17","42.202.0.0/15","42.204.0.0/14","42.208.0.0/12","42.224.0.0/12","42.240.0.0/17","42.240.128.0/17","42.242.0.0/15","42.244.0.0/14","42.248.0.0/13","49.4.0.0/14","49.51.0.0/16","49.52.0.0/14","49.64.0.0/11","49.112.0.0/13","49.120.0.0/14","49.128.0.0/24","49.128.2.0/23","49.140.0.0/15","49.152.0.0/14","49.208.0.0/15","49.210.0.0/15","49.220.0.0/14","49.232.0.0/14","49.239.0.0/18","49.239.192.0/18","49.246.224.0/19","58.14.0.0/15","58.16.0.0/16","58.17.0.0/17","58.17.128.0/17","58.18.0.0/16","58.19.0.0/16","58.20.0.0/16","58.21.0.0/16","58.22.0.0/15","58.24.0.0/15","58.30.0.0/15","58.32.0.0/13","58.40.0.0/15","58.42.0.0/16","58.43.0.0/16","58.44.0.0/14","58.48.0.0/13","58.56.0.0/15","58.58.0.0/16","58.59.0.0/17","58.59.128.0/17","58.60.0.0/14","58.65.232.0/21","58.66.0.0/15","58.68.128.0/17","58.82.0.0/15","58.87.64.0/18","58.99.128.0/17","58.100.0.0/15","58.116.0.0/14","58.128.0.0/13","58.144.0.0/16","58.154.0.0/15","58.192.0.0/15","58.194.0.0/15","58.196.0.0/15","58.198.0.0/15","58.200.0.0/13","58.208.0.0/12","58.240.0.0/15","58.242.0.0/15","58.244.0.0/15","58.246.0.0/15","58.248.0.0/13","59.32.0.0/13","59.40.0.0/15","59.42.0.0/16","59.43.0.0/16","59.44.0.0/14","59.48.0.0/16","59.49.0.0/17","59.49.128.0/17","59.50.0.0/16","59.51.0.0/17","59.51.128.0/17","59.52.0.0/14","59.56.0.0/14","59.60.0.0/15","59.62.0.0/15","59.64.0.0/14","59.68.0.0/14","59.72.0.0/15","59.74.0.0/15","59.76.0.0/16","59.77.0.0/16","59.78.0.0/15","59.80.0.0/14","59.107.0.0/17","59.107.128.0/17","59.108.0.0/15","59.110.0.0/15","59.151.0.0/17","59.155.0.0/16","59.172.0.0/15","59.174.0.0/15","59.191.0.0/17","59.191.240.0/20","59.192.0.0/10","60.0.0.0/13","60.8.0.0/15","60.10.0.0/16","60.11.0.0/16","60.12.0.0/16","60.13.0.0/18","60.13.64.0/18","60.13.128.0/17","60.14.0.0/15","60.16.0.0/13","60.24.0.0/14","60.28.0.0/15","60.30.0.0/16","60.31.0.0/16","60.55.0.0/16","60.63.0.0/16","60.160.0.0/15","60.162.0.0/15","60.164.0.0/15","60.166.0.0/15","60.168.0.0/13","60.176.0.0/12","60.194.0.0/15","60.200.0.0/14","60.204.0.0/16","60.205.0.0/16","60.206.0.0/15","60.208.0.0/13","60.216.0.0/15","60.218.0.0/15","60.220.0.0/14","60.232.0.0/15","60.235.0.0/16","60.245.128.0/17","60.247.0.0/16","60.252.0.0/16","60.253.128.0/17","60.255.0.0/16","61.4.80.0/22","61.4.84.0/22","61.4.88.0/21","61.4.176.0/20","61.8.160.0/20","61.28.0.0/20","61.28.16.0/20","61.28.32.0/19","61.28.64.0/18","61.29.128.0/18","61.29.192.0/19","61.29.224.0/20","61.29.240.0/20","61.45.128.0/18","61.45.224.0/20","61.47.128.0/18","61.48.0.0/14","61.52.0.0/15","61.54.0.0/16","61.55.0.0/16","61.87.192.0/18","61.128.0.0/15","61.130.0.0/15","61.132.0.0/16","61.133.0.0/17","61.133.128.0/17","61.134.0.0/18","61.134.64.0/19","61.134.96.0/19","61.134.128.0/18","61.134.192.0/18","61.135.0.0/16","61.136.0.0/18","61.136.64.0/18","61.136.128.0/17","61.137.0.0/17","61.137.128.0/17","61.138.0.0/18","61.138.64.0/18","61.138.128.0/18","61.138.192.0/18","61.139.0.0/17","61.139.128.0/18","61.139.192.0/18","61.140.0.0/14","61.144.0.0/14","61.148.0.0/15","61.150.0.0/15","61.152.0.0/16","61.153.0.0/16","61.154.0.0/15","61.156.0.0/16","61.157.0.0/16","61.158.0.0/17","61.158.128.0/17","61.159.0.0/18","61.159.64.0/18","61.159.128.0/17","61.160.0.0/16","61.161.0.0/18","61.161.64.0/18","61.161.128.0/17","61.162.0.0/16","61.163.0.0/16","61.164.0.0/16","61.165.0.0/16","61.166.0.0/16","61.167.0.0/16","61.168.0.0/16","61.169.0.0/16","61.170.0.0/15","61.172.0.0/14","61.176.0.0/16","61.177.0.0/16","61.178.0.0/16","61.179.0.0/16","61.180.0.0/17","61.180.128.0/17","61.181.0.0/16","61.182.0.0/16","61.183.0.0/16","61.184.0.0/14","61.188.0.0/16","61.189.0.0/17","61.189.128.0/17","61.190.0.0/15","61.232.0.0/14","61.236.0.0/15","61.240.0.0/14","101.0.0.0/22","101.1.0.0/22","101.2.172.0/22","101.4.0.0/14","101.16.0.0/12","101.32.0.0/12","101.48.0.0/15","101.50.56.0/22","101.52.0.0/16","101.53.100.0/22","101.54.0.0/16","101.55.224.0/21","101.64.0.0/13","101.72.0.0/14","101.76.0.0/15","101.78.0.0/22","101.78.32.0/19","101.80.0.0/12","101.96.0.0/21","101.96.8.0/22","101.96.16.0/20","101.96.128.0/17","101.99.96.0/19","101.101.64.0/19","101.101.100.0/24","101.101.102.0/23","101.101.104.0/21","101.101.112.0/20","101.102.64.0/19","101.102.100.0/23","101.102.102.0/24","101.102.104.0/21","101.102.112.0/20","101.104.0.0/14","101.110.64.0/19","101.110.96.0/20","101.110.116.0/22","101.110.120.0/21","101.120.0.0/14","101.124.0.0/15","101.126.0.0/16","101.128.0.0/22","101.128.8.0/21","101.128.16.0/20","101.128.32.0/19","101.129.0.0/16","101.130.0.0/15","101.132.0.0/14","101.144.0.0/12","101.192.0.0/14","101.196.0.0/14","101.200.0.0/15","101.203.128.0/19","101.203.160.0/21","101.203.172.0/22","101.203.176.0/20","101.204.0.0/14","101.224.0.0/13","101.232.0.0/15","101.234.64.0/21","101.234.76.0/22","101.234.80.0/20","101.234.96.0/19","101.236.0.0/14","101.240.0.0/14","101.244.0.0/14","101.248.0.0/15","101.251.0.0/22","101.251.8.0/21","101.251.16.0/20","101.251.32.0/19","101.251.64.0/18","101.251.128.0/17","101.252.0.0/15","101.254.0.0/16","103.1.8.0/22","103.1.20.0/22","103.1.24.0/22","103.1.72.0/22","103.1.88.0/22","103.1.168.0/22","103.2.108.0/22","103.2.156.0/22","103.2.164.0/22","103.2.200.0/22","103.2.204.0/22","103.2.208.0/22","103.2.212.0/22","103.3.84.0/22","103.3.88.0/22","103.3.92.0/22","103.3.96.0/22","103.3.100.0/22","103.3.104.0/22","103.3.108.0/22","103.3.112.0/22","103.3.116.0/22","103.3.120.0/22","103.3.124.0/22","103.3.128.0/22","103.3.132.0/22","103.3.136.0/22","103.3.140.0/22","103.3.148.0/22","103.3.152.0/22","103.3.156.0/22","103.4.56.0/22","103.4.168.0/22","103.4.184.0/22","103.5.36.0/22","103.5.52.0/22","103.5.56.0/22","103.5.252.0/22","103.6.76.0/22","103.6.220.0/22","103.7.4.0/22","103.7.28.0/22","103.7.212.0/22","103.7.216.0/22","103.7.220.0/22","103.8.4.0/22","103.8.8.0/22","103.8.32.0/22","103.8.52.0/22","103.8.108.0/22","103.8.156.0/22","103.8.200.0/22","103.8.204.0/22","103.8.220.0/22","103.9.152.0/22","103.9.248.0/22","103.9.252.0/22","103.10.0.0/22","103.10.16.0/22","103.10.84.0/22","103.10.111.0/24","103.10.140.0/22","103.11.180.0/22","103.12.32.0/22","103.12.68.0/22","103.12.136.0/22","103.12.184.0/22","103.12.232.0/22","103.13.124.0/22","103.13.144.0/22","103.13.196.0/22","103.13.244.0/22","103.14.84.0/22","103.14.112.0/22","103.14.132.0/22","103.14.136.0/22","103.14.156.0/22","103.14.240.0/22","103.15.4.0/22","103.15.8.0/22","103.15.16.0/22","103.22.0.0/22","103.22.4.0/22","103.22.8.0/22","103.22.12.0/22","103.22.16.0/22","103.22.20.0/22","103.22.24.0/22","103.22.28.0/22","103.22.32.0/22","103.22.36.0/22","103.22.40.0/22","103.22.44.0/22","103.22.48.0/22","103.22.52.0/22","103.22.56.0/22","103.22.60.0/22","103.22.64.0/22","103.22.68.0/22","103.22.72.0/22","103.22.76.0/22","103.22.80.0/22","103.22.84.0/22","103.22.88.0/22","103.22.92.0/22","103.22.100.0/22","103.22.104.0/22","103.22.108.0/22","103.22.112.0/22","103.22.116.0/22","103.22.120.0/22","103.22.124.0/22","103.22.188.0/22","103.22.228.0/22","103.22.252.0/22","103.23.8.0/22","103.23.56.0/22","103.23.160.0/22","103.23.164.0/22","103.23.176.0/22","103.23.228.0/22","103.28.4.0/22","103.28.8.0/22","103.28.204.0/22","103.29.16.0/22","103.29.128.0/22","103.29.132.0/22","103.29.136.0/22","103.246.8.0/22","103.246.12.0/22","103.246.120.0/22","103.246.124.0/22","103.246.132.0/22","103.246.152.0/22","103.246.156.0/22","103.247.168.0/22","103.247.172.0/22","103.247.176.0/22","103.247.200.0/22","103.247.212.0/22","106.0.0.0/24","106.0.2.0/23","106.0.4.0/22","106.0.8.0/21","106.0.16.0/20","106.0.64.0/18","106.2.0.0/15","106.4.0.0/14","106.8.0.0/15","106.11.0.0/16","106.12.0.0/14","106.16.0.0/12","106.32.0.0/12","106.48.0.0/15","106.50.0.0/16","106.52.0.0/14","106.56.0.0/13","106.74.0.0/15","106.80.0.0/12","106.108.0.0/14","106.112.0.0/13","106.120.0.0/13","106.224.0.0/12","110.6.0.0/15","110.16.0.0/14","110.40.0.0/14","110.44.144.0/20","110.48.0.0/16","110.51.0.0/16","110.52.0.0/15","110.56.0.0/13","110.64.0.0/15","110.72.0.0/15","110.75.0.0/17","110.75.128.0/19","110.75.160.0/19","110.75.192.0/18","110.76.0.0/19","110.76.32.0/19","110.76.156.0/22","110.76.184.0/22","110.76.192.0/18","110.77.0.0/17","110.80.0.0/13","110.88.0.0/14","110.93.32.0/19","110.94.0.0/15","110.96.0.0/11","110.152.0.0/14","110.156.0.0/15","110.165.32.0/19","110.166.0.0/15","110.172.192.0/18","110.173.0.0/19","110.173.32.0/20","110.173.64.0/19","110.173.96.0/19","110.173.192.0/19","110.176.0.0/13","110.184.0.0/13","110.192.0.0/11","110.228.0.0/14","110.232.32.0/19","110.236.0.0/15","110.240.0.0/12","111.0.0.0/10","111.66.0.0/16","111.67.192.0/20","111.68.64.0/19","111.72.0.0/13","111.85.0.0/16","111.91.192.0/19","111.112.0.0/15","111.114.0.0/15","111.116.0.0/15","111.118.200.0/21","111.119.64.0/18","111.119.128.0/19","111.120.0.0/14","111.124.0.0/16","111.126.0.0/15","111.128.0.0/11","111.160.0.0/13","111.170.0.0/16","111.172.0.0/14","111.176.0.0/13","111.186.0.0/15","111.192.0.0/12","111.208.0.0/14","111.212.0.0/14","111.221.128.0/17","111.222.0.0/16","111.223.240.0/22","111.223.248.0/22","111.224.0.0/14","111.228.0.0/14","111.235.96.0/19","111.235.156.0/22","111.235.160.0/19","112.0.0.0/10","112.64.0.0/15","112.66.0.0/15","112.73.0.0/16","112.74.0.0/15","112.80.0.0/13","112.88.0.0/13","112.96.0.0/15","112.98.0.0/15","112.100.0.0/14","112.109.128.0/17","112.111.0.0/16","112.112.0.0/14","112.116.0.0/15","112.122.0.0/15","112.124.0.0/14","112.128.0.0/14","112.132.0.0/16","112.137.48.0/21","112.192.0.0/14","112.224.0.0/11","113.0.0.0/13","113.8.0.0/15","113.11.192.0/19","113.12.0.0/14","113.16.0.0/15","113.18.0.0/16","113.24.0.0/14","113.31.0.0/16","113.44.0.0/14","113.48.0.0/14","113.52.160.0/19","113.54.0.0/15","113.56.0.0/15","113.58.0.0/16","113.59.0.0/17","113.59.224.0/22","113.62.0.0/15","113.64.0.0/11","113.96.0.0/12","113.112.0.0/13","113.120.0.0/13","113.128.0.0/15","113.130.96.0/20","113.130.112.0/21","113.132.0.0/14","113.136.0.0/13","113.194.0.0/15","113.197.100.0/22","113.200.0.0/15","113.202.0.0/16","113.204.0.0/14","113.208.96.0/19","113.208.128.0/17","113.209.0.0/16","113.212.0.0/18","113.212.100.0/22","113.212.184.0/21","113.213.0.0/17","113.214.0.0/15","113.218.0.0/15","113.220.0.0/14","113.224.0.0/12","113.240.0.0/13","113.248.0.0/14","114.28.0.0/16","114.54.0.0/15","114.60.0.0/14","114.64.0.0/14","114.68.0.0/16","114.79.64.0/18","114.80.0.0/12","114.96.0.0/13","114.104.0.0/14","114.110.0.0/20","114.110.64.0/18","114.111.0.0/19","114.111.160.0/19","114.112.0.0/14","114.116.0.0/15","114.118.0.0/15","114.132.0.0/16","114.135.0.0/16","114.138.0.0/15","114.141.64.0/21","114.141.128.0/18","114.196.0.0/15","114.198.248.0/21","114.208.0.0/14","114.212.0.0/15","114.214.0.0/16","114.215.0.0/16","114.216.0.0/13","114.224.0.0/12","114.240.0.0/12","115.24.0.0/14","115.28.0.0/15","115.32.0.0/14","115.44.0.0/15","115.46.0.0/16","115.47.0.0/16","115.48.0.0/12","115.69.64.0/20","115.84.0.0/18","115.84.192.0/19","115.85.192.0/18","115.100.0.0/14","115.104.0.0/14","115.120.0.0/14","115.124.16.0/20","115.148.0.0/14","115.152.0.0/15","115.154.0.0/15","115.156.0.0/15","115.158.0.0/16","115.159.0.0/16","115.166.64.0/19","115.168.0.0/14","115.172.0.0/14","115.180.0.0/14","115.190.0.0/15","115.192.0.0/11","115.224.0.0/12","116.0.8.0/21","116.0.24.0/21","116.1.0.0/16","116.2.0.0/15","116.4.0.0/14","116.8.0.0/14","116.13.0.0/16","116.16.0.0/12","116.50.0.0/20","116.52.0.0/14","116.56.0.0/15","116.58.128.0/20","116.58.208.0/20","116.60.0.0/14","116.66.0.0/17","116.69.0.0/16","116.70.0.0/17","116.76.0.0/15","116.78.0.0/15","116.85.0.0/16","116.89.144.0/20","116.90.80.0/20","116.90.184.0/21","116.95.0.0/16","116.112.0.0/14","116.116.0.0/15","116.128.0.0/10","116.192.0.0/16","116.193.16.0/20","116.193.32.0/19","116.193.176.0/21","116.194.0.0/15","116.196.0.0/16","116.198.0.0/16","116.199.0.0/17","116.199.128.0/19","116.204.0.0/15","116.207.0.0/16","116.208.0.0/14","116.212.160.0/20","116.213.64.0/18","116.213.128.0/17","116.214.32.0/19","116.214.64.0/20","116.214.128.0/17","116.215.0.0/16","116.216.0.0/14","116.224.0.0/12","116.242.0.0/15","116.244.0.0/15","116.246.0.0/15","116.248.0.0/15","116.251.64.0/18","116.252.0.0/15","116.254.128.0/17","116.255.128.0/17","117.8.0.0/13","117.21.0.0/16","117.22.0.0/15","117.24.0.0/13","117.32.0.0/13","117.40.0.0/14","117.44.0.0/15","117.48.0.0/14","117.53.48.0/20","117.53.176.0/20","117.57.0.0/16","117.58.0.0/17","117.59.0.0/16","117.60.0.0/14","117.64.0.0/13","117.72.0.0/15","117.74.64.0/20","117.74.80.0/20","117.74.128.0/17","117.75.0.0/16","117.76.0.0/14","117.80.0.0/12","117.100.0.0/15","117.103.16.0/20","117.103.40.0/21","117.103.72.0/21","117.103.128.0/20","117.104.168.0/21","117.106.0.0/15","117.112.0.0/13","117.120.64.0/18","117.120.128.0/17","117.121.0.0/17","117.121.128.0/18","117.121.192.0/21","117.122.128.0/17","117.124.0.0/14","117.128.0.0/10","118.24.0.0/15","118.26.0.0/16","118.27.0.0/16","118.28.0.0/15","118.30.0.0/16","118.31.0.0/16","118.64.0.0/15","118.66.0.0/16","118.67.112.0/20","118.72.0.0/13","118.80.0.0/15","118.84.0.0/15","118.88.32.0/19","118.88.64.0/18","118.88.128.0/17","118.89.0.0/16","118.91.240.0/20","118.102.16.0/20","118.102.32.0/21","118.112.0.0/13","118.120.0.0/14","118.124.0.0/15","118.126.0.0/16","118.127.128.0/19","118.132.0.0/14","118.144.0.0/14","118.178.0.0/16","118.180.0.0/14","118.184.0.0/16","118.185.0.0/16","118.186.0.0/15","118.188.0.0/16","118.190.0.0/15","118.192.0.0/15","118.194.0.0/17","118.194.128.0/17","118.195.0.0/16","118.196.0.0/14","118.202.0.0/15","118.204.0.0/14","118.212.0.0/16","118.213.0.0/16","118.224.0.0/14","118.228.0.0/15","118.230.0.0/16","118.239.0.0/16","118.242.0.0/16","118.244.0.0/14","118.248.0.0/13","119.0.0.0/15","119.2.0.0/19","119.2.128.0/17","119.3.0.0/16","119.4.0.0/14","119.8.0.0/16","119.10.0.0/17","119.15.136.0/21","119.16.0.0/16","119.18.192.0/20","119.18.208.0/21","119.18.224.0/20","119.18.240.0/20","119.19.0.0/16","119.20.0.0/14","119.27.64.0/18","119.27.128.0/19","119.27.160.0/19","119.27.192.0/18","119.28.0.0/15","119.30.48.0/20","119.31.192.0/19","119.32.0.0/14","119.36.0.0/16","119.37.0.0/17","119.37.128.0/18","119.37.192.0/18","119.38.0.0/17","119.38.128.0/18","119.38.192.0/20","119.38.208.0/20","119.38.224.0/19","119.39.0.0/16","119.40.0.0/18","119.40.64.0/20","119.40.128.0/17","119.41.0.0/16","119.42.0.0/19","119.42.128.0/21","119.42.136.0/21","119.42.224.0/19","119.44.0.0/15","119.48.0.0/13","119.57.0.0/16","119.58.0.0/16","119.59.128.0/17","119.60.0.0/16","119.61.0.0/16","119.62.0.0/16","119.63.32.0/19","119.75.208.0/20","119.78.0.0/15","119.80.0.0/16","119.82.208.0/20","119.84.0.0/14","119.88.0.0/14","119.96.0.0/13","119.108.0.0/15","119.112.0.0/13","119.120.0.0/13","119.128.0.0/12","119.144.0.0/14","119.148.160.0/20","119.148.176.0/20","119.151.192.0/18","119.160.200.0/21","119.161.128.0/17","119.162.0.0/15","119.164.0.0/14","119.176.0.0/12","119.232.0.0/15","119.235.128.0/18","119.248.0.0/14","119.252.96.0/21","119.252.240.0/20","119.253.0.0/16","119.254.0.0/15","120.0.0.0/12","120.24.0.0/14","120.30.0.0/16","120.31.0.0/16","120.32.0.0/13","120.40.0.0/14","120.44.0.0/14","120.48.0.0/15","120.52.0.0/14","120.64.0.0/14","120.68.0.0/14","120.72.32.0/19","120.72.128.0/17","120.76.0.0/14","120.80.0.0/13","120.88.8.0/21","120.90.0.0/15","120.92.0.0/16","120.94.0.0/16","120.95.0.0/16","120.128.0.0/14","120.132.0.0/17","120.132.128.0/17","120.133.0.0/16","120.134.0.0/15","120.136.128.0/18","120.137.0.0/17","120.143.128.0/19","120.192.0.0/10","121.0.8.0/21","121.0.16.0/20","121.4.0.0/15","121.8.0.0/13","121.16.0.0/13","121.24.0.0/14","121.28.0.0/15","121.30.0.0/16","121.31.0.0/16","121.32.0.0/14","121.36.0.0/16","121.37.0.0/16","121.38.0.0/15","121.40.0.0/14","121.46.0.0/18","121.46.128.0/17","121.47.0.0/16","121.48.0.0/15","121.50.8.0/21","121.51.0.0/16","121.52.160.0/19","121.52.208.0/20","121.52.224.0/19","121.54.176.0/21","121.55.0.0/18","121.56.0.0/15","121.58.0.0/17","121.58.136.0/21","121.58.144.0/20","121.58.160.0/21","121.59.0.0/16","121.60.0.0/14","121.68.0.0/14","121.76.0.0/15","121.79.128.0/18","121.89.0.0/16","121.100.128.0/17","121.101.0.0/18","121.101.208.0/20","121.192.0.0/16","121.193.0.0/16","121.194.0.0/15","121.196.0.0/14","121.200.192.0/21","121.201.0.0/16","121.204.0.0/14","121.224.0.0/12","121.248.0.0/14","121.255.0.0/16","122.0.64.0/18","122.0.128.0/17","122.4.0.0/14","122.8.0.0/16","122.9.0.0/16","122.10.0.0/17","122.10.128.0/17","122.11.0.0/16","122.12.0.0/16","122.13.0.0/16","122.14.0.0/16","122.15.0.0/16","122.48.0.0/16","122.49.0.0/18","122.51.0.0/16","122.64.0.0/11","122.96.0.0/15","122.102.0.0/20","122.102.64.0/20","122.102.80.0/20","122.112.0.0/14","122.119.0.0/16","122.128.120.0/21","122.136.0.0/13","122.144.128.0/17","122.152.192.0/18","122.156.0.0/14","122.188.0.0/14","122.192.0.0/14","122.198.0.0/16","122.200.64.0/18","122.201.48.0/20","122.204.0.0/14","122.224.0.0/12","122.240.0.0/13","122.248.24.0/21","122.248.48.0/20","122.255.64.0/21","123.0.128.0/18","123.4.0.0/14","123.8.0.0/13","123.49.128.0/17","123.50.160.0/19","123.52.0.0/14","123.56.0.0/15","123.58.0.0/16","123.59.0.0/16","123.60.0.0/15","123.62.0.0/16","123.64.0.0/11","123.96.0.0/15","123.98.0.0/17","123.99.128.0/17","123.100.0.0/19","123.101.0.0/16","123.103.0.0/17","123.108.128.0/20","123.108.208.0/20","123.112.0.0/12","123.128.0.0/13","123.136.80.0/20","123.137.0.0/16","123.138.0.0/15","123.144.0.0/14","123.148.0.0/16","123.149.0.0/16","123.150.0.0/15","123.152.0.0/13","123.160.0.0/14","123.164.0.0/14","123.168.0.0/14","123.172.0.0/15","123.174.0.0/15","123.176.60.0/22","123.176.80.0/20","123.177.0.0/16","123.178.0.0/15","123.180.0.0/14","123.184.0.0/14","123.188.0.0/14","123.196.0.0/15","123.199.128.0/17","123.206.0.0/15","123.232.0.0/14","123.242.0.0/17","123.244.0.0/14","123.249.0.0/16","123.253.0.0/16","124.6.64.0/18","124.14.0.0/15","124.16.0.0/15","124.20.0.0/16","124.21.0.0/20","124.21.16.0/20","124.21.32.0/19","124.21.64.0/18","124.21.128.0/17","124.22.0.0/15","124.28.192.0/18","124.29.0.0/17","124.31.0.0/16","124.40.112.0/20","124.40.128.0/18","124.40.192.0/19","124.42.0.0/17","124.42.128.0/17","124.47.0.0/18","124.64.0.0/15","124.66.0.0/17","124.67.0.0/16","124.68.0.0/14","124.72.0.0/16","124.73.0.0/16","124.74.0.0/15","124.76.0.0/14","124.88.0.0/16","124.89.0.0/17","124.89.128.0/17","124.90.0.0/15","124.92.0.0/14","124.108.8.0/21","124.108.40.0/21","124.109.96.0/21","124.112.0.0/15","124.114.0.0/15","124.116.0.0/16","124.117.0.0/16","124.118.0.0/15","124.126.0.0/15","124.128.0.0/13","124.147.128.0/17","124.151.0.0/16","124.152.0.0/16","124.156.0.0/16","124.160.0.0/16","124.161.0.0/16","124.162.0.0/16","124.163.0.0/16","124.164.0.0/14","124.172.0.0/15","124.174.0.0/15","124.192.0.0/15","124.196.0.0/16","124.200.0.0/13","124.220.0.0/14","124.224.0.0/16","124.225.0.0/16","124.226.0.0/15","124.228.0.0/14","124.232.0.0/15","124.234.0.0/15","124.236.0.0/14","124.240.0.0/17","124.240.128.0/18","124.242.0.0/16","124.243.192.0/18","124.248.0.0/17","124.249.0.0/16","124.250.0.0/15","124.254.0.0/18","125.31.192.0/18","125.32.0.0/16","125.33.0.0/16","125.34.0.0/16","125.35.0.0/17","125.35.128.0/17","125.36.0.0/14","125.40.0.0/13","125.58.128.0/17","125.61.128.0/17","125.62.0.0/18","125.64.0.0/13","125.72.0.0/16","125.73.0.0/16","125.74.0.0/15","125.76.0.0/17","125.76.128.0/17","125.77.0.0/16","125.78.0.0/15","125.80.0.0/13","125.88.0.0/13","125.96.0.0/15","125.98.0.0/16","125.104.0.0/13","125.112.0.0/12","125.169.0.0/16","125.171.0.0/16","125.208.0.0/18","125.210.0.0/16","125.211.0.0/16","125.213.0.0/17","125.214.96.0/19","125.215.0.0/18","125.216.0.0/15","125.218.0.0/16","125.219.0.0/16","125.220.0.0/15","125.222.0.0/15","125.254.128.0/18","125.254.192.0/18","134.196.0.0/16","139.9.0.0/16","139.129.0.0/16","139.148.0.0/16","139.155.0.0/16","139.159.0.0/16","139.170.0.0/16","139.176.0.0/16","139.183.0.0/16","139.186.0.0/16","139.189.0.0/16","139.196.0.0/14","139.200.0.0/13","139.208.0.0/13","139.220.0.0/15","139.224.0.0/16","139.226.0.0/15","140.75.0.0/16","140.143.0.0/16","140.205.0.0/16","140.206.0.0/15","140.210.0.0/16","140.224.0.0/16","140.237.0.0/16","140.240.0.0/16","140.243.0.0/16","140.246.0.0/16","140.249.0.0/16","140.250.0.0/16","140.255.0.0/16","144.0.0.0/16","144.7.0.0/16","144.12.0.0/16","144.52.0.0/16","144.123.0.0/16","144.255.0.0/16","150.0.0.0/16","150.115.0.0/16","150.121.0.0/16","150.122.0.0/16","150.138.0.0/15","150.223.0.0/16","150.255.0.0/16","153.0.0.0/16","153.3.0.0/16","153.34.0.0/15","153.36.0.0/15","153.99.0.0/16","153.101.0.0/16","153.118.0.0/15","157.0.0.0/16","157.18.0.0/16","157.61.0.0/16","157.122.0.0/16","157.148.0.0/16","157.156.0.0/16","157.255.0.0/16","159.226.0.0/16","161.207.0.0/16","162.105.0.0/16","163.0.0.0/16","163.125.0.0/16","163.142.0.0/16","163.177.0.0/16","163.179.0.0/16","163.204.0.0/16","166.111.0.0/16","167.139.0.0/16","168.160.0.0/16","171.8.0.0/13","171.34.0.0/15","171.36.0.0/14","171.40.0.0/13","171.80.0.0/14","171.84.0.0/14","171.88.0.0/13","171.104.0.0/13","171.112.0.0/14","171.116.0.0/14","171.120.0.0/13","171.208.0.0/12","175.0.0.0/12","175.16.0.0/13","175.24.0.0/14","175.30.0.0/15","175.42.0.0/15","175.44.0.0/16","175.46.0.0/15","175.48.0.0/12","175.64.0.0/11","175.102.0.0/16","175.106.128.0/17","175.146.0.0/15","175.148.0.0/14","175.152.0.0/14","175.160.0.0/12","175.178.0.0/16","175.184.128.0/18","175.185.0.0/16","175.186.0.0/15","175.188.0.0/14","180.76.0.0/16","180.77.0.0/16","180.78.0.0/15","180.84.0.0/15","180.86.0.0/16","180.88.0.0/14","180.94.56.0/21","180.94.96.0/20","180.95.128.0/17","180.96.0.0/11","180.129.128.0/17","180.130.0.0/16","180.136.0.0/13","180.148.16.0/21","180.148.152.0/21","180.148.216.0/21","180.148.224.0/19","180.149.128.0/19","180.150.160.0/19","180.152.0.0/13","180.160.0.0/12","180.178.192.0/18","180.184.0.0/14","180.188.0.0/17","180.189.148.0/22","180.200.252.0/22","180.201.0.0/16","180.202.0.0/15","180.208.0.0/15","180.210.224.0/19","180.212.0.0/15","180.222.224.0/19","180.223.0.0/16","180.233.0.0/18","180.233.64.0/19","180.235.64.0/19","182.16.192.0/19","182.18.0.0/17","182.23.184.0/21","182.23.200.0/21","182.32.0.0/12","182.48.96.0/19","182.49.0.0/16","182.50.0.0/20","182.50.112.0/20","182.51.0.0/16","182.54.0.0/17","182.61.0.0/16","182.80.0.0/14","182.84.0.0/14","182.88.0.0/14","182.92.0.0/16","182.96.0.0/12","182.112.0.0/12","182.128.0.0/12","182.144.0.0/13","182.157.0.0/16","182.160.64.0/19","182.174.0.0/15","182.200.0.0/13","182.236.128.0/17","182.238.0.0/16","182.239.0.0/19","182.240.0.0/13","182.254.0.0/16","183.0.0.0/10","183.64.0.0/13","183.78.180.0/22","183.81.180.0/22","183.84.0.0/15","183.91.128.0/22","183.91.136.0/21","183.91.144.0/20","183.92.0.0/14","183.128.0.0/11","183.160.0.0/13","183.168.0.0/15","183.170.0.0/16","183.172.0.0/14","183.182.0.0/19","183.184.0.0/13","183.192.0.0/10","192.124.154.0/24","192.188.170.0/24","202.0.100.0/23","202.0.122.0/23","202.0.176.0/22","202.3.128.0/23","202.4.128.0/19","202.4.252.0/22","202.6.6.0/23","202.6.66.0/23","202.6.72.0/23","202.6.87.0/24","202.6.88.0/23","202.6.92.0/23","202.6.103.0/24","202.6.108.0/24","202.6.110.0/23","202.6.114.0/24","202.6.176.0/20","202.8.0.0/24","202.8.2.0/23","202.8.4.0/23","202.8.12.0/24","202.8.24.0/24","202.8.77.0/24","202.8.128.0/19","202.8.192.0/20","202.9.32.0/24","202.9.34.0/23","202.9.48.0/23","202.9.51.0/24","202.9.52.0/23","202.9.54.0/24","202.9.57.0/24","202.9.58.0/23","202.10.64.0/20","202.12.1.0/24","202.12.2.0/24","202.12.17.0/24","202.12.18.0/24","202.12.19.0/24","202.12.72.0/24","202.12.84.0/23","202.12.96.0/24","202.12.98.0/23","202.12.106.0/24","202.12.111.0/24","202.12.116.0/24","202.14.64.0/23","202.14.69.0/24","202.14.73.0/24","202.14.74.0/23","202.14.76.0/24","202.14.78.0/23","202.14.88.0/24","202.14.97.0/24","202.14.104.0/23","202.14.108.0/23","202.14.111.0/24","202.14.114.0/23","202.14.118.0/23","202.14.124.0/23","202.14.127.0/24","202.14.129.0/24","202.14.135.0/24","202.14.136.0/24","202.14.149.0/24","202.14.151.0/24","202.14.157.0/24","202.14.158.0/23","202.14.169.0/24","202.14.170.0/23","202.14.176.0/24","202.14.184.0/23","202.14.208.0/23","202.14.213.0/24","202.14.219.0/24","202.14.220.0/24","202.14.222.0/23","202.14.225.0/24","202.14.226.0/23","202.14.231.0/24","202.14.235.0/24","202.14.236.0/23","202.14.238.0/24","202.14.239.0/24","202.14.246.0/24","202.14.251.0/24","202.20.66.0/24","202.20.79.0/24","202.20.87.0/24","202.20.88.0/23","202.20.90.0/24","202.20.94.0/23","202.20.114.0/24","202.20.117.0/24","202.20.120.0/24","202.20.125.0/24","202.20.127.0/24","202.21.131.0/24","202.21.132.0/24","202.21.141.0/24","202.21.142.0/24","202.21.147.0/24","202.21.148.0/24","202.21.150.0/23","202.21.152.0/23","202.21.154.0/24","202.21.156.0/24","202.22.248.0/22","202.22.252.0/22","202.27.136.0/23","202.38.0.0/23","202.38.2.0/23","202.38.8.0/21","202.38.48.0/20","202.38.64.0/19","202.38.96.0/19","202.38.128.0/23","202.38.130.0/23","202.38.132.0/23","202.38.134.0/24","202.38.135.0/24","202.38.136.0/23","202.38.138.0/24","202.38.140.0/23","202.38.142.0/23","202.38.146.0/23","202.38.149.0/24","202.38.150.0/23","202.38.152.0/23","202.38.154.0/23","202.38.156.0/24","202.38.158.0/23","202.38.160.0/23","202.38.164.0/22","202.38.168.0/23","202.38.170.0/24","202.38.171.0/24","202.38.176.0/23","202.38.184.0/21","202.38.192.0/18","202.40.4.0/23","202.40.7.0/24","202.40.15.0/24","202.40.135.0/24","202.40.136.0/24","202.40.140.0/24","202.40.143.0/24","202.40.144.0/23","202.40.150.0/24","202.40.155.0/24","202.40.156.0/24","202.40.158.0/23","202.40.162.0/24","202.41.8.0/23","202.41.11.0/24","202.41.12.0/23","202.41.128.0/24","202.41.130.0/23","202.41.152.0/21","202.41.192.0/24","202.41.240.0/20","202.43.76.0/22","202.43.144.0/20","202.44.16.0/20","202.44.67.0/24","202.44.74.0/24","202.44.129.0/24","202.44.132.0/23","202.44.146.0/23","202.45.0.0/23","202.45.2.0/24","202.45.15.0/24","202.45.16.0/20","202.46.16.0/23","202.46.18.0/24","202.46.20.0/23","202.46.32.0/19","202.46.128.0/24","202.46.224.0/20","202.47.82.0/23","202.47.126.0/24","202.47.128.0/24","202.47.130.0/23","202.57.240.0/20","202.58.0.0/24","202.59.0.0/24","202.59.212.0/22","202.59.232.0/23","202.59.236.0/24","202.60.48.0/21","202.60.96.0/21","202.60.112.0/20","202.60.132.0/22","202.60.136.0/21","202.60.144.0/20","202.62.112.0/22","202.62.248.0/22","202.62.252.0/24","202.62.255.0/24","202.63.81.0/24","202.63.82.0/23","202.63.84.0/22","202.63.88.0/21","202.63.160.0/19","202.63.248.0/22","202.65.0.0/21","202.65.8.0/23","202.67.0.0/22","202.69.4.0/22","202.69.16.0/20","202.70.0.0/19","202.70.96.0/20","202.70.192.0/20","202.72.40.0/21","202.72.80.0/20","202.73.128.0/22","202.74.8.0/21","202.74.80.0/20","202.74.254.0/23","202.75.208.0/20","202.75.252.0/22","202.76.252.0/22","202.77.80.0/21","202.77.92.0/22","202.78.8.0/21","202.79.224.0/21","202.79.248.0/22","202.80.192.0/21","202.80.200.0/21","202.81.0.0/22","202.83.252.0/22","202.84.4.0/22","202.84.8.0/21","202.84.24.0/21","202.85.208.0/20","202.86.249.0/24","202.86.252.0/22","202.87.80.0/20","202.89.8.0/21","202.90.0.0/22","202.90.112.0/20","202.90.196.0/24","202.90.224.0/20","202.91.0.0/22","202.91.96.0/20","202.91.128.0/22","202.91.176.0/20","202.91.224.0/19","202.92.0.0/22","202.92.8.0/21","202.92.48.0/20","202.92.252.0/22","202.93.0.0/22","202.93.252.0/22","202.94.92.0/22","202.95.0.0/22","202.95.4.0/22","202.95.8.0/21","202.95.16.0/20","202.95.240.0/21","202.95.252.0/22","202.96.0.0/18","202.96.64.0/21","202.96.72.0/21","202.96.80.0/20","202.96.96.0/21","202.96.104.0/21","202.96.112.0/20","202.96.128.0/21","202.96.136.0/21","202.96.144.0/20","202.96.160.0/21","202.96.168.0/21","202.96.176.0/20","202.96.192.0/21","202.96.200.0/21","202.96.208.0/20","202.96.224.0/21","202.96.232.0/21","202.96.240.0/20","202.97.0.0/21","202.97.8.0/21","202.97.16.0/20","202.97.32.0/19","202.97.64.0/19","202.97.96.0/20","202.97.112.0/20","202.97.128.0/18","202.97.192.0/19","202.97.224.0/21","202.97.232.0/21","202.97.240.0/20","202.98.0.0/21","202.98.8.0/21","202.98.16.0/20","202.98.32.0/21","202.98.40.0/21","202.98.48.0/20","202.98.64.0/19","202.98.96.0/21","202.98.104.0/21","202.98.112.0/20","202.98.128.0/19","202.98.160.0/21","202.98.168.0/21","202.98.176.0/20","202.98.192.0/21","202.98.200.0/21","202.98.208.0/20","202.98.224.0/21","202.98.232.0/21","202.98.240.0/20","202.99.0.0/18","202.99.64.0/19","202.99.96.0/21","202.99.104.0/21","202.99.112.0/20","202.99.128.0/19","202.99.160.0/21","202.99.168.0/21","202.99.176.0/20","202.99.192.0/21","202.99.200.0/21","202.99.208.0/20","202.99.224.0/21","202.99.232.0/21","202.99.240.0/20","202.100.0.0/21","202.100.8.0/21","202.100.16.0/20","202.100.32.0/19","202.100.64.0/21","202.100.72.0/21","202.100.80.0/20","202.100.96.0/21","202.100.104.0/21","202.100.112.0/20","202.100.128.0/21","202.100.136.0/21","202.100.144.0/20","202.100.160.0/21","202.100.168.0/21","202.100.176.0/20","202.100.192.0/21","202.100.200.0/21","202.100.208.0/20","202.100.224.0/19","202.101.0.0/18","202.101.64.0/19","202.101.96.0/19","202.101.128.0/18","202.101.192.0/19","202.101.224.0/21","202.101.232.0/21","202.101.240.0/20","202.102.0.0/19","202.102.32.0/19","202.102.64.0/18","202.102.128.0/21","202.102.136.0/21","202.102.144.0/20","202.102.160.0/19","202.102.192.0/21","202.102.200.0/21","202.102.208.0/20","202.102.224.0/21","202.102.232.0/21","202.102.240.0/20","202.103.0.0/21","202.103.8.0/21","202.103.16.0/20","202.103.32.0/19","202.103.64.0/19","202.103.96.0/21","202.103.104.0/21","202.103.112.0/20","202.103.128.0/18","202.103.192.0/19","202.103.224.0/21","202.103.232.0/21","202.103.240.0/20","202.104.0.0/15","202.106.0.0/16","202.107.0.0/17","202.107.128.0/17","202.108.0.0/16","202.109.0.0/16","202.110.0.0/18","202.110.64.0/18","202.110.128.0/18","202.110.192.0/18","202.111.0.0/17","202.111.128.0/19","202.111.160.0/19","202.111.192.0/18","202.112.0.0/16","202.113.0.0/20","202.113.16.0/20","202.113.32.0/19","202.113.64.0/18","202.113.128.0/18","202.113.192.0/19","202.113.224.0/20","202.113.240.0/20","202.114.0.0/19","202.114.32.0/19","202.114.64.0/18","202.114.128.0/17","202.115.0.0/19","202.115.32.0/19","202.115.64.0/18","202.115.128.0/17","202.116.0.0/19","202.116.32.0/20","202.116.48.0/20","202.116.64.0/19","202.116.96.0/19","202.116.128.0/17","202.117.0.0/18","202.117.64.0/18","202.117.128.0/17","202.118.0.0/19","202.118.32.0/19","202.118.64.0/18","202.118.128.0/17","202.119.0.0/19","202.119.32.0/19","202.119.64.0/20","202.119.80.0/20","202.119.96.0/19","202.119.128.0/17","202.120.0.0/18","202.120.64.0/18","202.120.128.0/17","202.121.0.0/16","202.122.0.0/21","202.122.32.0/21","202.122.64.0/19","202.122.112.0/21","202.122.120.0/21","202.122.128.0/24","202.122.132.0/24","202.123.96.0/20","202.124.16.0/21","202.124.24.0/22","202.125.112.0/20","202.125.176.0/20","202.127.0.0/23","202.127.2.0/24","202.127.3.0/24","202.127.4.0/24","202.127.5.0/24","202.127.6.0/23","202.127.12.0/22","202.127.16.0/20","202.127.40.0/21","202.127.48.0/20","202.127.112.0/20","202.127.128.0/20","202.127.144.0/20","202.127.160.0/21","202.127.192.0/23","202.127.194.0/23","202.127.196.0/22","202.127.200.0/21","202.127.208.0/24","202.127.209.0/24","202.127.212.0/22","202.127.216.0/21","202.127.224.0/19","202.130.0.0/19","202.130.224.0/19","202.131.16.0/21","202.131.48.0/20","202.131.208.0/20","202.133.32.0/20","202.134.58.0/24","202.134.128.0/20","202.136.48.0/20","202.136.208.0/20","202.136.224.0/20","202.137.231.0/24","202.141.160.0/19","202.142.16.0/20","202.143.4.0/22","202.143.16.0/20","202.143.32.0/20","202.143.56.0/21","202.146.160.0/20","202.146.188.0/22","202.146.196.0/22","202.146.200.0/21","202.147.144.0/20","202.148.32.0/20","202.148.64.0/19","202.148.96.0/19","202.149.32.0/19","202.149.160.0/19","202.149.224.0/19","202.150.16.0/20","202.150.32.0/20","202.150.56.0/22","202.150.192.0/20","202.150.224.0/19","202.151.0.0/22","202.151.128.0/19","202.152.176.0/20","202.153.0.0/22","202.153.48.0/20","202.157.192.0/19","202.158.160.0/19","202.160.176.0/20","202.162.67.0/24","202.162.75.0/24","202.164.0.0/20","202.164.25.0/24","202.164.96.0/19","202.165.96.0/20","202.165.176.0/20","202.165.208.0/20","202.165.239.0/24","202.165.240.0/23","202.165.243.0/24","202.165.245.0/24","202.165.251.0/24","202.165.252.0/22","202.166.224.0/19","202.168.160.0/20","202.168.176.0/20","202.170.128.0/19","202.170.216.0/21","202.170.224.0/19","202.171.216.0/21","202.171.235.0/24","202.172.0.0/22","202.173.0.0/22","202.173.8.0/21","202.173.224.0/19","202.174.64.0/20","202.176.224.0/19","202.179.240.0/20","202.180.128.0/19","202.180.208.0/21","202.181.112.0/20","202.182.32.0/20","202.182.192.0/19","202.189.0.0/18","202.189.80.0/20","202.189.184.0/21","202.191.0.0/24","202.191.68.0/22","202.191.72.0/21","202.191.80.0/20","202.192.0.0/13","202.200.0.0/14","202.204.0.0/14","203.0.4.0/22","203.0.10.0/23","203.0.18.0/24","203.0.24.0/24","203.0.42.0/23","203.0.45.0/24","203.0.46.0/23","203.0.81.0/24","203.0.82.0/23","203.0.90.0/23","203.0.96.0/23","203.0.104.0/21","203.0.114.0/23","203.0.122.0/24","203.0.128.0/24","203.0.130.0/23","203.0.132.0/22","203.0.137.0/24","203.0.142.0/24","203.0.144.0/24","203.0.146.0/24","203.0.148.0/24","203.0.150.0/23","203.0.152.0/24","203.0.177.0/24","203.0.224.0/24","203.1.4.0/22","203.1.18.0/24","203.1.26.0/23","203.1.65.0/24","203.1.66.0/23","203.1.70.0/23","203.1.76.0/23","203.1.90.0/24","203.1.97.0/24","203.1.98.0/23","203.1.100.0/22","203.1.108.0/24","203.1.253.0/24","203.1.254.0/24","203.2.64.0/21","203.2.73.0/24","203.2.112.0/21","203.2.126.0/23","203.2.140.0/24","203.2.150.0/24","203.2.152.0/22","203.2.156.0/23","203.2.160.0/21","203.2.180.0/23","203.2.196.0/23","203.2.209.0/24","203.2.214.0/23","203.2.226.0/23","203.2.229.0/24","203.2.236.0/23","203.3.68.0/24","203.3.72.0/23","203.3.75.0/24","203.3.80.0/21","203.3.96.0/22","203.3.105.0/24","203.3.112.0/21","203.3.120.0/24","203.3.123.0/24","203.3.135.0/24","203.3.139.0/24","203.3.143.0/24","203.4.132.0/23","203.4.134.0/24","203.4.151.0/24","203.4.152.0/22","203.4.174.0/23","203.4.180.0/24","203.4.186.0/24","203.4.205.0/24","203.4.208.0/22","203.4.227.0/24","203.4.230.0/23","203.5.4.0/23","203.5.7.0/24","203.5.8.0/23","203.5.11.0/24","203.5.21.0/24","203.5.22.0/24","203.5.44.0/24","203.5.46.0/23","203.5.52.0/22","203.5.56.0/23","203.5.60.0/23","203.5.114.0/23","203.5.118.0/24","203.5.120.0/24","203.5.172.0/24","203.5.180.0/23","203.5.182.0/24","203.5.185.0/24","203.5.186.0/24","203.5.188.0/23","203.5.190.0/24","203.5.195.0/24","203.5.214.0/23","203.5.218.0/23","203.6.131.0/24","203.6.136.0/24","203.6.138.0/23","203.6.142.0/24","203.6.150.0/23","203.6.157.0/24","203.6.159.0/24","203.6.224.0/20","203.6.248.0/23","203.7.129.0/24","203.7.138.0/23","203.7.147.0/24","203.7.150.0/23","203.7.158.0/24","203.7.192.0/23","203.7.200.0/24","203.8.0.0/24","203.8.8.0/24","203.8.23.0/24","203.8.24.0/21","203.8.70.0/24","203.8.82.0/24","203.8.86.0/23","203.8.91.0/24","203.8.110.0/23","203.8.115.0/24","203.8.166.0/23","203.8.169.0/24","203.8.173.0/24","203.8.184.0/24","203.8.186.0/23","203.8.190.0/23","203.8.192.0/24","203.8.197.0/24","203.8.198.0/23","203.8.203.0/24","203.8.209.0/24","203.8.210.0/23","203.8.212.0/22","203.8.217.0/24","203.8.220.0/24","203.9.32.0/24","203.9.36.0/23","203.9.57.0/24","203.9.63.0/24","203.9.65.0/24","203.9.70.0/23","203.9.72.0/24","203.9.75.0/24","203.9.76.0/23","203.9.96.0/22","203.9.100.0/23","203.9.108.0/24","203.9.158.0/24","203.10.34.0/24","203.10.56.0/24","203.10.74.0/23","203.10.84.0/22","203.10.88.0/24","203.10.95.0/24","203.10.125.0/24","203.11.70.0/24","203.11.76.0/22","203.11.82.0/24","203.11.84.0/22","203.11.100.0/22","203.11.109.0/24","203.11.117.0/24","203.11.122.0/24","203.11.126.0/24","203.11.136.0/22","203.11.141.0/24","203.11.142.0/23","203.11.180.0/22","203.11.208.0/22","203.12.16.0/24","203.12.19.0/24","203.12.24.0/24","203.12.57.0/24","203.12.65.0/24","203.12.66.0/24","203.12.70.0/23","203.12.87.0/24","203.12.88.0/21","203.12.100.0/23","203.12.103.0/24","203.12.114.0/24","203.12.118.0/24","203.12.130.0/24","203.12.137.0/24","203.12.196.0/22","203.12.200.0/21","203.12.211.0/24","203.12.219.0/24","203.12.226.0/24","203.12.240.0/22","203.13.18.0/24","203.13.24.0/24","203.13.44.0/23","203.13.80.0/21","203.13.88.0/23","203.13.92.0/22","203.13.173.0/24","203.13.224.0/23","203.13.227.0/24","203.13.233.0/24","203.14.24.0/22","203.14.33.0/24","203.14.56.0/24","203.14.61.0/24","203.14.62.0/24","203.14.104.0/24","203.14.114.0/23","203.14.118.0/24","203.14.162.0/24","203.14.184.0/21","203.14.192.0/24","203.14.194.0/23","203.14.214.0/24","203.14.231.0/24","203.14.246.0/24","203.15.0.0/20","203.15.20.0/23","203.15.22.0/24","203.15.87.0/24","203.15.88.0/23","203.15.105.0/24","203.15.112.0/21","203.15.130.0/23","203.15.149.0/24","203.15.151.0/24","203.15.156.0/22","203.15.174.0/24","203.15.227.0/24","203.15.232.0/21","203.15.240.0/23","203.15.246.0/24","203.16.10.0/24","203.16.12.0/23","203.16.16.0/21","203.16.27.0/24","203.16.38.0/24","203.16.49.0/24","203.16.50.0/23","203.16.58.0/24","203.16.133.0/24","203.16.161.0/24","203.16.162.0/24","203.16.186.0/23","203.16.228.0/24","203.16.238.0/24","203.16.240.0/24","203.16.245.0/24","203.17.2.0/24","203.17.18.0/24","203.17.28.0/24","203.17.39.0/24","203.17.56.0/24","203.17.74.0/23","203.17.88.0/23","203.17.136.0/24","203.17.164.0/24","203.17.187.0/24","203.17.190.0/23","203.17.231.0/24","203.17.233.0/24","203.17.248.0/24","203.17.255.0/24","203.18.2.0/23","203.18.4.0/24","203.18.7.0/24","203.18.31.0/24","203.18.37.0/24","203.18.48.0/23","203.18.50.0/24","203.18.52.0/24","203.18.72.0/22","203.18.80.0/23","203.18.87.0/24","203.18.100.0/23","203.18.105.0/24","203.18.107.0/24","203.18.110.0/24","203.18.129.0/24","203.18.131.0/24","203.18.132.0/23","203.18.144.0/24","203.18.153.0/24","203.18.199.0/24","203.18.208.0/24","203.18.211.0/24","203.18.215.0/24","203.19.18.0/24","203.19.24.0/24","203.19.30.0/24","203.19.32.0/21","203.19.41.0/24","203.19.44.0/23","203.19.46.0/24","203.19.58.0/24","203.19.60.0/23","203.19.64.0/24","203.19.68.0/24","203.19.72.0/24","203.19.101.0/24","203.19.111.0/24","203.19.131.0/24","203.19.133.0/24","203.19.144.0/24","203.19.149.0/24","203.19.156.0/24","203.19.176.0/24","203.19.178.0/23","203.19.208.0/24","203.19.228.0/22","203.19.233.0/24","203.19.242.0/24","203.19.248.0/23","203.19.255.0/24","203.20.17.0/24","203.20.40.0/23","203.20.48.0/24","203.20.61.0/24","203.20.65.0/24","203.20.84.0/23","203.20.89.0/24","203.20.106.0/23","203.20.115.0/24","203.20.117.0/24","203.20.118.0/23","203.20.122.0/24","203.20.126.0/23","203.20.135.0/24","203.20.136.0/21","203.20.150.0/24","203.20.230.0/24","203.20.232.0/24","203.20.236.0/24","203.21.0.0/23","203.21.2.0/24","203.21.8.0/24","203.21.10.0/24","203.21.18.0/24","203.21.33.0/24","203.21.34.0/24","203.21.41.0/24","203.21.44.0/24","203.21.68.0/24","203.21.82.0/24","203.21.96.0/22","203.21.124.0/24","203.21.136.0/23","203.21.145.0/24","203.21.206.0/24","203.22.24.0/24","203.22.28.0/23","203.22.31.0/24","203.22.68.0/24","203.22.76.0/24","203.22.78.0/24","203.22.84.0/24","203.22.87.0/24","203.22.92.0/22","203.22.99.0/24","203.22.106.0/24","203.22.122.0/23","203.22.131.0/24","203.22.163.0/24","203.22.166.0/24","203.22.170.0/24","203.22.176.0/21","203.22.194.0/24","203.22.242.0/23","203.22.245.0/24","203.22.246.0/24","203.22.252.0/23","203.23.0.0/24","203.23.47.0/24","203.23.61.0/24","203.23.62.0/23","203.23.73.0/24","203.23.85.0/24","203.23.92.0/22","203.23.98.0/24","203.23.107.0/24","203.23.112.0/24","203.23.130.0/24","203.23.140.0/23","203.23.172.0/24","203.23.182.0/24","203.23.186.0/23","203.23.192.0/24","203.23.197.0/24","203.23.198.0/24","203.23.204.0/22","203.23.224.0/24","203.23.226.0/23","203.23.228.0/22","203.23.249.0/24","203.23.251.0/24","203.24.13.0/24","203.24.18.0/24","203.24.27.0/24","203.24.43.0/24","203.24.56.0/24","203.24.58.0/24","203.24.67.0/24","203.24.74.0/24","203.24.79.0/24","203.24.80.0/23","203.24.84.0/23","203.24.86.0/24","203.24.90.0/24","203.24.111.0/24","203.24.112.0/24","203.24.116.0/24","203.24.122.0/23","203.24.145.0/24","203.24.152.0/23","203.24.157.0/24","203.24.161.0/24","203.24.167.0/24","203.24.186.0/23","203.24.199.0/24","203.24.202.0/24","203.24.212.0/23","203.24.217.0/24","203.24.219.0/24","203.24.244.0/24","203.25.19.0/24","203.25.20.0/23","203.25.46.0/24","203.25.48.0/21","203.25.64.0/23","203.25.91.0/24","203.25.99.0/24","203.25.100.0/24","203.25.106.0/24","203.25.131.0/24","203.25.135.0/24","203.25.138.0/24","203.25.147.0/24","203.25.153.0/24","203.25.154.0/23","203.25.164.0/24","203.25.166.0/24","203.25.174.0/23","203.25.180.0/24","203.25.182.0/24","203.25.191.0/24","203.25.199.0/24","203.25.200.0/24","203.25.202.0/23","203.25.208.0/20","203.25.229.0/24","203.25.235.0/24","203.25.236.0/24","203.25.242.0/24","203.26.12.0/24","203.26.34.0/24","203.26.49.0/24","203.26.50.0/24","203.26.55.0/24","203.26.56.0/23","203.26.60.0/24","203.26.65.0/24","203.26.68.0/24","203.26.76.0/24","203.26.80.0/24","203.26.84.0/24","203.26.97.0/24","203.26.102.0/23","203.26.115.0/24","203.26.116.0/24","203.26.129.0/24","203.26.143.0/24","203.26.144.0/24","203.26.148.0/23","203.26.154.0/24","203.26.158.0/23","203.26.170.0/24","203.26.173.0/24","203.26.176.0/24","203.26.185.0/24","203.26.202.0/23","203.26.210.0/24","203.26.214.0/24","203.26.222.0/24","203.26.224.0/24","203.26.228.0/24","203.26.232.0/24","203.27.0.0/24","203.27.10.0/24","203.27.15.0/24","203.27.16.0/24","203.27.20.0/24","203.27.22.0/23","203.27.40.0/24","203.27.45.0/24","203.27.53.0/24","203.27.65.0/24","203.27.66.0/24","203.27.81.0/24","203.27.88.0/24","203.27.102.0/24","203.27.109.0/24","203.27.117.0/24","203.27.121.0/24","203.27.122.0/23","203.27.125.0/24","203.27.200.0/24","203.27.202.0/24","203.27.233.0/24","203.27.241.0/24","203.27.250.0/24","203.28.10.0/24","203.28.12.0/24","203.28.33.0/24","203.28.34.0/23","203.28.43.0/24","203.28.44.0/24","203.28.54.0/24","203.28.56.0/24","203.28.73.0/24","203.28.74.0/24","203.28.76.0/24","203.28.86.0/24","203.28.88.0/24","203.28.112.0/24","203.28.131.0/24","203.28.136.0/24","203.28.140.0/24","203.28.145.0/24","203.28.165.0/24","203.28.169.0/24","203.28.170.0/24","203.28.178.0/23","203.28.185.0/24","203.28.187.0/24","203.28.196.0/24","203.28.226.0/23","203.28.239.0/24","203.29.2.0/24","203.29.8.0/23","203.29.13.0/24","203.29.14.0/24","203.29.28.0/24","203.29.46.0/24","203.29.57.0/24","203.29.61.0/24","203.29.63.0/24","203.29.69.0/24","203.29.73.0/24","203.29.81.0/24","203.29.90.0/24","203.29.95.0/24","203.29.100.0/24","203.29.103.0/24","203.29.112.0/24","203.29.120.0/22","203.29.182.0/23","203.29.187.0/24","203.29.189.0/24","203.29.190.0/24","203.29.205.0/24","203.29.210.0/24","203.29.217.0/24","203.29.227.0/24","203.29.231.0/24","203.29.233.0/24","203.29.234.0/24","203.29.248.0/24","203.29.254.0/23","203.30.16.0/23","203.30.25.0/24","203.30.27.0/24","203.30.29.0/24","203.30.66.0/24","203.30.81.0/24","203.30.87.0/24","203.30.111.0/24","203.30.121.0/24","203.30.123.0/24","203.30.152.0/24","203.30.156.0/24","203.30.162.0/24","203.30.173.0/24","203.30.175.0/24","203.30.187.0/24","203.30.194.0/24","203.30.217.0/24","203.30.220.0/24","203.30.222.0/24","203.30.232.0/23","203.30.235.0/24","203.30.240.0/23","203.30.246.0/24","203.30.250.0/23","203.31.45.0/24","203.31.46.0/24","203.31.49.0/24","203.31.51.0/24","203.31.54.0/23","203.31.69.0/24","203.31.72.0/24","203.31.80.0/24","203.31.85.0/24","203.31.97.0/24","203.31.105.0/24","203.31.106.0/24","203.31.108.0/23","203.31.124.0/24","203.31.162.0/24","203.31.174.0/24","203.31.177.0/24","203.31.181.0/24","203.31.187.0/24","203.31.189.0/24","203.31.204.0/24","203.31.220.0/24","203.31.222.0/23","203.31.225.0/24","203.31.229.0/24","203.31.248.0/23","203.31.253.0/24","203.32.20.0/24","203.32.48.0/23","203.32.56.0/24","203.32.60.0/24","203.32.62.0/24","203.32.68.0/23","203.32.76.0/24","203.32.81.0/24","203.32.84.0/23","203.32.95.0/24","203.32.102.0/24","203.32.105.0/24","203.32.130.0/24","203.32.133.0/24","203.32.140.0/24","203.32.152.0/24","203.32.186.0/23","203.32.192.0/24","203.32.196.0/24","203.32.203.0/24","203.32.204.0/23","203.32.212.0/24","203.33.4.0/24","203.33.7.0/24","203.33.8.0/21","203.33.21.0/24","203.33.26.0/24","203.33.32.0/24","203.33.63.0/24","203.33.64.0/24","203.33.67.0/24","203.33.68.0/24","203.33.73.0/24","203.33.79.0/24","203.33.100.0/24","203.33.122.0/24","203.33.129.0/24","203.33.131.0/24","203.33.145.0/24","203.33.156.0/24","203.33.158.0/23","203.33.174.0/24","203.33.185.0/24","203.33.200.0/24","203.33.202.0/23","203.33.204.0/24","203.33.206.0/23","203.33.214.0/23","203.33.224.0/23","203.33.226.0/24","203.33.233.0/24","203.33.243.0/24","203.33.250.0/24","203.34.4.0/24","203.34.21.0/24","203.34.27.0/24","203.34.39.0/24","203.34.48.0/23","203.34.54.0/24","203.34.56.0/23","203.34.67.0/24","203.34.69.0/24","203.34.76.0/24","203.34.92.0/24","203.34.106.0/24","203.34.113.0/24","203.34.147.0/24","203.34.150.0/24","203.34.152.0/23","203.34.161.0/24","203.34.162.0/24","203.34.187.0/24","203.34.192.0/21","203.34.204.0/22","203.34.232.0/24","203.34.240.0/24","203.34.242.0/24","203.34.245.0/24","203.34.251.0/24","203.55.2.0/23","203.55.4.0/24","203.55.10.0/24","203.55.13.0/24","203.55.22.0/24","203.55.30.0/24","203.55.93.0/24","203.55.101.0/24","203.55.109.0/24","203.55.110.0/24","203.55.116.0/23","203.55.119.0/24","203.55.128.0/23","203.55.146.0/23","203.55.192.0/24","203.55.196.0/24","203.55.218.0/23","203.55.221.0/24","203.55.224.0/24","203.56.1.0/24","203.56.4.0/24","203.56.12.0/24","203.56.24.0/24","203.56.38.0/24","203.56.40.0/24","203.56.46.0/24","203.56.48.0/21","203.56.68.0/23","203.56.82.0/23","203.56.84.0/23","203.56.95.0/24","203.56.110.0/24","203.56.121.0/24","203.56.161.0/24","203.56.169.0/24","203.56.172.0/23","203.56.175.0/24","203.56.183.0/24","203.56.185.0/24","203.56.187.0/24","203.56.192.0/24","203.56.198.0/24","203.56.201.0/24","203.56.208.0/23","203.56.210.0/24","203.56.214.0/24","203.56.216.0/24","203.56.227.0/24","203.56.228.0/24","203.56.232.0/24","203.56.240.0/24","203.56.252.0/24","203.56.254.0/24","203.57.5.0/24","203.57.6.0/24","203.57.12.0/23","203.57.28.0/24","203.57.39.0/24","203.57.46.0/24","203.57.58.0/24","203.57.61.0/24","203.57.66.0/24","203.57.69.0/24","203.57.70.0/23","203.57.73.0/24","203.57.90.0/24","203.57.101.0/24","203.57.109.0/24","203.57.123.0/24","203.57.157.0/24","203.57.200.0/24","203.57.202.0/24","203.57.206.0/24","203.57.222.0/24","203.57.224.0/20","203.57.246.0/23","203.57.249.0/24","203.57.253.0/24","203.57.254.0/23","203.62.2.0/24","203.62.131.0/24","203.62.139.0/24","203.62.161.0/24","203.62.197.0/24","203.62.228.0/22","203.62.234.0/24","203.62.246.0/24","203.76.160.0/22","203.76.168.0/22","203.77.180.0/22","203.78.48.0/20","203.79.0.0/20","203.79.32.0/20","203.80.4.0/23","203.80.32.0/20","203.80.57.0/24","203.80.132.0/22","203.80.136.0/21","203.80.144.0/20","203.81.0.0/21","203.81.16.0/20","203.82.0.0/23","203.82.16.0/21","203.83.0.0/22","203.83.56.0/21","203.83.224.0/20","203.86.0.0/19","203.86.32.0/19","203.86.64.0/20","203.86.80.0/20","203.86.96.0/19","203.86.254.0/23","203.88.32.0/19","203.88.192.0/19","203.89.0.0/22","203.89.8.0/21","203.89.136.0/22","203.90.0.0/22","203.90.8.0/22","203.90.128.0/19","203.90.160.0/19","203.90.192.0/19","203.91.32.0/19","203.91.96.0/20","203.91.120.0/21","203.92.0.0/22","203.92.160.0/19","203.93.0.0/22","203.93.4.0/22","203.93.8.0/24","203.93.9.0/24","203.93.10.0/23","203.93.12.0/22","203.93.16.0/20","203.93.32.0/19","203.93.64.0/18","203.93.128.0/21","203.93.136.0/22","203.93.140.0/24","203.93.141.0/24","203.93.142.0/23","203.93.144.0/20","203.93.160.0/19","203.93.192.0/18","203.94.0.0/22","203.94.4.0/22","203.94.8.0/21","203.94.16.0/20","203.95.0.0/21","203.95.96.0/20","203.95.112.0/20","203.95.128.0/18","203.95.224.0/19","203.99.8.0/21","203.99.16.0/20","203.99.80.0/20","203.100.32.0/20","203.100.48.0/21","203.100.63.0/24","203.100.80.0/20","203.100.96.0/19","203.100.192.0/20","203.104.32.0/20","203.105.96.0/19","203.105.128.0/19","203.107.0.0/17","203.110.160.0/19","203.110.208.0/20","203.110.232.0/23","203.110.234.0/24","203.114.244.0/22","203.118.192.0/19","203.118.241.0/24","203.118.248.0/22","203.119.24.0/21","203.119.32.0/22","203.119.80.0/22","203.119.85.0/24","203.119.113.0/24","203.119.114.0/23","203.119.116.0/22","203.119.120.0/21","203.119.128.0/17","203.128.32.0/19","203.128.96.0/19","203.128.224.0/21","203.129.8.0/21","203.130.32.0/19","203.132.32.0/19","203.134.240.0/21","203.135.96.0/20","203.135.112.0/20","203.135.160.0/20","203.142.224.0/19","203.144.96.0/19","203.145.0.0/19","203.148.0.0/18","203.148.64.0/20","203.148.80.0/22","203.148.86.0/23","203.149.92.0/22","203.152.64.0/19","203.152.128.0/19","203.153.0.0/22","203.156.192.0/18","203.158.16.0/21","203.160.104.0/21","203.160.129.0/24","203.160.192.0/19","203.161.0.0/22","203.161.180.0/24","203.161.192.0/19","203.166.160.0/19","203.168.0.0/19","203.170.58.0/23","203.171.0.0/22","203.171.224.0/20","203.174.4.0/24","203.174.7.0/24","203.174.96.0/19","203.175.128.0/19","203.175.192.0/18","203.176.0.0/18","203.176.64.0/19","203.176.168.0/21","203.184.80.0/20","203.187.160.0/19","203.189.0.0/23","203.189.6.0/23","203.189.112.0/22","203.189.192.0/19","203.190.96.0/20","203.190.249.0/24","203.191.0.0/23","203.191.16.0/20","203.191.64.0/18","203.191.144.0/21","203.191.152.0/21","203.192.0.0/19","203.193.224.0/19","203.194.120.0/21","203.195.64.0/19","203.195.112.0/21","203.195.128.0/17","203.196.0.0/21","203.196.8.0/21","203.202.236.0/22","203.205.64.0/19","203.205.128.0/17","203.207.64.0/18","203.207.128.0/17","203.208.0.0/20","203.208.16.0/22","203.208.32.0/19","203.209.224.0/19","203.212.0.0/20","203.212.80.0/20","203.215.232.0/21","203.222.192.0/20","203.223.0.0/20","203.223.16.0/21","210.2.0.0/20","210.2.16.0/20","210.5.0.0/19","210.5.56.0/21","210.5.128.0/20","210.5.144.0/20","210.12.0.0/18","210.12.64.0/18","210.12.128.0/18","210.12.192.0/18","210.13.0.0/18","210.13.64.0/18","210.13.128.0/17","210.14.64.0/19","210.14.112.0/20","210.14.128.0/19","210.14.160.0/19","210.14.192.0/19","210.14.224.0/19","210.15.0.0/19","210.15.32.0/19","210.15.64.0/19","210.15.96.0/19","210.15.128.0/18","210.16.128.0/18","210.21.0.0/17","210.21.128.0/17","210.22.0.0/16","210.23.32.0/19","210.25.0.0/16","210.26.0.0/15","210.28.0.0/14","210.32.0.0/14","210.36.0.0/14","210.40.0.0/13","210.48.136.0/21","210.51.0.0/16","210.52.0.0/18","210.52.64.0/18","210.52.128.0/17","210.53.0.0/17","210.53.128.0/17","210.56.192.0/19","210.72.0.0/17","210.72.128.0/19","210.72.160.0/19","210.72.192.0/18","210.73.0.0/19","210.73.32.0/19","210.73.64.0/18","210.73.128.0/17","210.74.0.0/19","210.74.32.0/19","210.74.64.0/19","210.74.96.0/19","210.74.128.0/19","210.74.160.0/19","210.74.192.0/18","210.75.0.0/16","210.76.0.0/19","210.76.32.0/19","210.76.64.0/18","210.76.128.0/17","210.77.0.0/16","210.78.0.0/19","210.78.32.0/19","210.78.64.0/18","210.78.128.0/19","210.78.160.0/19","210.78.192.0/18","210.79.64.0/18","210.79.224.0/19","210.82.0.0/15","210.87.128.0/20","210.87.144.0/20","210.87.160.0/19","210.185.192.0/18","210.192.96.0/19","211.64.0.0/14","211.68.0.0/15","211.70.0.0/15","211.80.0.0/16","211.81.0.0/16","211.82.0.0/16","211.83.0.0/16","211.84.0.0/15","211.86.0.0/15","211.88.0.0/16","211.89.0.0/16","211.90.0.0/15","211.92.0.0/15","211.94.0.0/15","211.96.0.0/15","211.98.0.0/16","211.99.0.0/18","211.99.64.0/19","211.99.96.0/19","211.99.128.0/17","211.100.0.0/16","211.101.0.0/18","211.101.64.0/18","211.101.128.0/17","211.102.0.0/16","211.103.0.0/17","211.103.128.0/17","211.136.0.0/14","211.140.0.0/15","211.142.0.0/17","211.142.128.0/17","211.143.0.0/16","211.144.0.0/15","211.146.0.0/16","211.147.0.0/16","211.148.0.0/14","211.152.0.0/15","211.154.0.0/16","211.155.0.0/18","211.155.64.0/19","211.155.96.0/19","211.155.128.0/17","211.156.0.0/14","211.160.0.0/14","211.164.0.0/14","218.0.0.0/16","218.1.0.0/16","218.2.0.0/15","218.4.0.0/15","218.6.0.0/16","218.7.0.0/16","218.8.0.0/15","218.10.0.0/16","218.11.0.0/16","218.12.0.0/16","218.13.0.0/16","218.14.0.0/15","218.16.0.0/14","218.20.0.0/16","218.21.0.0/17","218.21.128.0/17","218.22.0.0/15","218.24.0.0/15","218.26.0.0/16","218.27.0.0/16","218.28.0.0/15","218.30.0.0/15","218.56.0.0/14","218.60.0.0/15","218.62.0.0/17","218.62.128.0/17","218.63.0.0/16","218.64.0.0/15","218.66.0.0/16","218.67.0.0/17","218.67.128.0/17","218.68.0.0/15","218.70.0.0/15","218.72.0.0/14","218.76.0.0/15","218.78.0.0/15","218.80.0.0/14","218.84.0.0/14","218.88.0.0/13","218.96.0.0/15","218.98.0.0/17","218.98.128.0/18","218.98.192.0/19","218.98.224.0/19","218.99.0.0/16","218.100.88.0/21","218.100.96.0/19","218.100.128.0/17","218.104.0.0/17","218.104.128.0/19","218.104.160.0/19","218.104.192.0/21","218.104.200.0/21","218.104.208.0/20","218.104.224.0/19","218.105.0.0/16","218.106.0.0/15","218.108.0.0/16","218.109.0.0/16","218.185.192.0/19","218.185.240.0/21","218.192.0.0/16","218.193.0.0/16","218.194.0.0/16","218.195.0.0/16","218.196.0.0/14","218.200.0.0/14","218.204.0.0/15","218.206.0.0/15","218.240.0.0/14","218.244.0.0/15","218.246.0.0/15","218.249.0.0/16","219.72.0.0/16","219.82.0.0/16","219.83.128.0/17","219.128.0.0/12","219.144.0.0/14","219.148.0.0/16","219.149.0.0/17","219.149.128.0/18","219.149.192.0/18","219.150.0.0/19","219.150.32.0/19","219.150.64.0/19","219.150.96.0/20","219.150.112.0/20","219.150.128.0/17","219.151.0.0/19","219.151.32.0/19","219.151.64.0/18","219.151.128.0/17","219.152.0.0/15","219.154.0.0/15","219.156.0.0/15","219.158.0.0/17","219.158.128.0/17","219.159.0.0/18","219.159.64.0/18","219.159.128.0/17","219.216.0.0/15","219.218.0.0/15","219.220.0.0/16","219.221.0.0/16","219.222.0.0/15","219.224.0.0/15","219.226.0.0/16","219.227.0.0/16","219.228.0.0/15","219.230.0.0/15","219.232.0.0/14","219.236.0.0/15","219.238.0.0/15","219.242.0.0/15","219.244.0.0/14","220.101.192.0/18","220.112.0.0/14","220.152.128.0/17","220.154.0.0/15","220.160.0.0/11","220.192.0.0/15","220.194.0.0/15","220.196.0.0/14","220.200.0.0/13","220.231.0.0/18","220.231.128.0/17","220.232.64.0/18","220.234.0.0/16","220.242.0.0/15","220.247.136.0/21","220.248.0.0/14","220.252.0.0/16","221.0.0.0/15","221.2.0.0/16","221.3.0.0/17","221.3.128.0/17","221.4.0.0/16","221.5.0.0/17","221.5.128.0/17","221.6.0.0/16","221.7.0.0/19","221.7.32.0/19","221.7.64.0/19","221.7.96.0/19","221.7.128.0/17","221.8.0.0/15","221.10.0.0/16","221.11.0.0/17","221.11.128.0/18","221.11.192.0/19","221.11.224.0/19","221.12.0.0/17","221.12.128.0/18","221.13.0.0/18","221.13.64.0/19","221.13.96.0/19","221.13.128.0/17","221.14.0.0/15","221.122.0.0/15","221.128.128.0/17","221.129.0.0/16","221.130.0.0/15","221.133.224.0/19","221.136.0.0/16","221.137.0.0/16","221.172.0.0/14","221.176.0.0/13","221.192.0.0/15","221.194.0.0/16","221.195.0.0/16","221.196.0.0/15","221.198.0.0/16","221.199.0.0/19","221.199.32.0/20","221.199.48.0/20","221.199.64.0/18","221.199.128.0/18","221.199.192.0/20","221.199.224.0/19","221.200.0.0/14","221.204.0.0/15","221.206.0.0/16","221.207.0.0/18","221.207.64.0/18","221.207.128.0/17","221.208.0.0/14","221.212.0.0/16","221.213.0.0/16","221.214.0.0/15","221.216.0.0/13","221.224.0.0/13","221.232.0.0/14","221.236.0.0/15","221.238.0.0/16","221.239.0.0/17","221.239.128.0/17","222.16.0.0/15","222.18.0.0/15","222.20.0.0/15","222.22.0.0/16","222.23.0.0/16","222.24.0.0/15","222.26.0.0/15","222.28.0.0/14","222.32.0.0/11","222.64.0.0/13","222.72.0.0/15","222.74.0.0/16","222.75.0.0/16","222.76.0.0/14","222.80.0.0/15","222.82.0.0/16","222.83.0.0/17","222.83.128.0/17","222.84.0.0/16","222.85.0.0/17","222.85.128.0/17","222.86.0.0/15","222.88.0.0/15","222.90.0.0/15","222.92.0.0/14","222.125.0.0/16","222.126.128.0/17","222.128.0.0/14","222.132.0.0/14","222.136.0.0/13","222.160.0.0/15","222.162.0.0/16","222.163.0.0/19","222.163.32.0/19","222.163.64.0/18","222.163.128.0/17","222.168.0.0/15","222.170.0.0/15","222.172.0.0/17","222.172.128.0/17","222.173.0.0/16","222.174.0.0/15","222.176.0.0/13","222.184.0.0/13","222.192.0.0/14","222.196.0.0/15","222.198.0.0/16","222.199.0.0/16","222.200.0.0/14","222.204.0.0/15","222.206.0.0/15","222.208.0.0/13","222.216.0.0/15","222.218.0.0/16","222.219.0.0/16","222.220.0.0/15","222.222.0.0/15","222.240.0.0/13","222.248.0.0/16","222.249.0.0/17","222.249.128.0/19","222.249.160.0/20","222.249.176.0/20","222.249.192.0/18","223.0.0.0/15","223.2.0.0/15","223.4.0.0/14","223.8.0.0/13","223.20.0.0/15","223.27.184.0/22","223.64.0.0/11","223.96.0.0/12","223.112.0.0/14","223.116.0.0/15","223.120.0.0/13","223.128.0.0/15","223.144.0.0/12","223.160.0.0/14","223.166.0.0/15","223.192.0.0/15","223.198.0.0/15","223.201.0.0/16","223.202.0.0/15","223.208.0.0/14","223.212.0.0/15","223.214.0.0/15","223.220.0.0/15","223.223.176.0/20","223.223.192.0/20","223.240.0.0/13","223.248.0.0/14","223.252.128.0/17","223.254.0.0/16","223.255.0.0/17","223.255.236.0/22","223.255.252.0/23"]
