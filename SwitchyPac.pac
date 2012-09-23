function regExpMatch(url, pattern) {
	try { return new RegExp(pattern).test(url); } catch(ex) { return false; }
}

function FindProxyForURL(url, host) {
	if (shExpMatch(url, "*goo|t\\.co|gfw|facebook|twitter|wikipedia|newsmth*")) return 'PROXY 127.0.0.1:1998';
	if (shExpMatch(url, "*weibo|sina|douban|qq|xunlei|quantserve|renren|360|baidu|youdao*")) return 'DIRECT';
	if(shExpMatch(host, 'localhost')) return 'DIRECT';
	if(shExpMatch(host, '127.0.0.1')) return 'DIRECT';
	if(shExpMatch(host, '<local>')) return 'DIRECT';
        if (
            shExpMatch(url,'*.mzxzx.com/*') ||
            shExpMatch(url,'*hioo*') ||
            shExpMatch(url,'*.gg.ma/*') ||
            shExpMatch(url,'*.qs99w.com/*') ||
            shExpMatch(url,'*.unkzone.net/*') ||
            shExpMatch(url,'*bipics.net/*') ||
            shExpMatch(url,'*pen.io*') ||
            shExpMatch(url,'*cl.orc.st*')||
            shExpMatch(url,'*.5917.me/*') ||
            shExpMatch(url,'*.dmxf.com/*') ||
            shExpMatch(url,'*.h5gal.net/*') ||
            shExpMatch(url,'*.tumblr.com/*') ||
            shExpMatch(url,'*35xs*') ||
            shExpMatch(url,'*.hkpic.net/*') ||
            shExpMatch(url,'*.myforum.com.hk/*') ||
            shExpMatch(url,'*.sankakucomplex.com/*')||
            shExpMatch(url,'*.sankakustatic.com/*')||
            shExpMatch(url,'*chrislin2k.com/*')||
            shExpMatch(url,'*bipics.net/*')||
            shExpMatch(url,'*bisi-forum.com/*')) { return DIRECT;}
	return 'PROXY 127.0.0.1:1998';
}
