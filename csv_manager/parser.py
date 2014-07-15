class Parser(object):
	def __init__(self, csv, heading):
		self.csv = csv
		self.heading = heading

	def parse(self):
		loaded_file = open(self.csv).read()
		return self._file_to_object(loaded_file)

	def _file_to_object(self, csv):
		rows = csv.split('\n')
		row_object = {}
		
		if self.heading:
			head = rows[0].split(',')
			del[rows[0]]
		else:
			head = None

		i = 0
		for row in rows:
			row_object[i] = self._string_to_object(row, head)
			i += 1

		return row_object

	def _string_to_object(self, string, head):
		column_object = {}
		character_list = []
		escaped = False

		j = 0
		for character in string:
			if not escaped and character == '"':
				escaped = True
				character_list.append(character)
			elif escaped and character == '"':
				escaped = False
				character_list.append(character)
			elif not escaped and character == ',':
				column = ''.join(character_list)
				character_list = []
				if head is not None:
					column_object[head[j]] = column
				else:
					column_object[j] = column				
				j += 1
			elif escaped and character == ',':
				character_list.append(character)
			else:
				character_list.append(character)

		column = ''.join(character_list)
		
		if head is not None:
			column_object[head[j]] = column
		else:
			column_object[j] = column

		return column_object