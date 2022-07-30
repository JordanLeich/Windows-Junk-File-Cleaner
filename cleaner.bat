@ECHO OFF

title Windows Junk File Cleanup
color 0a

REM Removing all junk files.
echo Removing all junk files . . .
echo.

rd "%temp%" /s /q
rd "%WINDIR%\Temp" /s /q
rd "%TMP%" /s /q
rd "%AppData%\Local\Microsoft\Windows\INetCache\IE" /s /q

del "%WINDIR%\Downloaded Program Files\*" /s /f /q

cd /d %WINDIR%\Prefetch
for /F "delims=" %%i in ('dir /b') do (rmdir "%%i" /s/q || del "%%i" /s/q)

for /f "skip=1" %%d in ('wmic logicaldisk get DeviceID ^| findstr /v /r "^$"') do for /f "delims=" %%u in ('dir /a /b %%d\$Recycle.bin 2^>nul') do rd "%%d\$Recycle.bin\%%u" /s /q

REM Finished.
echo.
echo All junk files removed!
echo.
pause

