import sys
import suds
from suds.client import Client
url='http://    :9080/OpenMasService?wsdl'
c=Client(url)

def sms(phonenumber,text):
    d=c.factory.create('ns4:ArrayOfstring')
    d.string=[phonenumber]
    j=c.service.SendMessage3(d,text,'8','    ','  ')

    
if __name__=='__main__':
    if len(sys.argv)!=3:
        print ('Usage:python need 2 string')
        exit(1)
    phonenumber=sys.argv[1]
    text=sys.argv[2]
    
    sms(phonenumber,text)


    
