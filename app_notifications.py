import os
from dotenv import load_dotenv
import sendgrid
from sendgrid.helpers.mail import * # source of Email, Content, Mail, etc.

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_EMAIL_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

# AUTHENTICATE

sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)

# COMPILE REQUEST PARAMETERS (PREPARE THE EMAIL)

from_email = Email(MY_EMAIL_ADDRESS)
to_email = Email(MY_EMAIL_ADDRESS)
subject = "Hello World from the SendGrid Python Library!"
content = Content("text/plain", "Hello, Email!")
mail = Mail(from_email, subject, to_email, content)

# ISSUE REQUEST (SEND EMAIL)

response = sg.client.mail.send.post(request_body=mail.get())

# PARSE RESPONSE

print(response.status_code) 
print(response.body) 
print(response.headers)

#https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/718d10fa22072a56101c20f82229910feb7cbc20/notes/python/packages/sendgrid.md
