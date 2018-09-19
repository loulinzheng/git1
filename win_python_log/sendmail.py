# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.

# -*- coding:utf-8 -*-

import argparse
import smtplib, sys
#from email.MIMEText import MIMEText
from email.mime.text import MIMEText

# you can change this constant to parameters of sendmail
USR_FROM = '  '
USR = '  '
PASSWD = 'dsdzmbbboyjjbjda'

SMTP_SERVER = 'smtp.qq.com'
SMTP_PORT = 587

def sendmail(usr_to, subject, msg, subtype='html'):
    usr_from = USR_FROM
    msg = MIMEText(msg, subtype, _charset='utf-8')
    msg['Subject'] = subject
    msg['To'] = ';'.join(usr_to)
    msg['From'] = usr_from
    server = smtplib.SMTP()
    server.connect(SMTP_SERVER, SMTP_PORT)
    # ONLY for debug
    # server.set_debuglevel(1)
    # if exchange use STARTTLS auth, you need to uncomment next line
    server.starttls() 
    server.login(USR, PASSWD)
    server.sendmail(usr_from, usr_to, msg.as_string())
    server.quit()


if __name__ == '__main__':
    """
    Example:
    python sendmail.py --usr_to mike@mail.com peter@mail.com --subject 'TEST_SUBJECT' --msg 'TEST_MSG'

    Remark:
    1. msg supports HTML and Chinese
    """
    parser = argparse.ArgumentParser(description='parser for senemail')
    parser.add_argument('--usr_to', dest='usr_to', nargs='+', required=True)
    parser.add_argument('--subject', dest='subject', required=True)
    parser.add_argument('--msg', dest='msg', required=True)
    args = parser.parse_args()
    sendmail(usr_to=args.usr_to, subject=args.subject, msg=args.msg)
