import time
import random
from send_mail import send_email
import os

# email_address = str(input("Put your yahoo address here "))
# passcode = str(input("Put your special code here "))
email_address = ''     # add email address here
passcode = '' #special password to your accound generate in settings https://login.yahoo.com/?done=https%3A%2F%2Flogin.yahoo.com%2Fmyaccount%2Fsecurity%2F%3F.scrumb%3D0&src=mc

# in this version attachment types can be only .pdf, .jpeg, .png
attachmentPath = f"{os.getcwd()}//python.jpeg"

# read text of email
txt_mail = open(f"{os.getcwd()}//text_mail.txt", 'r').read()

count = 0

def run():
    global count
    with open("recipients.txt", 'r') as f:
        for email in f:
            email = email.replace('\n', '')
            try:
                send_email(passcode, email_address, email, 'SUBJECT', txt_mail, attachmentPath)
                time.sleep(random.randint(3, 10))
                print(f"Sent email to {email}")
                print(f"Emails sent | {count}")
                print(f"---------------------")
                count += 1
            except Exception as e:
                print(e)

if __name__ == "__main__":
    run()