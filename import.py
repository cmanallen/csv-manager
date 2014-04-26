class CsvToObject(object):
	
	def __init__(self, csv, heading):
		self.csv = csv
		self.heading = heading

	def convert(self):
		rows = self.csv.read().split('\n')
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

		escaped = []
		character_stack = []

		j = 0
		for character in string:
			if not escaped and character == '"':
				escaped.append(character)
				character_stack.append(character)

			elif escaped and character == '"':
				escaped.pop()
				character_stack.append(character)

			elif not escaped and character == ',':
				column = ''.join(character_stack)
				character_stack[:] = []

				if head is not None:
					column_object[head[j]] = column
				else:
					column_object[j] = column

				j += 1

			elif escaped and character == ',':
				character_stack.append(character)

			else:
				character_stack.append(character)

		column = ''.join(character_stack)

		if head is not None:
			column_object[head[j]] = column
		else:
			column_object[j] = column

		return column_object


test = CsvToObject(open('example.txt'), True).convert()
print(test)