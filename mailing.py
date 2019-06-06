import smtplib
import ssl
import os

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_prices(prices):
    """Send an email containing the json file with headset's prices."""
    port = 465  # port for ssl conneciton
    subject = "Oculus prices"
    body = "This an automated email from a Python script"
    sender_email = os.environ.get('OCULUS_MAIL')
    receiver_email = os.environ.get('OCULUS_MAIL')
    password = os.environ.get('OCULUS_PASS')

    # create a secure ssl context
    context = ssl.create_default_context()

    # create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email

    # Add body to the email
    message.attach(MIMEText(body, "plain"))
    filename = 'prices.json'
    filepath = '/Users/MateuszGrzybek/Desktop/oculus/prices.json'

    with open(filepath, "r") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to the server using SSL and send the data
    print("Sending an e-mail...")
    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
