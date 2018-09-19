@echo off

echo 为保护您的电脑免受“勒索病毒”的攻击，入网规范管理系统正在为您电脑进行安全加固

ver | find "5.0." > NUL && goto LessThanWin7
ver | find "5.1." > NUL && goto LessThanWin7
ver | find "5.2." > NUL && goto LessThanWin7
goto MoreThanWin7


REM win xp
:LessThanWin7

netsh firewall set opmode mode=ENABLE > NUL

netsh firewall set portopening ALL 135 DISABLE > NUL
netsh firewall set portopening ALL 137 DISABLE > NUL
netsh firewall set portopening ALL 138 DISABLE > NUL
netsh firewall set portopening ALL 139 DISABLE > NUL
netsh firewall set portopening ALL 445 DISABLE > NUL

exit

REM win7
:MoreThanWin7

netsh advfirewall set currentprofile state on > NUL
netsh advfirewall set domainprofile state on > NUL
netsh advfirewall set privateprofile state on > NUL

netsh advfirewall firewall add rule name="deny tcp 135 in" dir=in protocol=tcp localport=135 action=block > NUL
netsh advfirewall firewall add rule name="deny tcp 135 out" dir=out protocol=tcp localport=135 action=block > NUL
netsh advfirewall firewall add rule name="deny udp 135 in" dir=in protocol=udp localport=135 action=block > NUL
netsh advfirewall firewall add rule name="deny udp 135 out" dir=out protocol=udp localport=135 action=block > NUL

netsh advfirewall firewall add rule name="deny tcp 137 in" dir=in protocol=tcp localport=137 action=block > NUL
netsh advfirewall firewall add rule name="deny tcp 137 out" dir=out protocol=tcp localport=137 action=block > NUL
netsh advfirewall firewall add rule name="deny udp 137 in" dir=in protocol=udp localport=137 action=block > NUL
netsh advfirewall firewall add rule name="deny udp 137 out" dir=out protocol=udp localport=137 action=block > NUL

netsh advfirewall firewall add rule name="deny tcp 138 in" dir=in protocol=tcp localport=138 action=block > NUL
netsh advfirewall firewall add rule name="deny tcp 138 out" dir=out protocol=tcp localport=138 action=block > NUL
netsh advfirewall firewall add rule name="deny udp 138 in" dir=in protocol=udp localport=138 action=block > NUL
netsh advfirewall firewall add rule name="deny udp 138 out" dir=out protocol=udp localport=138 action=block > NUL

netsh advfirewall firewall add rule name="deny tcp 139 in" dir=in protocol=tcp localport=139 action=block > NUL
netsh advfirewall firewall add rule name="deny tcp 139 out" dir=out protocol=tcp localport=139 action=block > NUL
netsh advfirewall firewall add rule name="deny udp 139 in" dir=in protocol=udp localport=139 action=block > NUL
netsh advfirewall firewall add rule name="deny udp 139 out" dir=out protocol=udp localport=139 action=block > NUL

netsh advfirewall firewall add rule name="deny tcp 445 in" dir=in protocol=tcp localport=445 action=block > NUL
netsh advfirewall firewall add rule name="deny tcp 445 out" dir=out protocol=tcp localport=445 action=block > NUL
netsh advfirewall firewall add rule name="deny udp 445 in" dir=in protocol=udp localport=445 action=block > NUL
netsh advfirewall firewall add rule name="deny udp 445 out" dir=out protocol=udp localport=445 action=block > NUL

exit
