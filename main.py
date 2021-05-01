import sys

from image_converter import converter

option = sys.argv[1]
if option == 'converter':
	converter(sys.argv)
else:
	print(f'Option \'{option}\' is invalid, please read documentation')
