#----------------------------------------------------Getting Email Notifications
load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_EMAIL = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL")
sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)

rom_email = Email(MY_EMAIL)
to_email = Email(MY_EMAIL)
subject = "Example Notification"
message_text = "Hello, \n\nThis is a message from your personal notification service.\n\nCustomize this example notification content to make it useful for you! Maybe weather info? Maybe stock prices? Let your creativity guide you!"
content = Content("text/plain", message_text)
mail = Mail(from_email, subject, to_email, content)

# ISSUE REQUEST (SEND EMAIL)

response = sg.client.mail.send.post(request_body=mail.get())

# PARSE RESPONSE

pp = pprint.PrettyPrinter(indent=4)

print("----------------------")
print("EMAIL")
print("----------------------")
print("RESPONSE: ", type(response))
print("STATUS:", response.status_code) 
print("HEADERS:")
pp.pprint(dict(response.headers))
print("BODY:")
print(response.body) 

#email notification service
