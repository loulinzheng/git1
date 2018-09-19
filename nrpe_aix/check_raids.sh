#!/usr/bin/ksh

export NLS_LANG=AMERICAN_AMERICA.ZHS16GBK


export ORACLE_BASE=/oracle

export ORACLE_HOME=/oracle/product/10.2.0/db_1

export PATH=$ORACLE_HOME/bin:$PATH

export ORACLE_SID=sportdb



#date >> /data/1.txt
#echo "select count(*) from v\$open_cursor;" | sqlplus / as sysdba >> /data/1.txt


#echo '##################Start##########################' >>/data/1.txt

#iostat 5 12 >>/data/1.txt

#echo '##################End##########################'   >>/data/1.txt
p=`lsdev -C |grep disk | grep Available | wc -l `
if [ $p = "6" ] ; then     #如果是linux的话打印linux字符串

{ echo "OK!There are $p disks in";
exit 0; 
}
else 
{ echo "No!There are only $p disks now";
exit 2;
}
fi


