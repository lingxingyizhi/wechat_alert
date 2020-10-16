#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys
import email
import wechat_alert


def email_content_parse(file_name):
    fp = open(file_name, "r")
    msg = email.message_from_file(fp)   #返回Message类的实例
    fp.close()
    mail_from = email.utils.parseaddr(msg.get("from"))[1]   #msg.get()是取
    mail_content = ''
    if mail_from == "alert@h3c.com":
        mail_content = msg.get_payload(decode=True).decode("GB18030")
    elif msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                mail_content = str(part.get_payload(decode=True),'utf-8')
                break
            else:
                    mail_content = msg.get_payload(decode=True)
    else:
        mail_content = msg.get_payload(decode=True).decode(mail_charset)
    return mail_from,mail_content


now = str(time.time())
file_name = "/home/ggt/mail_box/" + now
f = open(file_name,"w")
while True:
        line = sys.stdin.readline()
        if not line:
                break
        f.write(line)
f.close()
mail_from,mail_content = email_content_parse(file_name)
wechat_alert.alert_run(mail_from,mail_content)
