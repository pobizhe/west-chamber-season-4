@echo off
echo. IE◊‘∂Ø≈‰÷√Ω≈±æ(PAC)
pause

@reg add "HKCU\SOFTWARE\Microsoft\windows\CurrentVersion\Internet Settings" /v AutoConfigURL /t REG_SZ /d "file://%cd%\flora_pac.pac" /f
@reg add "HKU\S-1-5-21-823518204-1993962763-1177238915-500\SOFTWARE\Microsoft\windows\CurrentVersion\Internet Settings" /v AutoConfigURL /t REG_SZ /d "file://%cd%\flora_pac.pac" /f  