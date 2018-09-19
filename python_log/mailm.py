import sys
import smtplib
import string
def Mail(TO,SUBJECT,text):
    HOST="smtp.qq.com"
    FROM="24760080@qq.com"
    BODY='\r\n'.join((
     "From:%s"%FROM,
     "To:%s"%TO,
     "Subject:%s"%SUBJECT,
     "",
     text
     ))
    server=smtplib.SMTP(host="smtp.qq.com",port=587)
    server.ehlo()
    server.starttls()
    server.login("24760080@qq.com","dsdzmbbboyjjbjda")
    server.sendmail(FROM,[TO],BODY)
    server.quit()

if __name__=='__main__':
    if len(sys.argv)!=4:
        print ('Usage:python need 3 string')
        exit(1)
    TO=sys.argv[1]
    SUBJECT=sys.argv[2]
    text=sys.argv[3]
    Mail(TO,SUBJECT,text)


    
