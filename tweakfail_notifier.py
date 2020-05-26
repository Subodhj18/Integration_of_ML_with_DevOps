#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "svjadhav1818@gmail.com"
host_pass = "****"
guest_address = "svjadhav7799@gmail.com"
subject = "REGARDING FAILURE OF tweak.py"
content = """\<html>
  <head></head>
  <body>
    <p style="color: red;"><h2>Hello, 
		Developer this is an email regarding to your last commit. It seems that your tweak.py file is not working properly please check it once and recommit.</h2>
			THANK YOU</p>
  </body>
</html>"""
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'html'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Successfully sent your mail')

