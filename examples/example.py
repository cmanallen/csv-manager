from csv_manager.parser import CsvToObject

dataset = CsvToObject('example.csv', True).parse()
# for key, value in dataset.items():
	# print(value)

for key, item in dataset.items():
	print(item)