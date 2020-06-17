import configparser
from tracker import sending_email as se
from tracker import extract_info as ei

config = configparser.ConfigParser()
config.read('./ref/config.ini')

if __name__ == '__main__':
    se.send_email(config['email_sender']['email'],
                  config['email_sender']['secret_key'],
                  config['email_recipient']['email'],
                  "McDonald Observatory Tracker", 
                  se.concat_message())