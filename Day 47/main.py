import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


response = requests.get('https://appbrewery.github.io/instant_pot/')


soup = BeautifulSoup(response.text, 'html.parser')

prices1 = str (soup.find('span', class_='a-price-whole').text)
prices2 = str (soup.find('span', class_='a-price-fraction').text)
print(prices1 + prices2)

# Get email credentials from environment variables
from_address = os.getenv('GMAIL_USER')
smtp_password = os.getenv('GMAIL_PASS')
to_address = 'recipient_email@example.com'
subject = 'Test Email from Python'
body = 'Hello, this is a test email sent from a Python script using Gmail.'

# Gmail server details
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Create message container
msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Connect to Gmail's SMTP server and send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_address, smtp_password)
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    print('Email sent successfully')
except Exception as e:
    print(f'Error: {e}')
finally:
    server.quit()