
from pprint import pprint

def  custom_write(file_name, strings):
        file_name = 'test.txt'
        file = open(file_name, 'w', encoding='utf-8')
        strings_positions = {}
        number = 1
        for string in strings:
            strings_positions[(number, file.tell())] = string
            file.write(string + '\n')
            number += 1
        file.close()
        return strings_positions





info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']
result = custom_write('test.txt', info)
for elem in result.items():
 print(elem)
