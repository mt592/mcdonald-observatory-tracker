'''Create desired message and send email.'''
import smtplib
from tracker import extract_info as ei

def send_new_pr():
    '''Evaluate whether or not new press release exists.'''
    updated = False
    
    f = open("./ref/latest_pr.txt", "r")
    previous_pr = f.read(8)
    f.close()

    soup = ei.set_page_source('news/releases')
    current_pr = ei.get_release_max_date(soup)
    
    if current_pr != previous_pr:
        f = open('./ref/latest_pr.txt', 'w').close()
        f = open("./ref/latest_pr.txt", "w")
        f.write(current_pr)
        f.close()
        updated = True
    return updated

def concat_message():
    '''Concatenates open status and press release messages.'''
    obs_open = ei.is_open()
    if send_new_pr():
        show_pr = ei.get_latest_pr()
        return obs_open + show_pr
    return obs_open
    
def send_email(user, password, recipient, subject, body):
    '''Sends email.'''
    PASS= password
    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, PASS)
        server.sendmail(FROM, TO, message)
        server.close()
        print('Successfully sent mail')
    except:
        print("Failed to send mail")