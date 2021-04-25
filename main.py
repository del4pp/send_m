import smtplib
import email.message
import tempmail
import tolist
import database


def start_send():
    try:
        tolist.get_all_email()
        get_len_list = tolist.get_len_list()
        for i in range(get_len_list):
            msg = email.message.Message()
            msg['Subject'] = tempmail.subject
            msg['From'] = 'alert@creator.com'
            msg['To'] = tolist.all_mail[i]
            password = "password"
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(tempmail.email_content)
            #Server
            s = smtplib.SMTP(host='smtp.server', port=587)
            s.starttls()
            # Login Credentials for sending the mail
            s.login(msg['From'], password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
            #database and i
            print(msg['To'])
            database.addlog(msg['To'])
            i += 1
    except Exception as e:
        print(e)

start_send()