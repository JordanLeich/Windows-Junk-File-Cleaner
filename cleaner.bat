@ECHO OFF

title Windows Junk File Cleanup
color 0a

REM Removing all junk files.
echo Removing all junk files . . .
echo.

del "C:\Windows\Prefetch\*.*" /s /f /q
del %temp%\*.* /s /f /q
del "C:\Windows\Temp\*.*" /s /f /q
del "%AppData%\Local\Microsoft\Windows\INetCache\IE\*.*" /s /f /q
del "C:\Windows\Downloaded Program Files\*.*" /s /f /q
del "\$Recycle.Bin\%SID%\*.*" /s /f /q

REM Finished.
echo.
echo All junk files removed!
echo.
pause

