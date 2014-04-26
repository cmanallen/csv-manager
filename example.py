from csv_to_object import *

heading_test = CsvToObject(open('example.txt'), True).convert()
print(heading_test)

no_heading = CsvToObject(open('example.txt'), False).convert()
print(no_heading)