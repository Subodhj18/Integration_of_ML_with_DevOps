#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "svjadhav1818@gmail.com"
host_pass = "nandya@jambhya1234"
guest_address = "svjadhav7799@gmail.com"
subject = "Regarding failure of rebuild.py"
content = '''Hello, 
				Developer this is an email regarding to your last commit. It seems that your tweak.py fileis not working properly please check it once and recommit.
			THANK YOU'''
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Successfully sent your mail')

