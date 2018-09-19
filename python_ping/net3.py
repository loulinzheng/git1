
#!/usr/bin/env python
import time
import datetime
import pyodbc
import os


var = 1
while var <= 7 :  # five day is a circle
    if var==7 :
        #clear var to 1
        cnxn2 = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=10.200.198.9;DATABASE=OpenMas;UID=aa;PWD=bb')
        cursor = cnxn2.cursor()
        cursor.execute("insert into COM_SmsSent_3  ( MessageID,  MessageContent, ExtendCode,  DestinationAddress,  SendType,       SendTime,         IsWapPush,         WapUrl,         CreateTime    )    VALUES ('%s','%s','%s','%s','%d','%s','%d','%s','%s')"  % (      '1', 'The networks has been running 7 days.','NULL',  '15088256320', 0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0,'NULL', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     ))
        cnxn2.commit()
        cnxn2.close()
        #
        #
        var=1
    else :
        print var
        var=var+1
    for i in range(1,25):#48 * 30 min=24hour=1day   3-1=2
        #test the data
        #print datetime.datetime.now()

        if os.system('ping -l 1000 61.164.34.113')>0:
            #alarm.system has been down

            cnxn2 = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=10.200.198.9;DATABASE=OpenMas;UID=aa;PWD=bb')
            cursor = cnxn2.cursor()
            cursor.execute("insert into COM_SmsSent_3  ( MessageID,  MessageContent, ExtendCode,  DestinationAddress,  SendType,       SendTime,         IsWapPush,         WapUrl,         CreateTime    )    VALUES ('%s','%s','%s','%s','%d','%s','%d','%s','%s')"  % (      '1', '61.164.34.113 is down!','NULL',  '15088256320', 0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0,'NULL', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     ))
            cnxn2.commit()
            cnxn2.close()            #
            #
            #
            #
            #var=0
        if os.system('ping -l 1000 10.200.9.254')>0:
            #alarm.system has been down

            cnxn2 = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=10.200.198.9;DATABASE=OpenMas;UID=aa;PWD=bb')
            cursor = cnxn2.cursor()
            cursor.execute("insert into COM_SmsSent_3  ( MessageID,  MessageContent, ExtendCode,  DestinationAddress,  SendType,       SendTime,         IsWapPush,         WapUrl,         CreateTime    )    VALUES ('%s','%s','%s','%s','%d','%s','%d','%s','%s')"  % (      '1', '10.200.9.254 is down!','NULL',  '15088256320', 0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0,'NULL', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     ))
            cnxn2.commit()
            cnxn2.close()            #

        if os.system('ping -l 1000 10.200.196.2')>0:
            #alarm.system has been down

            cnxn2 = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=10.200.198.9;DATABASE=OpenMas;UID=aa;PWD=bb')
            cursor = cnxn2.cursor()
            cursor.execute("insert into COM_SmsSent_3  ( MessageID,  MessageContent, ExtendCode,  DestinationAddress,  SendType,       SendTime,         IsWapPush,         WapUrl,         CreateTime    )    VALUES ('%s','%s','%s','%s','%d','%s','%d','%s','%s')"  % (      '1', '10.200.196.2 is down!','NULL',  '15088256320', 0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0,'NULL', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     ))
            cnxn2.commit()
            cnxn2.close()            #

        if os.system('ping -l 1000 10.200.5.254')>0:
            #alarm.system has been down

            cnxn2 = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=10.200.198.9;DATABASE=OpenMas;UID=aa;PWD=bb')
            cursor = cnxn2.cursor()
            cursor.execute("insert into COM_SmsSent_3  ( MessageID,  MessageContent, ExtendCode,  DestinationAddress,  SendType,       SendTime,         IsWapPush,         WapUrl,         CreateTime    )    VALUES ('%s','%s','%s','%s','%d','%s','%d','%s','%s')"  % (      '1', '10.200.5.254 is down!','NULL',  '15088256320', 0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0,'NULL', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     ))
            cnxn2.commit()
            cnxn2.close()            #

        if os.system('ping -l 1000 10.200.6.254')>0:
            #alarm.system has been down

            cnxn2 = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=10.200.198.9;DATABASE=OpenMas;UID=aa;PWD=bb')
            cursor = cnxn2.cursor()
            cursor.execute("insert into COM_SmsSent_3  ( MessageID,  MessageContent, ExtendCode,  DestinationAddress,  SendType,       SendTime,         IsWapPush,         WapUrl,         CreateTime    )    VALUES ('%s','%s','%s','%s','%d','%s','%d','%s','%s')"  % (      '1', '10.200.6.254 is down!','NULL',  '15088256320', 0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0,'NULL', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     ))
            cnxn2.commit()
            cnxn2.close()            #

        if os.system('ping -l 1000 115.236.50.225')>0:
            #alarm.system has been down

            cnxn2 = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=10.200.198.9;DATABASE=OpenMas;UID=aa;PWD=bb')
            cursor = cnxn2.cursor()
            cursor.execute("insert into COM_SmsSent_3  ( MessageID,  MessageContent, ExtendCode,  DestinationAddress,  SendType,       SendTime,         IsWapPush,         WapUrl,         CreateTime    )    VALUES ('%s','%s','%s','%s','%d','%s','%d','%s','%s')"  % (      '1', '115.236.50.225 is down!','NULL',  '15088256320', 0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0,'NULL', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     ))
            cnxn2.commit()
            cnxn2.close()            #

        if os.system('ping -l 1000 10.200.9.253')>0:
            #alarm.system has been down

            cnxn2 = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=10.200.198.9;DATABASE=OpenMas;UID=aa;PWD=bb')
            cursor = cnxn2.cursor()
            cursor.execute("insert into COM_SmsSent_3  ( MessageID,  MessageContent, ExtendCode,  DestinationAddress,  SendType,       SendTime,         IsWapPush,         WapUrl,         CreateTime    )    VALUES ('%s','%s','%s','%s','%d','%s','%d','%s','%s')"  % (      '1', '10.200.9.253 is down!','NULL',  '15088256320', 0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0,'NULL', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     ))
            cnxn2.commit()
            cnxn2.close()            #

            
                #       
        ########################################################

        if os.system('ping -l 1000 10.200.13.254')>0:
            #alarm.system has been down

            cnxn2 = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=10.200.198.9;DATABASE=OpenMas;UID=aa;PWD=bb')
            cursor = cnxn2.cursor()
            cursor.execute("insert into COM_SmsSent_3  ( MessageID,  MessageContent, ExtendCode,  DestinationAddress,  SendType,       SendTime,         IsWapPush,         WapUrl,         CreateTime    )    VALUES ('%s','%s','%s','%s','%d','%s','%d','%s','%s')"  % (      '1', '10.200.13.254 is down!','NULL',  '15088256320', 0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0,'NULL', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     ))
            cnxn2.commit()
            cnxn2.close()            #

            
                #       
        ########################################################

        if os.system('ping -l 1000 10.200.13.253')>0:
            #alarm.system has been down

            cnxn2 = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=10.200.198.9;DATABASE=OpenMas;UID=aa;PWD=bb')
            cursor = cnxn2.cursor()
            cursor.execute("insert into COM_SmsSent_3  ( MessageID,  MessageContent, ExtendCode,  DestinationAddress,  SendType,       SendTime,         IsWapPush,         WapUrl,         CreateTime    )    VALUES ('%s','%s','%s','%s','%d','%s','%d','%s','%s')"  % (      '1', '10.200.13.253 is down!','NULL',  '15088256320', 0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0,'NULL', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     ))
            cnxn2.commit()
            cnxn2.close()            #

            
                #       
        ########################################################

        if os.system('ping -l 1000 10.200.12.253')>0:
            #alarm.system has been down

            cnxn2 = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=10.200.198.9;DATABASE=OpenMas;UID=aa;PWD=bb')
            cursor = cnxn2.cursor()
            cursor.execute("insert into COM_SmsSent_3  ( MessageID,  MessageContent, ExtendCode,  DestinationAddress,  SendType,       SendTime,         IsWapPush,         WapUrl,         CreateTime    )    VALUES ('%s','%s','%s','%s','%d','%s','%d','%s','%s')"  % (      '1', '10.200.12.253 is down!','NULL',  '15088256320', 0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0,'NULL', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     ))
            cnxn2.commit()
            cnxn2.close()            #

            
                #       
        ########################################################

        if os.system('ping -l 1000 10.200.12.254')>0:
            #alarm.system has been down

            cnxn2 = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=10.200.198.9;DATABASE=OpenMas;UID=aa;PWD=bb')
            cursor = cnxn2.cursor()
            cursor.execute("insert into COM_SmsSent_3  ( MessageID,  MessageContent, ExtendCode,  DestinationAddress,  SendType,       SendTime,         IsWapPush,         WapUrl,         CreateTime    )    VALUES ('%s','%s','%s','%s','%d','%s','%d','%s','%s')"  % (      '1', '10.200.12.254 is down!','NULL',  '15088256320', 0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0,'NULL', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     ))
            cnxn2.commit()
            cnxn2.close()            #

            
                #       
        ########################################################

        if os.system('ping -l 1000 10.200.8.253')>0:
            #alarm.system has been down

            cnxn2 = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=10.200.198.9;DATABASE=OpenMas;UID=aa;PWD=bb')
            cursor = cnxn2.cursor()
            cursor.execute("insert into COM_SmsSent_3  ( MessageID,  MessageContent, ExtendCode,  DestinationAddress,  SendType,       SendTime,         IsWapPush,         WapUrl,         CreateTime    )    VALUES ('%s','%s','%s','%s','%d','%s','%d','%s','%s')"  % (      '1', '10.200.8.253 is down!','NULL',  '15088256320', 0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0,'NULL', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     ))
            cnxn2.commit()
            cnxn2.close()            #
#        if os.system('ping -l 1000 10.200.196.199')>0:
            #alarm.system has been down

#            cnxn2 = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=10.200.198.9;DATABASE=OpenMas;UID=aa;PWD=bb')
#            cursor = cnxn2.cursor()
#            cursor.execute("insert into COM_SmsSent_3  ( MessageID,  MessageContent, ExtendCode,  DestinationAddress,  SendType,       SendTime,         IsWapPush,         WapUrl,         CreateTime    )    VALUES ('%s','%s','%s','%s','%d','%s','%d','%s','%s')"  % (      '1', '10.200.196.199 is down!','NULL',  '15088256320', 0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0,'NULL', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     ))
#            cnxn2.commit()
#            cnxn2.close()            #
        if os.system('ping -l 1000 10.200.196.198')>0:
            #alarm.system has been down

            cnxn2 = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=10.200.198.9;DATABASE=OpenMas;UID=aa;PWD=bb')
            cursor = cnxn2.cursor()
            cursor.execute("insert into COM_SmsSent_3  ( MessageID,  MessageContent, ExtendCode,  DestinationAddress,  SendType,       SendTime,         IsWapPush,         WapUrl,         CreateTime    )    VALUES ('%s','%s','%s','%s','%d','%s','%d','%s','%s')"  % (      '1', '10.200.196.198 is down!','NULL',  '15088256320', 0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0,'NULL', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     ))
            cnxn2.commit()
            cnxn2.close()            #
        if os.system('ping -l 1000 10.200.196.200')>0:
            #alarm.system has been down

            cnxn2 = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=10.200.198.9;DATABASE=OpenMas;UID=aa;PWD=bb')
            cursor = cnxn2.cursor()
            cursor.execute("insert into COM_SmsSent_3  ( MessageID,  MessageContent, ExtendCode,  DestinationAddress,  SendType,       SendTime,         IsWapPush,         WapUrl,         CreateTime    )    VALUES ('%s','%s','%s','%s','%d','%s','%d','%s','%s')"  % (      '1', '10.200.196.200 is down!','NULL',  '15088256320', 0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0,'NULL', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     ))
            cnxn2.commit()
            cnxn2.close()            #

            
                #       
        ########################################################

        net2=os.popen('c:\python27\python net2.py ','r')
        net3=1
        for eachLine in net2:
            #alarm.system has been down
            if len(eachLine.rstrip().split("=")[1])>0 :
                net3=net3+1

        if net3<3 :                       
            time.sleep(1800)
            net4=os.popen('c:\python27\python net2.py ','r')
            net5=1
            for eachLine in net4:
            #alarm.system has been down
                if len(eachLine.rstrip().split("=")[1])>0 :
                    net5=net5+1

            if net5<3 :                       

            
                cnxn2 = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=10.200.198.9;DATABASE=OpenMas;UID=aa;PWD=bb')
                cursor = cnxn2.cursor()
                cursor.execute("insert into COM_SmsSent_3  ( MessageID,  MessageContent, ExtendCode,  DestinationAddress,  SendType,       SendTime,         IsWapPush,         WapUrl,         CreateTime    )    VALUES ('%s','%s','%s','%s','%d','%s','%d','%s','%s')"  % (      '1', 'Nagios is down! on'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),'NULL',  '15088256320', 0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0,'NULL', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     ))
                cnxn2.commit()
                cnxn2.close()            #

            
                # 

       
        

        time.sleep(3600)  #1800s=30min


 
