双向丢包
--------
服务器、客户端同时丢掉GFW 的干扰包。服务器上脚本 server.sh ，客户端脚本 client.sh. 如果路由器可以设置 iptables 防火墙(如Tomato 或 OpenWRT)，直接在路由器上设置即可：

    iptables -I FORWARD -p tcp -m tcp --tcp-flags RST RST -j DROP
    
目前这种方法还有问题。第一次丢包可以成功，第二次会被GFW发的SYN+ACK 干扰，而且这个非RESET的干扰包似乎不太好丢, 因为iptables 没有针对SEQ 错乱的丢包规则。
学术上, 这种攻击被定义为 Off-Path TCP Sequence Number Inference Attack [PDF](http://web.eecs.umich.edu/~zhiyunq/pub/oakland12_TCP_sequence_number_inference.pdf)
另外, GFW 对reset 惩罚, 最近(2012.11.09) 改成临时性的IP封锁. 这样丢包就没太大意义了. 

DoS攻击
-------
这种方式暂时不能翻墙，但是，理论上可以增加GFW的负载。期望是，攻击者达到一定数量之后，能够降低GFW 的reset 判断精度，或者迫使其放弃对CRLF 注入的reset。
使用方法：

    cd west-chamber-proxy;
    sh dos.sh start 
    sh dos.sh status 
    sh dos.sh stop #停止

Windows 用户可以直接双机 dos.py （可以同时打开N个

修改本地hosts文件
----------------
修改本地的 hosts 文件，并使用https 方式访问。参考[smarthosts](http://code.google.com/p/smarthosts/)项目。
 

反DNS污染
-------
修改hosts 文件部分解决了污染问题, 但是很可能不全. 要彻底解决DNS污染，设置国外的DNS 服务器，并本机丢弃GFW的 DNS伪包。

    a) 国外DNS服务器。大家比较熟悉的可能是[Google Public DNS](http://code.google.com/speed/public-dns/)。但是Google DNS经常出问题。先推荐两个，台湾中华电信的168.95.1.1 和 [OpenDNS](http://www.opendns.com/), 还不行，那就上午搜一个国外的DNS。

    b) 自建DNS 服务器。系统要求：Linux 或 Mac。可以用dnsmasq 做本地的DNS服务器。如果在国内有Linux服务器，建议做一个DNS服务小范围共享。

    c) 丢弃DNS伪包。
    * Linux: 需要有iptables。如果 iptables 有 u32模块(或者你能自己搞定安装一个)，可以直接用本项目中的 client.sh；否则，只能自己编译原始的[西厢项目](http://code.google.com/p/scholarzhang)，具体操作看西厢的文档。

其它值得尝试的方法：[如何本地避免GFW的DNS污染](http://liruqi.info/post/28775426009/how-to-avoid-dns-hijack-locally)

项目目的
--------
* 不依赖代理服务器的本地翻墙代理工具。
* [项目维护地址](https://github.com/gdwgi1225/west-chamber-season-3)
* [Follow up](https://plus.google.com/b/108661470402896863593/)

使用方法
--------
* Windows

    1. 下载[客户端](http://code.google.com/p/west-chamber-season-3/downloads/list) ，解压缩，双击 exe
    2. 把浏览器HTTP/HTTPS 代理设置为 127.0.0.1:1998，或者使用pac 脚本设置自动代理。
    3. Windows 版本更新比较慢。如果希望使用最新代码，先下载 python 2.7，[32位](http://python.org/ftp/python/2.7.2/python-2.7.2.msi) / [64位](http://python.org/ftp/python/2.7.2/python-2.7.2.amd64.msi) ，然后下载[代码](https://github.com/liruqi/west-chamber-season-3/zipball/master)，解压缩，进入 west-chamber-proxy 文件夹，双击 westchamberproxy.py。

* Mac 
    1. 去GoAgentX for WCProxy的[下载列表](https://github.com/liruqi/GoAgentX/downloads)下载最新的客户端，解压缩，双击打开
    2. 把浏览器HTTP/HTTPS 代理设置为 127.0.0.1:1998，或者使用pac 脚本设置自动代理。
    
* Linux

    1. 下载项目代码: [zip](https://github.com/liruqi/west-chamber-season-3/zipball/master)
    2. 解压缩，打开终端，cd 到代码目录，cd west-chamber-proxy; 启动代理：./wcproxy start；关闭代理：./wcproxy stop。
    3. 把浏览器HTTP/HTTPS 代理设置为 127.0.0.1:1998，或者使用pac 脚本设置自动代理。

* Android

    基于[GAE Proxy](http://code.google.com/p/gaeproxy/)修改的。Google Market 上的[地址](https://market.android.com/details?id=org.westchamberproxy)。

* iOS
    
    目前不打算自己做一个iOS 应用放在 appstore上，比较麻烦。越狱版本的可能最近会推出。

    1. 局域网内的其它设备(PC, Android 设备)上安装本代理，然后把 iOS 设备的 HTTP 代理设置到该设备上。（或者在国内有服务器的同学，自己搭建HTTP 代理）
    2. 类似GoAgent 那种iOS客户端的办法。需要越狱。单我本人没有iOS设备，所以，暂不研究了。

* SSL证书
    如果希望HTTPS代理正常使用，在Windows上用管理员权限、Mac 上用root 权限执行本代理即可。

代理设置
--------

* 浏览器代理设置
    做了一个 [.pac 文件](https://raw.github.com/gdwgi1225/west-chamber-season-3/master/SwitchyPac.pac)。下载这个pac 文件，然后在代理设置中导入即可。
    具体使用方法, IE, Firefox, Safari 都可以设置自动代理配置。

* Chrome浏览器+SwitchySharp扩展

    Chrome可以直接在高级选项中设置代理服务器，不过这样Chrome会修改系统的代理设置. 要实现Chrome自动代理配置，可以使用switchysharp扩展.
    首先安装[SwitchySharp](https://chrome.google.com/webstore/detail/dpplabbmogkhghncfbfdeeokoefdjegm), 安装后的设置：
   
    1. 在switchysharp选项页面，点击后面的导入/导出 -> “在线恢复备份”后面的输入框粘贴进下面的链接 http://west-chamber-season-3.googlecode.com/files/SwitchyOptions.bak
    2. 点击在线恢复备份 -> 确定 
    3. 点击SwitchySharp扩展图标 -> 自动切换模式

    到此浏览器代理配置成功。

* 代理自身的代理配置

    1. 默认配置是GoAgent，包含若干内置的appid, 如果有自己的appid 建议更换，在 config.py 里面替换即可。
    2. 也可以设置socks5代理。如 `ssh -NfD 0.0.0.0:1234 user@hostname` 启动代理之后，把PROXY_TYPE的配置 "goagent" 改为 "socks5"，然后把 SOCKS_HOST/SOCKS_PORT 修改为自己的代理。
    3. 部分配置项也可以在网页上修改，直接打开代理地址即可（如 http://127.0.0.1:1998）

开发者
------
* [XIAOXIA](http://xiaoxia.org), 原始版本作者
* [LIRUQI](http://liruqi.info), 后续开发, 各平台的打包、发布

代理原理
--------

1. 对抗关键词过滤: [rfc2616 - section 4.1](http://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html)
2. 对抗DNS污染: 修改PyDNS 库，实现丢弃GFW DNS 伪包。
3. 对抗IP封锁: 收集被封锁的IP, 在DNS 解析过程中尝试找到可用IP。
4. 如果没有可用IP，或者是HTTP注入导致异常，本代理会走[GoAgent](http://code.google.com/p/goagent/) 代理。

问题反馈
--------
在[这里](https://github.com/liruqi/west-chamber-season-3/issues) 反馈各种问题。 

其它工具
--------
[icefox](https://code.google.com/p/icefox/) 原理跟西厢代理类似,但是此软件可以直接修改系统代理的设置,更方便.目测没解决IP封锁问题.