@echo off
CLS
color 17
@title Hosts自动更新程序  By  FGQI  2012-11-10

:MENU
echo.          =-=-=-=-=Hosts自动更新程序菜单=-=-=-=-= 
echo.
echo. 本程序只会更新相应的hosts地址，不会影响你hosts里面原有的其它地址
echo.
echo. 2012-11-10 换IP段
echo.
echo. 1 运行Google脚本，使用北京服务器地址更新Google服务地址（推荐使用这个）
echo.
echo. 2 运行Google脚本，使用www.g.cn的地址更新Google服务地址
echo.
echo. 3 恢复Google顶部的黑色导航栏
echo.
echo. 4 退出
echo.
echo. 5 还原前一个hosts
echo.
echo. 6 Android手机专用的Google服务hosts(Google hosts for Android）
echo.
echo. 7 访问发布页，提出意见并查看hosts的最新更新情况
echo.

echo. 请输入选择项目的序号并按回车键运行：
set /p XUANXIANG= 
if "%XUANXIANG%"=="1" goto 1
if "%XUANXIANG%"=="2" goto 2
if "%XUANXIANG%"=="3" goto 3
if "%XUANXIANG%"=="4" goto 4
if "%XUANXIANG%"=="5" goto 5
if "%XUANXIANG%"=="6" goto 6
if "%XUANXIANG%"=="7" goto 7

:1
echo.
echo 正在使用Google北京服务器地址更新hosts，请稍等
setlocal enabledelayedexpansion
set min=202
set max=229
set /a mod=!max!-!min!+1
set /a r=!random!%%!mod!+!min!
set GOOGLE=203.208.46.%r%
type %windir%\System32\drivers\etc\hosts|find "FGQI" /i /v|find "Google" /i /v|find "ggpht" /i /v|find "gmail" /i /v|find "gstatic" /i /v|find "appspot" /i /v|find "sandai" /i /v|find "github" /i /v|findstr "." >>%windir%\System32\drivers\etc\hostsfgqi
if exist %windir%\System32\drivers\etc\hosts.backup1 del %windir%\System32\drivers\etc\hosts.backup1 /q
if exist %windir%\System32\drivers\etc\hosts.backup ren %windir%\System32\drivers\etc\hosts.backup hosts.backup1
if exist %windir%\System32\drivers\etc\hosts ren %windir%\System32\drivers\etc\hosts hosts.backup
ren %windir%\System32\drivers\etc\hostsfgqi hosts
echo	58.61.39.206	hub5idx.shub.sandai.net	>>%windir%\System32\drivers\etc\hosts
echo	121.9.209.135	hub5pr.sandai.net	>>%windir%\System32\drivers\etc\hosts
echo	#Google By FGQI	>>%windir%\System32\drivers\etc\hosts
echo	207.97.227.239	github.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	drive.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	doc-10-3o-docs.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	play.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	0-focus-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	3hdrrlnlknhi77nrmsjnjr152ueo3soc-a-calendar-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	accounts.google.com	>>%windir%\System32\drivers\etc\hosts
echo	74.125.71.139	www.appspot.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	ajax.googleapis.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	android.l.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	apis.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	appengine.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	bks0.books.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	bks1.books.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	bks2.books.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	bks3.books.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	bks4.books.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	bks5.books.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	bks6.books.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	bks7.books.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	bks8.books.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	bks9.books.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	blogsearch.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	blogsearch.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	books.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	browserchannel-docs.l.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	browserchannel-spreadsheets.l.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	browsersync.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	cache.pack.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	calendar.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	chatenabled.mail.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	checkout.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	chrome.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	clients1.google.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.102	clients1.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	clients2.google.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.102	clients2.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	clients3.google.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.102	clients3.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	clients4.google.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.102	clients4.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	clients5.google.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.102	clients5.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	clients6.google.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.102	clients6.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	clients7.google.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.102	clients7.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	code.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	www.gstatic.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	csi.gstatic.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	desktop.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	desktop2.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	ditu.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	ditu.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	dl.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	docs.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	earth.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	encrypted.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	encrypted.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	encrypted-tbn0.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	encrypted-tbn1.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	encrypted-tbn2.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	encrypted-tbn3.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	feedback.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	finance.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	fonts.googleapis.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	g0.gstatic.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	gg.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	ghs.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	ghs.l.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	googlecl.googlecode.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	googlehosted.l.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	groups.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	id.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	id.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	id.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	images.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	images.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	images0-focus-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	images1-focus-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	images2-focus-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	images3-focus-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	images4-focus-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	images5-focus-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	images6-focus-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	images-lso-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	images-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	images-pos-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	investor.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	khms0.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	khms1.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	labs.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	large-uploads.l.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	lh1.ggpht.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	lh1.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	lh2.ggpht.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	lh2.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	lh3.ggpht.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	lh3.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	lh4.ggpht.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	lh4.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	lh5.ggpht.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	lh5.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	lh6.ggpht.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	lh6.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	m.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mail.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mail-attachment.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	maps.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	maps.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	maps.gstatic.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	maps.gstatic.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	maps-api-ssl.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mt0.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mt0.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mt1.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mt1.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mt2.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mt2.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mt3.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mt3.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mts0.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mts1.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	music.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	music.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	music-streaming.l.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mw2.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	news.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	news.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	news.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	newsfeed-dot-latest-dot-rovio-ad-engine.appspot.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	nt0.ggpht.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	nt1.ggpht.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	nt2.ggpht.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	nt3.ggpht.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	oauth.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	ode25pfjgmvpquh3b1oqo31ti5ibg5fr-a-calendar-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	pack.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	pack.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	picasa.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	picasaweb.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	picasaweb.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	places.google.com	>>%windir%\System32\drivers\etc\hosts
echo	74.125.31.102	plus.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	plusone.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	pop.gmail.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	profiles.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	project-slingshot-gp.appspot.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	s1.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	s2.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	s3.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	s4.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	s5.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	s6.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	safebrowsing.clients.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	safebrowsing-cache.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	sandbox.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	scholar.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	scholar.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	scholar.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	scholar.l.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	services.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	sites.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	sketchup.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	spreadsheets.google.com	>>%windir%\System32\drivers\etc\hosts
echo	74.125.235.254	ssl.google-analytics.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	ssl.gstatic.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	suggestqueries.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	t.doc-0-0-sj.sj.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	t0.gstatic.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	t1.gstatic.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	t2.gstatic.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	t3.gstatic.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.138	talkgadget.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	talkx.l.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	themes.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	toolbar.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	toolbar.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	toolbarqueries.clients.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	toolbarqueries.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	tools.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	translate.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	translate.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	translate.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	translate.googleapis.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	uploadsj.clients.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	v8mq9slfbk1dglresapkg0i5f8pm64lc-a-calendar-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	video.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	video.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	video.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	voice.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	wave.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	webcache.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	wenda.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	www.gmail.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	www.windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	www.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	www.googleadservices.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	www.google-analytics.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	www.googleapis.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	www.googlelabs.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	www-calendar-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	www-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	www-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	r3270-dot-latest-dot-project-slingshot-gp.appspot.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	bt26mravu2qpe56n8gnmjnpv2inl84bf-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	rbjhe237k979f79d87gmenp3gejfonu9-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	k6v18tjr24doa89b55o3na41kn4v73eb-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	8kubpeu8314p2efdd7jlv09an9i2ljdo-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	adstvca8k2ooaknjjmv89j22n9t676ve-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	ob7f2qc0i50kbjnc81vkhgmb5hsv7a8l-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	53rd6p0catml6vat6qra84rs0del836d-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	u807isd5egseeabjccgcns005p2miucq-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	r70rmsn4s0rhk6cehcbbcbfbs31pu0va-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	59cbv4l9s05pbaks9v77vc3mengeqors-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	i8brh95qor6r54nkl52hidj2ggcs4jgm-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	upt14k1i2veesusrda9nfotcrbp9d7p5-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	debh8vg7vd93bco3prdajidmm7dhql3f-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	4fjvqid3r3oq66t548clrdj52df15coc-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	hsco54a20sh11q9jkmb51ad2n3hmkmrg-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	qhie5b8u979rnch1q0hqbrmbkn9estf7-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	e6ha3snmi09c57cs4h4dnoa006cgfjfu-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	66fl6oqbdsqf5fjl032t5iulimtqjhpa-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	vvpk2b7flnbhcm2p10u4hcnatnp40i3i-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	0rgn8o7pqk7dq7rm8q0639erjd8gnf7g-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	cfmmurgvo3fqrmfu0tjfcpgdt7mh6ccv-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts

echo.
echo 成功运行完Google脚本
echo.
echo Google Reader、Groups、Map（加星功能）服务请使用Https链接
echo.
echo 按任意键返回菜单，之前的hosts备份为hosts.backup
pause
CLS
goto MENU

:2
echo.
echo 请稍等,正在获取Google服务器的IP
for /f "tokens=2 delims=[]" %%i in ('ping www.g.cn') do set GOOGLE=%%i
for /f "delims=." %%i in ("%GOOGLE%") do if %%i==203 (echo 你获取的是北京服务器的地址，正在更新hosts，请稍等) else echo 你获取的是%GOOGLE%，不是Google北京服务器地址，正在更新hosts，请稍等
for /f "delims=." %%i in ("%GOOGLE%") do if not %%i==203 echo 因为地址不是北京服务器，可能导致服务不能用，推荐使用选项 1 更新hosts
type %windir%\System32\drivers\etc\hosts|find "FGQI" /i /v|find "Google" /i /v|find "ggpht" /i /v|find "gmail" /i /v|find "gstatic" /i /v|find "appspot" /i /v|find "sandai" /i /v|find "github" /i /v|findstr "." >>%windir%\System32\drivers\etc\hostsfgqi
if exist %windir%\System32\drivers\etc\hosts.backup1 del %windir%\System32\drivers\etc\hosts.backup1 /q
if exist %windir%\System32\drivers\etc\hosts.backup ren %windir%\System32\drivers\etc\hosts.backup hosts.backup1
if exist %windir%\System32\drivers\etc\hosts ren %windir%\System32\drivers\etc\hosts hosts.backup
ren %windir%\System32\drivers\etc\hostsfgqi hosts
echo	58.61.39.206	hub5idx.shub.sandai.net	>>%windir%\System32\drivers\etc\hosts
echo	121.9.209.135	hub5pr.sandai.net	>>%windir%\System32\drivers\etc\hosts
echo	#Google By FGQI	>>%windir%\System32\drivers\etc\hosts
echo	207.97.227.239	github.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	drive.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	doc-10-3o-docs.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	play.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	0-focus-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	3hdrrlnlknhi77nrmsjnjr152ueo3soc-a-calendar-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	accounts.google.com	>>%windir%\System32\drivers\etc\hosts
echo	74.125.71.139	www.appspot.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	ajax.googleapis.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	android.l.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	apis.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	appengine.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	bks0.books.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	bks1.books.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	bks2.books.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	bks3.books.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	bks4.books.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	bks5.books.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	bks6.books.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	bks7.books.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	bks8.books.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	bks9.books.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	blogsearch.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	blogsearch.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	books.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	browserchannel-docs.l.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	browserchannel-spreadsheets.l.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	browsersync.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	cache.pack.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	calendar.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	chatenabled.mail.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	checkout.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	chrome.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	clients1.google.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.102	clients1.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	clients2.google.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.102	clients2.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	clients3.google.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.102	clients3.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	clients4.google.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.102	clients4.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	clients5.google.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.102	clients5.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	clients6.google.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.102	clients6.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	clients7.google.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.102	clients7.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	code.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	www.gstatic.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	csi.gstatic.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	desktop.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	desktop2.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	ditu.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	ditu.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	dl.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	docs.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	earth.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	encrypted.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	encrypted.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	encrypted-tbn0.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	encrypted-tbn1.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	encrypted-tbn2.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	encrypted-tbn3.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	feedback.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	finance.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	fonts.googleapis.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	g0.gstatic.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	gg.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	ghs.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	ghs.l.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	googlecl.googlecode.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	googlehosted.l.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	groups.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	id.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	id.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	id.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	images.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	images.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	images0-focus-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	images1-focus-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	images2-focus-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	images3-focus-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	images4-focus-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	images5-focus-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	images6-focus-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	images-lso-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	images-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	images-pos-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	investor.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	khms0.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	khms1.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	labs.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	large-uploads.l.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	lh1.ggpht.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	lh1.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	lh2.ggpht.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	lh2.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	lh3.ggpht.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	lh3.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	lh4.ggpht.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	lh4.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	lh5.ggpht.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	lh5.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	lh6.ggpht.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	lh6.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	m.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mail.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mail-attachment.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	maps.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	maps.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	maps.gstatic.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	maps.gstatic.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	maps-api-ssl.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mt0.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mt0.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mt1.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mt1.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mt2.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mt2.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mt3.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mt3.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mts0.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mts1.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	music.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	music.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	music-streaming.l.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	mw2.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	news.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	news.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	news.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	newsfeed-dot-latest-dot-rovio-ad-engine.appspot.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	nt0.ggpht.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	nt1.ggpht.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	nt2.ggpht.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	nt3.ggpht.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	oauth.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	ode25pfjgmvpquh3b1oqo31ti5ibg5fr-a-calendar-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	pack.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	pack.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	picasa.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	picasaweb.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	picasaweb.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	places.google.com	>>%windir%\System32\drivers\etc\hosts
echo	74.125.31.102	plus.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	plusone.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	pop.gmail.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	profiles.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	project-slingshot-gp.appspot.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	s1.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	s2.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	s3.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	s4.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	s5.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.132	s6.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	safebrowsing.clients.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	safebrowsing-cache.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	sandbox.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	scholar.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	scholar.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	scholar.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	scholar.l.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	services.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	sites.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	sketchup.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	spreadsheets.google.com	>>%windir%\System32\drivers\etc\hosts
echo	74.125.235.254	ssl.google-analytics.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	ssl.gstatic.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	suggestqueries.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	t.doc-0-0-sj.sj.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	t0.gstatic.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	t1.gstatic.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	t2.gstatic.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	t3.gstatic.com	>>%windir%\System32\drivers\etc\hosts
echo	173.194.72.102	talkgadget.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	talkx.l.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	themes.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	toolbar.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	toolbar.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	toolbarqueries.clients.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	toolbarqueries.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	tools.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	translate.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	translate.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	translate.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	translate.googleapis.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	uploadsj.clients.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	v8mq9slfbk1dglresapkg0i5f8pm64lc-a-calendar-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	video.google.cn	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	video.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	video.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	voice.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	wave.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	webcache.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	wenda.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	www.gmail.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	www.google.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	www.google.com.hk	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	www.googleadservices.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	www.google-analytics.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	www.googleapis.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	www.googlelabs.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	www-calendar-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	www-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	www-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	r3270-dot-latest-dot-project-slingshot-gp.appspot.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	bt26mravu2qpe56n8gnmjnpv2inl84bf-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	rbjhe237k979f79d87gmenp3gejfonu9-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	k6v18tjr24doa89b55o3na41kn4v73eb-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	8kubpeu8314p2efdd7jlv09an9i2ljdo-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	adstvca8k2ooaknjjmv89j22n9t676ve-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	ob7f2qc0i50kbjnc81vkhgmb5hsv7a8l-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	53rd6p0catml6vat6qra84rs0del836d-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	u807isd5egseeabjccgcns005p2miucq-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	r70rmsn4s0rhk6cehcbbcbfbs31pu0va-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	59cbv4l9s05pbaks9v77vc3mengeqors-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	i8brh95qor6r54nkl52hidj2ggcs4jgm-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	upt14k1i2veesusrda9nfotcrbp9d7p5-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	debh8vg7vd93bco3prdajidmm7dhql3f-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	4fjvqid3r3oq66t548clrdj52df15coc-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	hsco54a20sh11q9jkmb51ad2n3hmkmrg-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	qhie5b8u979rnch1q0hqbrmbkn9estf7-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	e6ha3snmi09c57cs4h4dnoa006cgfjfu-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	66fl6oqbdsqf5fjl032t5iulimtqjhpa-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	vvpk2b7flnbhcm2p10u4hcnatnp40i3i-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	0rgn8o7pqk7dq7rm8q0639erjd8gnf7g-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts
echo	%GOOGLE%	cfmmurgvo3fqrmfu0tjfcpgdt7mh6ccv-a-oz-opensocial.googleusercontent.com	>>%windir%\System32\drivers\etc\hosts


echo.
echo 成功运行完Google脚本
echo.
echo Google Reader、Groups、Map（加星功能）服务请使用Https链接
echo.
echo 按任意键返回菜单，之前的hosts备份为hosts.backup
pause
CLS
goto MENU

:3
echo.
start http://www.google.com/ncr
CLS
goto MENU

:5
echo.
if exist %windir%\System32\drivers\etc\hosts ren %windir%\System32\drivers\etc\hosts hosts.backup2
if exist %windir%\System32\drivers\etc\hosts.backup ren %windir%\System32\drivers\etc\hosts.backup hosts
if exist %windir%\System32\drivers\etc\hosts.backup2 ren %windir%\System32\drivers\etc\hosts.backup2 hosts.backup
echo 已经还原完hosts，之前的hosts备份为hosts.backup
pause
CLS
goto MENU

:6
start https://plus.google.com/109906764666611489817/posts/Z854TLWuTPV
CLS
goto MENU

:7
start https://plus.google.com/109906764666611489817/posts/iRs7zi4hHqB
CLS
goto MENU


:4

