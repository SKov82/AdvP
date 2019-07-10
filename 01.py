import chardet


def codec(obj, code, do=1):
    return obj.encode(code) if do else obj.decode(code)


strings = ('разработка', 'сокет', 'декоратор')
codes = ('utf-8', 'cp1251', 'cp866')  # , 'latin-1')

for code in codes:
    for string in strings:
        byte = codec(string, code)
        print(byte, type(byte), chardet.detect(byte)['encoding'])

        string = codec(byte, code, 0)
        print(string, type(string), '\n')
