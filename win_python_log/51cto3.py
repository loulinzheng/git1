#!/srv/python/bin/python3
# -*- encoding: utf-8 -*-
# Cisco ASA Firewall - Syslog Server by neo
# logged in from
# link status is DOWN.
# failed to log in from
# Author: neo<openunix@163.com>

import logging
import socketserver
import threading

LOG_FILE = './log/asa5550.log'

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
        d='S4624'
        e='4625'
        #data = bytes.decode(self.request[0].strip())
        data=self.request[0].strip()
        socket = self.request[1]
        print( "%s : " % self.client_address[0], data.decode("gbk","ignore"))
        if (str(data).find(a)>1 or str(data).find(b)>1 or str(data).find(c)>1 or str(data).find(d)>1 or str(data).find(e)>1):
 
            #print( "%s : " % self.client_address[0], str(data))
            #logging.info(self.client_address[0]+':'+data.decode('utf-8','strict'))
            logging.info(self.client_address[0]+':'+data.decode("gbk","ignore"))
#        socket.sendto(data.upper(), self.client_address)

if __name__ == "__main__":
    try:
        HOST, PORT = "0.0.0.0", 514
        server = socketserver.UDPServer((HOST, PORT), SyslogUDPHandler)
        server.serve_forever(poll_interval=0.5)
    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        print ("Crtl+C Pressed. Shutting down.")
