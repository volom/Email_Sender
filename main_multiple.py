import time
import random
from send_mail import *
import os
import pandas as pd

import telebot

# telegram bot check
@timeout(20)
def sent_msg2bot(txt):
    try:
        bot = telebot.TeleBot('bot_token')
        @bot.message_handler(content_types=['text'])
        def get_text_message(message):
            bot.send_message('user_id', txt)
        get_text_message('send')
    except:
        pass
#


email_address1 = ''     
passcode1 = '' 

email_address2 = ''     
passcode2 = '' 

email_address3 = ''     
passcode3 = '' 

email_address4 = ''     
passcode4 = '' 

email_address5 = ''     
passcode5 = '' 

email_address6 = ''     
passcode6 = '' 


# in this version attachment types can be only .pdf, .jpeg, .png
attachmentPath = f"{os.getcwd()}//python.jpeg"

# read text of email
txt_mail = open(f"{os.getcwd()}//text_mail.txt", 'r').read()

df = pd.read_csv("recipients.txt")

# filter already sent
sent = pd.read_csv('mails.sent.txt')
sent = list(sent.iloc[:,0])
df = df[df[df.columns[0]].isin(sent)==False]


count = 1

def run():
    global count
    index = 1
    for email in list(df.iloc[:,0]):
        email = email.replace('\n', '')
        if index == 1:
            for i in range(2):
                try:
                    send_email(passcode1, email_address1, email, 'SUBJECT', txt_mail, attachmentPath)
                    with open('mails.sent.txt', 'a') as r:
                        r.write(f'{email}\n')
                    print(f"Sent email from {email_address1} to {email}")
                    print(f"Emails sent | {count}")
                    print(f"---------------------")
                    try:
                        sent_msg2bot(f"Sent email from {email_address1} to {email}")
                    except:
                        pass
                    count += 1
                    break
                except Exception as e:
                    print(str(e))
                    try:
                        sent_msg2bot(str(e))
                    except:
                        pass
                    time.sleep(5)
                    continue
            time.sleep(random.randint(20, 25))
            index += 1
        elif index == 2:
            for i in range(2):
                try:
                    send_email(passcode2, email_address2, email, 'SUBJECT', txt_mail, attachmentPath)
                    with open('mails.sent.txt', 'a') as r:
                        r.write(f'{email}\n')
                    print(f"Sent email from {email_address2} to {email}")
                    print(f"Emails sent | {count}")
                    print(f"---------------------")
                    try:
                        sent_msg2bot(f"Sent email from {email_address2} to {email}")
                    except:
                        pass
                    count += 1
                    break
                except Exception as e:
                    print(str(e))
                    try:
                        sent_msg2bot(str(e))
                    except:
                        pass
                    time.sleep(5)
                    continue
            time.sleep(random.randint(20, 25))
            index += 1               
        elif index == 3:
            for i in range(2):
                try:
                    send_email(passcode3, email_address3, email, 'SUBJECT', txt_mail, attachmentPath)
                    with open('mails.sent.txt', 'a') as r:
                        r.write(f'{email}\n')
                    print(f"Sent email from {email_address3} to {email}")
                    print(f"Emails sent | {count}")
                    print(f"---------------------")
                    try:
                        sent_msg2bot(f"Sent email from {email_address3} to {email}")
                    except:
                        pass
                    count += 1
                    break
                except Exception as e:
                    print(str(e))
                    try:
                        sent_msg2bot(str(e))
                    except:
                        pass
                    time.sleep(5)
                    continue
            time.sleep(random.randint(20, 25))
            index += 1  
        elif index == 4:
            for i in range(2):
                try:
                    send_email(passcode4, email_address4, email, 'SUBJECT', txt_mail, attachmentPath)
                    with open('mails.sent.txt', 'a') as r:
                        r.write(f'{email}\n')
                    print(f"Sent email from {email_address4} to {email}")
                    print(f"Emails sent | {count}")
                    print(f"---------------------")
                    try:
                        sent_msg2bot(f"Sent email from {email_address4} to {email}")
                    except:
                        pass
                    count += 1
                    break
                except Exception as e:
                    print(str(e))
                    try:
                        sent_msg2bot(str(e))
                    except:
                        pass
                    time.sleep(5)
                    continue
            time.sleep(random.randint(20, 25))
            index += 1
        elif index == 5:
            for i in range(2):
                try:
                    send_email(passcode5, email_address5, email, 'SUBJECT', txt_mail, attachmentPath)
                    with open('mails.sent.txt', 'a') as r:
                        r.write(f'{email}\n')
                    print(f"Sent email from {email_address5} to {email}")
                    print(f"Emails sent | {count}")
                    print(f"---------------------")
                    try:
                        sent_msg2bot(f"Sent email from {email_address5} to {email}")
                    except:
                        pass
                    count += 1
                    break
                except Exception as e:
                    print(str(e))
                    try:
                        sent_msg2bot(str(e))
                    except:
                        pass
                    time.sleep(5)
                    continue
            time.sleep(random.randint(20, 25))
            index += 1  
        elif index == 6:
            for i in range(2):
                try:
                    send_email(passcode6, email_address6, email, 'SUBJECT', txt_mail, attachmentPath)
                    with open('mails.sent.txt', 'a') as r:
                        r.write(f'{email}\n')
                    print(f"Sent email from {email_address6} to {email}")
                    print(f"Emails sent | {count}")
                    print(f"---------------------")
                    try:
                        sent_msg2bot(f"Sent email from {email_address6} to {email}")
                    except:
                        pass
                    count += 1
                    break
                except Exception as e:
                    print(e)
                    time.sleep(5)
                    continue
            time.sleep(random.randint(20, 25))
            index = 1  
        try:    
            sent_msg2bot(f"Emails sent | {count}")
        except:
            pass
                
if __name__ == "__main__":
    run()
    
    
