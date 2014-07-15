from csv_manager.parser import Parser
from csv_manager.writer import Writer

dataset = Parser('example.csv', True).parse()
csv_file = Writer(dataset, True).write('myfile')


print(csv_file)