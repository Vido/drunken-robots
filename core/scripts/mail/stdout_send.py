#! /bin/python

import sys
import json
import smtplib


def format_message(config, fp):

    headers = [
        "From: " + config['sender'],
        "Subject: " + config['subject'],
        "To: " + config['recipient'],
        "MIME-Version: 1.0",
        "Content-Type: text/html"
    ]

    body = fp.readlines()    

    return headers + "\r\n\r\n" + body

if __name__ == '__main__':
    
    with open('stdout_send.conf', 'r') as fp:
        config = json.load(fp)

    ip, port = config['smtp_addr']
    sender = config['sender']
    recipient = config['recipient']
    password = config['password']
    mesg = format_message(config, sys.stdin)
    
    session = smtplib.SMTP(ip, port)
    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(sender, password)
 
    session.sendmail(sender, recipient, mesg)
    session.quit()

