import requests
import smtplib
import os
import paramiko
import linode_api4
import time
import schedule

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
LINODE_TOKEN = os.environ.get('LINODE_TOKEN')


def restart_server_and_container():
    #restart the server (pip install linode-api4)
    print('Rebooting the server.....')
    client = linode_api4.LinodeClient(LINODE_TOKEN)
    nginx_server = client.load(linode_api4.Instance, 24920590)
    nginx_server.reboot()


    #restart the application
    while True:
        nginx_server = client.load(linode_api4.Instance, 24920590)
        if nginx_server.status == 'running':
            time.sleep(5)
            restart_container()
            break


def send_notification(eamil_msg):
    print('Sending an email.......')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls() # securing connection with the external services
                smtp.ehlo() # Identify python application with the mail server
                #smtp.login("chandrakishore93@gmail.com", "khfakjhsakfhk") # Create app password for gmail using https://myaccount.google.com/u/1/apppasswords
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                #smtp.sendmail("sender_email", "receiver_email", "Subject: SITE DOWN \n Application returned {response.status_code}. Fix the issue, Restart the application")
                message = "Subject: SITE DOWN\n{email_msg}"
                smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)


def restart_container():
    print('Restarting the application.......')
    #restart the application
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='192.168.2.32', username='root', key_filename='/Users/kishore/.ssh/id_rsa')
    stdin, stdout, stderr =  ssh.exec_command('docker start <container-id>')
    #print(stdin)
    print(stdout.readlines())
    ssh.close()


def monitor_application():
    try:
        response = requests.get('url')
        #print(response.text)
        #print(response.status_code)
        if response.status_code == 200:
            print(f"Application is running successfully")
        else:
            print(f"Application Down. Fix it!")
            # Send email to me
            msg = f'Application returned {response.status_code}. Fix the issue, Restart the application'
            send_notification(msg)
            #restart the container
            restart_container()        
    except Exception as ex:
        print(f"Connection error happend:{ex}")
        msg = 'Application not accessible at all'
        send_notification(msg)
        #restart the server and container
        restart_server_and_container()



schedule.every(5).minutes.do(monitor_application)

while True:
    schedule.run_pending()