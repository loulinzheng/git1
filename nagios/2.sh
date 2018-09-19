#!/bin/sh
while [ 1 ] 
do
sleep 1h
pid=`ping 120.199.53.201  -c 4 -s 1000| grep time= | wc -l`
#echo $pid
if [ $pid -ne 4 ];  then 
  /bin/echo "yidong network is error" |  /bin/mail -s error  15088256320@139.com 

#else
#   echo "ok"
fi
done

