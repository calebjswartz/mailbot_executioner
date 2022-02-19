import imaplib, email
import pprint
import time

# credentials go here
USER = ''
PASSWORD = ''
IMAP_SERVER = 'imap.gmail.com'
IMAP_PORT = 993
TIMER = 5

def get_mail():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(USER, PASSWORD)
    
# open the drafts folder
    mail.select('[Gmail]/Drafts')
    resp_code, mails = mail.search(None, 'ALL')

# get the email
    for mail_id in mails[0].decode().split()[-2:]:
        resp_code, mail_data = mail.fetch(mail_id, '(RFC822)')
        message = email.message_from_bytes(mail_data[0][1])

# get body of message
    with open("command.txt", "w")as command_file:
        for payload in message.get_payload():
            command_file.write(payload.get_payload())
        command_file.close()
        edit()

def edit():
    end_msg = "parsekillhere = 0\n" # this message goes at end of script in email
    with open("command.txt", "r") as command_file:
        line_list = []
        for line in command_file:
            line_list.append(line)
            if line == end_msg:
                break
        command_file.close()
# write list back to file
    with open("command.txt", "w") as command_file: 
        command_file.writelines(line_list)
        command_file.close()
    execute()

# execute commands from email
def execute():
    with open("command.txt", "r") as command_file:
        commands = command_file.readlines()
        for command in commands:
            exec(command)
    delete()

# delete the email
def delete():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(USER, PASSWORD)
    mail.select('[Gmail]/Drafts')
    resp_code, mails = mail.search(None, 'ALL')
    for num in mails[0].split():
        mail.store(num, '+FLAGS', '\\Deleted')
    mail.expunge()
    mail.logout()
# optional code to delete command file
#    command_file = open("command.txt", "w")
#    command_file.write("This message overwrites saved commands.")
#    command_file.close()
    wait()
    
# this function starts the process after time specified in seconds with TIMER constant              
def wait():
    time.sleep(TIMER)
    get_mail()

wait()