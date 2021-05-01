import PyPDF2


def watermarker(argv):
	if len(argv) < 4:
		print('Option \'watermarker\' requires one file and one water mark, please read documentation')
	else:
		input_path = argv[2]
		wtr_path = argv[3]
		output_path = argv[4]

		template = PyPDF2.PdfFileReader(open(input_path))
		watermark = PyPDF2.PdfFileReader(open(wtr_path))
		writer = PyPDF2.PdfFileWriter()

		for i in range(template.getNumPages()):
			page = template.getPage(i)
			page.mergePage(watermark.getPage(0))
			writer.addPage(page)

		with open(output_path, 'rb') as file:
			writer.write(file)
