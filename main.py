import sys

from email_sender import email_sender
from image_converter import converter
from pdf_merger import merger
from pdf_watermarker import watermarker

option = sys.argv[1]
if option == 'converter':
	converter(sys.argv)
elif option == 'merger':
	merger(sys.argv)
elif option == 'watermarker':
	watermarker(sys.argv)
elif option == 'email':
	email_sender(sys.argv)
else:
	print(f'Option \'{option}\' is invalid, please read documentation')
