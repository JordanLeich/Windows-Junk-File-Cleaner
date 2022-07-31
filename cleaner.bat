@ECHO OFF

title Windows Junk File Cleanup
color 0a

echo Running windows built in Disk Cleanup tool . . .
echo.

REM Running windows built in Disk Cleanup tool.
cleanmgr.exe /sagerun:1
pause
echo. 

echo Removing more junk folders and files . . .
echo.
REM Removing more junk folders and files that the Disk Cleanup tool does not clean.
rd "%temp%" /s /q
rd "%WINDIR%\Temp" /s /q
rd "%WINDIR%\Prefetch" /s /q
rd "%userprofile%\AppData\Local\Microsoft\Windows\INetCache\IE" /s /q

del "%WINDIR%\Downloaded Program Files\*" /s /f /q

for /f "skip=1" %%d in ('wmic logicaldisk get DeviceID ^| findstr /v /r "^$"') do for /f "delims=" %%u in ('dir /a /b %%d\$Recycle.bin 2^>nul') do rd "%%d\$Recycle.bin\%%u" /s /q

REM Finished.
echo.
echo All junk folders and files removed!
echo.
pause

