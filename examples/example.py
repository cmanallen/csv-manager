from csv_manager.parser import CsvToObject

dataset = CsvToObject(open('example.csv'), True).convert()
for key, value in dataset.items():
	print(value['Close'])