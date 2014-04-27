from csv_to_object import *

dataset = CsvToObject(open('example.csv'), True).convert()
for key, value in dataset.items():
	print(value['Close'])