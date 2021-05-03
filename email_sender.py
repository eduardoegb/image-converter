import smtplib
from getpass import getpass
from email.message import EmailMessage
import consts


def email_sender(argv):
	message = EmailMessage()

	email_from = consts.email_from
	email_to = consts.email_to
	email_subject = 'Testing Python!'
	email_content = 'I am a Python Master!'

	if len(argv) > 5:
		email_content = argv[5]
	if len(argv) > 4:
		email_subject = argv[4]
	if len(argv) > 3:
		email_to = argv[3]
	if len(argv) > 2:
		email_from = argv[2]

	message['from'] = email_from
	message['to'] = email_to
	message['subject'] = email_subject
	message.set_content(f'{email_content}')

	email_user = input('User: ')
	email_password = getpass('Password: ')

	with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.login(email_user, email_password)
		smtp.send_message(message)
		print('All good, boss!')