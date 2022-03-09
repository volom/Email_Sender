# The code is written based on https://python.plainenglish.io/how-to-send-email-with-python-705cce2bce38

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import re
import os

import signal
from functools import wraps


def timeout(timeout_secs: int):
    def wrapper(func):
        @wraps(func)
        def time_limited(*args, **kwargs):
            # Register an handler for the timeout
            def handler(signum, frame):
                raise Exception(f"Timeout for function '{func.__name__}'")

            # Register the signal function handler
            signal.signal(signal.SIGALRM, handler)

            # Define a timeout for your function
            signal.alarm(timeout_secs)

            result = None
            try:
                result = func(*args, **kwargs)
            except Exception as exc:
                raise exc
            finally:
                # disable the signal alarm
                signal.alarm(0)

            return result

        return time_limited

    return wrapper


@timeout(100)
def send_email(passcode, from_, to, subject, content, attachment_path):
    # create message
    msg = MIMEMultipart()
    #msg = MIMEText(content)
    text = MIMEText(content)
    msg.attach(text)
    msg['Subject'] = subject
    
    # msg attachment
    filename = re.split(r'\\|/', attachment_path)[-1]
    _subtype=re.split(r'\.', attachment_path)[-1]
    if _subtype == 'pdf':
        try:
            with open(attachment_path, "rb") as attachment:
                p = MIMEApplication(attachment.read(),_subtype=_subtype)	
                p.add_header('Content-Disposition', f"attachment; filename={filename}") 
                msg.attach(p)
        except Exception as e:
            print(str(e))
    elif _subtype in ['jpeg', 'png']:
        try:
            with open(attachment_path, 'rb') as f:
                img_data = f.read()
                image = MIMEImage(img_data, name=os.path.basename(attachment_path))
                msg.attach(image)
        except Exception as e:
            print(str(e))

    # connection to the server
    conn = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465) #smtp.gmail.com for gmail get password in the same way
    conn.ehlo()
    conn.login(from_, passcode)

    # send message
    conn.sendmail(from_, to, msg.as_string())
    conn.quit()
