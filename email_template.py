import smtplib
from getpass import getpass
from email.message import EmailMessage
from string import Template
from pathlib import Path


def email_template():
	html = Template(Path('assets/index.html').read_text())
	message = EmailMessage()

	message['subject'] = 'You\'ve won 1,000,000 dollars!'

	email_from = input('Gmail User: ')
	email_password = getpass('Password: ')
	email_to = input('To: ')

	message['from'] = email_from
	message['to'] = email_to
	message.set_content(html.substitute(name=email_to), 'html')

	with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.login(email_from, email_password)
		smtp.send_message(message)
		print('All good, boss!')
