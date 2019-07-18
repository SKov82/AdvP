import csv
import json
import yaml
from pprint import pprint

# Необходимые и достаточные условия
# Реализовать скрипт для чтения/записи данных в формате csv

with open('data/read.csv', 'r') as file:
    data = csv.reader(file)
    # pprint(list(data))

data = (['header1', 'header2', 'header3', 'header4'],
        ['data1', 'data2', 'data3', 'data4'],
        ['data1', 'data2', 'data3', 'data4'],
        ['data1', 'data2', 'data3', 'data4'])

with open('data/write.csv', 'w') as file:
    csv.writer(file, quoting=csv.QUOTE_NONNUMERIC).writerows(data)

# Реализовать скрипт для чтения/записи данных в формате json

with open('data/read.json', 'r') as file:
    data = json.load(file)
    # pprint(data)

data = [{'header': 'data1', 'header2': 'data2', 'header3': 'data3'},
        {'header': 'data1', 'header2': 'data2', 'header3': 'data3'},
        {'header': 'data1', 'header2': 'data2', 'header3': 'data3'},
        {'header': 'data1', 'header2': 'data2', 'header3': 'data3'}]

with open('data/write.json', 'w') as file:
    json.dump(data, file, sort_keys=True)

# Реализовать скрипт для чтения/записи данных в формате yaml

with open('data/read.yml', 'r') as file:
    data = yaml.load(file)
    # pprint(data)

data = ({'attr1': 'value1', 'attr2': 'value2',
         'attr3': 'value3', 'attr4': ['value1', 'value2', 'value3']})

with open('data/write.yml', 'w') as file:
    yaml.dump(data, file)

# Реализовать скрипт для преобразования данных в формате csv в формат json

with open('data/read.csv', 'r') as file:
    data = list(csv.reader(file))
    data = dict(zip(data[0], data[1:]))

with open('data/csv_to_json.json', 'w') as file:
    json.dump(data, file, indent=2)

# Реализовать скрипт для преобразования данных в формате csv в формат yaml

with open('data/read.csv', 'r') as file:
    data = list(csv.reader(file))
    data = dict(zip(data[0], data[1:]))

with open('data/csv_to_yaml.yml', 'w') as file:
    yaml.dump(data, file)

# Реализовать скрипт для преобразования данных в формате json в формат yaml

with open('data/read.json', 'r') as file:
    data = json.load(file)

with open('data/json_to_yaml.yml', 'w') as file:
    yaml.dump(data, file)
