:HASE
c:\windows\system32\tasklist.exe | find /c "notepad.exe" >1.txt
set /p a=<1.txt
echo %a%
if %a% equ 0 start c:\windows\system32\notepad.exe
@ECHO Wscript.Sleep(60000) > sleep.vbs
@START /w wscript.exe sleep.vbs
@DEL /Q sleep.vbs

goto HASE
:END


rem tasklist /svc
rem sc start 