import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass
import csv


def send_mail(recipient, subject, message_html, mypassword):

    display_name = "Sir Worrall"  # Alter how your email displays to recipient - EDIT
    username = "your.email@outlook.com"  # Alter the email address you send from - EDIT
    password = mypassword

    msg = MIMEMultipart()
    msg["From"] = f"{display_name} <{username}>"
    msg["To"] = recipient
    msg["Subject"] = subject

    part2 = MIMEText(message_html, "html")
    # Add html message to email
    msg.attach(part2)

    filename = "test_data.csv"  # Choose file to attach - EDIT

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
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
    msg.attach(part)

    # Connect to Server and send email
    try:
        print("sending mail to " + recipient + " - subject: " + subject)

        mailServer = smtplib.SMTP(
            "smtp-mail.outlook.com", 587
        )  # EDIT - if not using Microsoft server/account
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(username, password)
        mailServer.sendmail(
            f"{display_name} <{username}>", recipient, msg.as_string()
        )  # N.B., code could be more efficient by looping over csv file here, as then only one connection to the server is needed.
        mailServer.close()

    except error as e:
        print(str(e))


email_subject = "Sending mass emails with Python!"  # EDIT
email_password = getpass("Enter password and hit 'Enter': ")
# email_password = "myPassword" # Uncomment and set password in script for testing purposes

# get the content as html
with open("html_message.html", "r", encoding="utf-8") as reader:
    content = reader.read()


with open("test_data.csv") as file:  # EDIT - for your csv file
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for (
        School,
        Title,
        First_Name,
        Surname,
        Address1,
        Address2,
        City,
        Post_Code,
        Email,
    ) in reader:  # EDIT - to match the number of fields in your csv file

        # adapt content to be specific for each row on the data entry - EDIT according to how you want to replace text in html file
        body = content.replace(
            "SCHOOL NAME HERE", School
        )  # new object created so that template is not overwritten
        body = body.replace(
            "SCHOOL TEACHER NAME", First_Name
        )  # other fields in new object changed too

        print(f"Sending email to {School}")
        send_mail(
            f"{First_Name} {Surname} <{Email}>", email_subject, body, email_password
        )  # Send email using defined function, for each data entry
        # N.B. The first argument of the function (recipient), always requires an email address, but it can be edited to included how you want the contact to be displayed e.g. (DISPLAY NAME <Email>)


# send_mail('recipient@domain_name.com', 'Test', 'Be careful who you send emails to at first!', email_password)

# Script will ask for the password of the email account you are sending from. Your keystrokes will be received, but they won't appear in the console.
