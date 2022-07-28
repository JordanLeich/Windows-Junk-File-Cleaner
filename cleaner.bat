@ECHO OFF

title Windows Junk File Cleanup
color 0a

REM Removing all junk files.
echo Removing all junk files . . .
echo.

cd /d %WINDIR%\Prefetch
for /F "delims=" %%i in ('dir /b') do (rmdir "%%i" /s/q || del "%%i" /s/q)

cd /d %temp%
for /F "delims=" %%i in ('dir /b') do (rmdir "%%i" /s/q || del "%%i" /s/q)

cd /d %WINDIR%\Temp
for /F "delims=" %%i in ('dir /b') do (rmdir "%%i" /s/q || del "%%i" /s/q)

cd /d %TMP%
for /F "delims=" %%i in ('dir /b') do (rmdir "%%i" /s/q || del "%%i" /s/q)

del "%Windows%\Downloaded Program Files\*" /s /f /q
del "%AppData%\Local\Microsoft\Windows\INetCache\IE\*" /s /f /q
del "\$Recycle.Bin\%SID%\*" /s /f /q

REM Finished.
echo.
echo All junk files removed!
echo.
pause

