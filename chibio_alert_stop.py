import time
import re
import smtplib
from email.message import EmailMessage

# Email settings
sender_email = "sending@yourmail.com"
receiver_email = "receiving@yourmail.com"
password = "yourpassword"  # Consider using an app-specific password
smtp_server = "smtp-mail.outlook.com"
smtp_port = 587  # Usually 587 for TLS or 465 for SSL

# Path to your PuTTY log file
log_file_path = "C:/Users/youruser/Downloads/ssh_log/chibio.log"

# The specific message you're looking for
specific_message = "Shutting down: Master"

def send_email_alert():
    msg = EmailMessage()
    with open(log_file_path, 'r') as file:
        msg.set_content("Alert: Chibio has stopped working! Log file is attached\n\n"+file.read())
    msg['Subject'] = "Chibio Stop Alert"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Start TLS encryption
        server.login(sender_email, password)
        server.send_message(msg)

def check_for_message():
    with open(log_file_path, 'r') as file:
        content = file.read()
        if re.search(specific_message, content):
            return True
    return False

def main():
    while True:
        if check_for_message():
            send_email_alert()
            break
        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    main()
