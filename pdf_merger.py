import PyPDF2


def merger(argv):
	if len(argv) < 5:
		print('Option \'converter\' requires at least two files to merge, please read documentation')
	else:
		output = argv[2]
		files = argv[3:]
		print('Merging...')
		merger = PyPDF2.PdfFileMerger()
		merged = 0
		for pdf in files:
			try:
				merger.append(pdf)
				merged = + 1
			except FileNotFoundError:
				print(f'{pdf} does not exist')
		if merged:
			merger.write(f'{output}.pdf')
			print(f'All done! {output}.pdf was created')
		else:
			print('Could not merge any files')
