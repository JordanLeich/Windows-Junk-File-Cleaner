@ECHO OFF

title Windows Junk File Cleanup
color 0a

REM Removing junk files.
echo Removing junk files . . .

del "C:\Windows\Prefetch\*.*" /s /f /q
del %temp%\*.* /s /f /q
del "C:\Windows\Temp\*.*" /s /f /q
del "%AppData%\Local\Microsoft\Windows\INetCache\IE\*.*" /s /f /q
del "C:\Windows\Downloaded Program Files\*.*" /s /f /q
del "\$Recycle.Bin\%SID%\*.*" /s /f /q

REM Finished.
echo All junk files removed!

