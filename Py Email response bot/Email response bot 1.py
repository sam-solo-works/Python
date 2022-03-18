# -*- coding: utf-8 -*-
"""
Created on Fri May 28 14:27:01 2021

@author: ssolmonson
"""

import html2text
import easyimap
import regex
import json
import time

login = "blamk"
password = "Password123"
imapper = easyimap.connect('imap.corporation.com', login, password)

f = open("messages.json")
processed_messages = json.loads(f.read())
f.close()

while True:
    print("searching for command...")
    for mail_id in imapper.listids(limit=100):
        mail = imapper.mail(mail_id)
        body = html2text.html2text(mail.body)
        if re.findall("^IMPORTANT COMMAND", body) \
                and str(mail_id) not in processed_messages:
            subject = mail.title

            message = "Hello!"

            citation = u"> From: " + mail.from_addr + '\n'
            citation += u"> Date: " + mail.date + '\n'
            citation += u"> Body: " + html2text.html2text(mail.body)

            send_email([str(mail.from_addr)], subject, message + "\n\n" + citation)

            processed_messages[str(mail_id)] = {'subject':subject, 'message':message, 'ts':int(time.time())}
            f = open("messages.json","w")
            f.write(json.dumps(processed_messages))
            f.close()
            print(str(mail_id) + " processed!")
    time.sleep(5)