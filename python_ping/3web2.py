# -*- coding: utf-8 -*-
# @Time    : 2017/10/14 16:54
# @Author  : 蛇崽
# @Email   : 643435675@QQ.com
# @File    : FlaskTest.py
from flask import Flask
from flask import request
import pyodbc
#b='abc'
#c=20
app = Flask(__name__)

#@app.route('/',methods=['GET','POSt'])
#def home():
#    return '<h1>Home</h1>'

@app.route('/signin',methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
    <p><input name="username"></p>
    <p><input name="password" type="password"></p>
    <p><button type="submit">Sign In </button></p>
    </form>
    '''

@app.route('/signin',methods=['POST'])
def signin():
    if request.form['username'] == '   ' and request.form['password'] == '    ':
        #return '<h3>Hello ,admin!</h3>'
        #a=1234
        #return '<h3>%s%s%d%d</h3>'%('123',b,c,a)
        cnxn1 = pyodbc.connect('DRIVER={SQL Server};SERVER=yunmac-pc;DATABASE=jitondata;UID=read;PWD=123456')
        cursor1 = cnxn1.cursor()

        cursor1.execute("SELECT top 1 [devpropid] ,[hisvalue] ,[hisdate] ,[tb] ,[valuedescript]  FROM [JitonData].[dbo].[hisdata_K2001]  where    devpropid='K2001001'  order  by  hisdate desc")
        roww1=cursor1.fetchone()
        cursor1.execute("SELECT top 1 [devpropid] ,[hisvalue] ,[hisdate] ,[tb] ,[valuedescript]  FROM [JitonData].[dbo].[hisdata_K2002]  where    devpropid='K2002001'  order  by  hisdate desc")
        roww2=cursor1.fetchone()
        cursor1.execute("SELECT top 1 [devpropid] ,[hisvalue] ,[hisdate] ,[tb] ,[valuedescript]  FROM [JitonData].[dbo].[hisdata_K2001]  where    devpropid='K2001002'  order  by  hisdate desc")
        rows1=cursor1.fetchone()
        cursor1.execute("SELECT top 1 [devpropid] ,[hisvalue] ,[hisdate] ,[tb] ,[valuedescript]  FROM [JitonData].[dbo].[hisdata_K2002]  where    devpropid='K2002002'  order  by  hisdate desc")
        rows2=cursor1.fetchone()

        cursor1.execute("SELECT top 1 [devpropid] ,[hisvalue] ,[hisdate] ,[tb] ,[valuedescript]  FROM [JitonData].[dbo].[hisdata_UPC01]   where    devpropid='UPC01001'  order  by  hisdate desc")
        ro1=cursor1.fetchone()

        cnxn1.close()


        return '<h3>%s      %s<br>%s      %s<br>%s<br>%s</h3>'%(roww1[1],rows1[1],roww2[1],rows2[1],ro1[1],ro1[2])
    return '<h3>Bad username or password</h3>'


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
        )
