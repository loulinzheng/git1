#!/usr/bin/python3
# -*- coding: utf-8 -*- 
# Cisco ASA Firewall - Syslog Server by neo
# logged in from
# link status is DOWN.
# failed to log in from
# Author: neo<openunix@163.com>

import logging
import socketserver
import threading
import re
import mailm
import smsm
#import sys

#reload( sys )

#sys.setdefaultencoding('gbk')


LOG_FILE = '/var/log/asa5550.log'

logging.basicConfig(level=logging.INFO,
                    format='%(message)s',
                    datefmt='',
                    filename=LOG_FILE,
                    filemode='a')

class SyslogUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        a='logged in from'
        b='link status is DOWN.'
        c='failed to log in from'
        o='link status is down'
        d='S4624'
        e='S682'
        f='F4625error'
        g='F529'
        data = self.request[0].strip()
        socket = self.request[1]
        if (str(data).find(a)>1 or str(data).find(b)>1 or str(data).find(c)>1 or  str(data).find(o)>1 ):
 
            print( "%s : " % self.client_address[0], str(data))
            logging.info(self.client_address[0]+':'+str(data))
            smsm.sms('15088256320',self.client_address[0]+':'+str(data))
#        socket.sendto(data.upper(), self.client_address)
        elif ( str(data).find(d)>1 or str(data).find(e)>1 or str(data).find(f)>1 or str(data).find(g)>1  ):
            print( "%s : " % self.client_address[0], str(data))
            logging.info(self.client_address[0]+':'+str(data))
            m='[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
            n=str(data)
            l=re.search(m,n)
#           w=self.client_address[0]+':'+str(data)
            if l:
                y=n[l.start():l.end()]

                w=self.client_address[0]+':'+str(data)
            
                mailm.Mail('184832806@qq.com',y,w)




if __name__ == "__main__":
    try:
        HOST, PORT = "0.0.0.0", 514
        server = socketserver.UDPServer((HOST, PORT), SyslogUDPHandler)
        server.serve_forever(poll_interval=0.5)
    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        print ("Crtl+C Pressed. Shutting down.")
