import smtplib
import datetime as dt
import random
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Function to send email
def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())

# Main script
now = dt.datetime.now()
week_day = now.weekday()

if week_day == 1:  # Check if today is Tuesday
    try:
        with open("quotes.txt") as quote_file:
            all_quotes = quote_file.readlines()
            quote = random.choice(all_quotes)
    except FileNotFoundError:
        print("No quotes file found")
    else:
        # Email details
        subject = "Tuesday Motivation"
        body = quote
        sender = os.getenv('EMAIL_USER')
        recipients = ["recipient1@gmail.com", "recipient2@gmail.com"]
        password = os.getenv('EMAIL_PASS')

        # Send the email
        send_email(subject, body, sender, recipients, password)
        print("Email sent successfully!")
