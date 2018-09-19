
#!/usr/bin/env python
import time
import datetime
import pyodbc
import os


var = 1
while var <= 5 :  # five day is a circle
    if var==5 :
        #clear var to 1
        cnxn2 = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=10.200.198.9;DATABASE=OpenMas;UID=aa;PWD=bb')
        cursor = cnxn2.cursor()
        cursor.execute("insert into COM_SmsSent_3  ( MessageID,  MessageContent, ExtendCode,  DestinationAddress,  SendType,       SendTime,         IsWapPush,         WapUrl,         CreateTime    )    VALUES ('%s','%s','%s','%s','%d','%s','%d','%s','%s')"  % (      '1', 'The system has been running 5 days.'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),'NULL',  '15088256320', 0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0,'NULL', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     ))
        cnxn2.commit()
        cnxn2.close()
        #
        #
        var=1
    else :
        print var
        var=var+1
    for i in range(1,97):#48 * 30 min=24hour=1day   3-1=2
        #test the data
        #print datetime.datetime.now()
        cnxn1 = pyodbc.connect('DRIVER={SQL Server};SERVER=yunmac-pc;DATABASE=jitondata;UID=read;PWD=123456')

        cursor1 = cnxn1.cursor()
        cursor1.execute("SELECT top 1 [devpropid] ,[hisvalue] ,[hisdate] ,[tb] ,[valuedescript]  FROM [JitonData].[dbo].[hisdata_K2001]   order  by  hisdate desc")
        #<pyodbc.Cursor object at 0x027C02C0>
        row1=cursor1.fetchone()

        cursor1.execute("SELECT top 1 [devpropid] ,[hisvalue] ,[hisdate] ,[tb] ,[valuedescript]  FROM [JitonData].[dbo].[hisdata_K2002]    order  by  hisdate desc")
        #<pyodbc.Cursor object at 0x027C02C0>
        row2=cursor1.fetchone()
        cursor1.execute("SELECT top 1 [devpropid] ,[hisvalue] ,[hisdate] ,[tb] ,[valuedescript]  FROM [JitonData].[dbo].[hisdata_K2001]  where    devpropid='K2001001'  order  by  hisdate desc")
        #<pyodbc.Cursor object at 0x027C02C0>
        roww1=cursor1.fetchone()

        cursor1.execute("SELECT top 1 [devpropid] ,[hisvalue] ,[hisdate] ,[tb] ,[valuedescript]  FROM [JitonData].[dbo].[hisdata_K2002]  where    devpropid='K2002001'  order  by  hisdate desc")
        #<pyodbc.Cursor object at 0x027C02C0>
        roww2=cursor1.fetchone()

        cursor1.execute("SELECT top 1 [devpropid] ,[hisvalue] ,[hisdate] ,[tb] ,[valuedescript]  FROM [JitonData].[dbo].[hisdata_UPC01]   where    devpropid='UPC01001'  order  by  hisdate desc")
        ro1=cursor1.fetchone()
        cnxn1.close()  #close datebase 

        if datetime.datetime.now()>row1[2]+datetime.timedelta(0,3600,0) and datetime.datetime.now()>row2[2]+datetime.timedelta(0,3600,0):
            #alarm.system has been down

            #cnxn2 = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=10.200.198.9;DATABASE=OpenMas;UID=aa;PWD=bb')
            #cursor = cnxn2.cursor()
            #cursor.execute("insert into COM_SmsSent_3  ( MessageID,  MessageContent, ExtendCode,  DestinationAddress,  SendType,       SendTime,         IsWapPush,         WapUrl,         CreateTime    )    VALUES ('%s','%s','%s','%s','%d','%s','%d','%s','%s')"  % (      '1', 'The system runs error!','NULL',  '15088256320', 0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0,'NULL', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     ))
            #cnxn2.commit()
            #cnxn2.close()            #
            #
            #
            os.system('taskkill /f /im Server.exe')
            var=0
        else:
            if roww1[1]>27.5 or roww2[1]>27.5 :# 
                #temper is too high
                cnxn2 = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=10.200.198.9;DATABASE=OpenMas;UID=aa;PWD=bb')
                cursor = cnxn2.cursor()
                cursor.execute("insert into COM_SmsSent_3  ( MessageID,  MessageContent, ExtendCode,  DestinationAddress,  SendType,       SendTime,         IsWapPush,         WapUrl,         CreateTime    )    VALUES ('%s','%s','%s','%s','%d','%s','%d','%s','%s')"  % (      '1', 'The temperature is a little high.','NULL',  '15088256320', 0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0,'NULL', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     ))
                cnxn2.commit()
                cnxn2.close()            #
                #       
        #####
            if datetime.datetime.now()>ro1[2]+datetime.timedelta(0,43200,0):
                #ups detective failure
                cnxn2 = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=10.200.198.9;DATABASE=OpenMas;UID=aa;PWD=bb')
                cursor = cnxn2.cursor()
                cursor.execute("insert into COM_SmsSent_3  ( MessageID,  MessageContent, ExtendCode,  DestinationAddress,  SendType,       SendTime,         IsWapPush,         WapUrl,         CreateTime    )    VALUES ('%s','%s','%s','%s','%d','%s','%d','%s','%s')"  % (      '1', 'The ups cannot be detected.','NULL',  '15088256320', 0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0,'NULL', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     ))
                cnxn2.commit()
                cnxn2.close()
            if ro1[1]<200:
                #power input error
                cnxn2 = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=10.200.198.9;DATABASE=OpenMas;UID=aa;PWD=bb')
                cursor = cnxn2.cursor()
                cursor.execute("insert into COM_SmsSent_3  ( MessageID,  MessageContent, ExtendCode,  DestinationAddress,  SendType,       SendTime,         IsWapPush,         WapUrl,         CreateTime    )    VALUES ('%s','%s','%s','%s','%d','%s','%d','%s','%s')"  % (      '1', 'Warning.No Power.','NULL',  '15088256320', 0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 0,'NULL', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     ))
                cnxn2.commit()
                cnxn2.close()
                ###################################################
       
        

        time.sleep(900)  #1800s=30min


 
