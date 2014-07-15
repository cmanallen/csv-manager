class Writer(object):
	def __init__(self, dictionary, heading):
		self.dictionary = dictionary
		self.heading = heading

	def write(self, filename):
		csv = ''
		for num, row in self.dictionary.items():
			stringify_row = ''
			if num == 0 and self.heading:
				for head in row:
					stringify_row += head + ','
				stringify_row += '\n'
			for head, column in row.items():
				if type(column) is str:
					column = '"' + column + '"'
				stringify_row += column + ','
			csv += stringify_row + '\n'
		
		with open(filename + '.csv', 'w+') as csv_file:
			csv_file.write(csv)

		return filename + '.csv'