from csv_manager.parser import CsvToObject

dataset = CsvToObject('example.csv', True).parse()

for key, item in dataset.items():
	print(item)