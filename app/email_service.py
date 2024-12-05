
# # this is the app/email_service.py file...

# # LOCAL DEV (ENV VARS)

# import os
# from dotenv import load_dotenv
# import requests

# load_dotenv() # looks in the ".env" file for env vars

# #SENDGRID_SENDER_ADDRESS = os.getenv("SENDGRID_SENDER_ADDRESS")
# #SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
# MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
# #MAILGUN_SENDER_ADDRESS = os.getenv("MAILGUN_SENDER_ADDRESS")


# # HELPER FUNCTION:

# def send_simple_message():
#   	return requests.post(
#   		"https://api.mailgun.net/v3/sandboxc3ccbf1aded84501bf14655a1262af6c.mailgun.org/messages",
#   		auth=("api", "MAILGUN_API_KEY"),
#   		data={"from": "Excited User <mailgun@sandboxc3ccbf1aded84501bf14655a1262af6c.mailgun.org>",
#   			"to": ["bar@example.com", "YOU@sandboxc3ccbf1aded84501bf14655a1262af6c.mailgun.org"],
#   			"subject": "Hello",
#   			"text": "Testing some Mailgun awesomeness!"})



