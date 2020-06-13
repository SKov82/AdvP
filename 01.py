import chardet
import subprocess


# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом
# формате и проверить тип и содержание соответствующих переменных. Затем с
# помощью онлайн-конвертера преобразовать строковые представление в формат
# Unicode и также проверить тип и содержимое переменных.

kit = [
    ['разработка', 'сокет', 'декоратор'],
    ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
     '\u0441\u043e\u043a\u0435\u0442',
     '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']
]

for words in kit:
    for word in words:
        print(type(word), word)

# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без
# преобразования в последовательность кодов (не используя методы encode и
# decode) и определить тип, содержимое и длину соответствующих переменных.

words = [b'class', b'function', b'method']

for word in words:
    print(type(word), word, len(word))

# 3. Определить, какие из слов «attribute», «класс», «функция», «type»
# невозможно записать в байтовом типе.
#  Кириллические не могут.

words = ['attribute', 'класс', 'функция', 'type']

for word in words:
    word = word.encode('utf-8')
    print(type(word), word)

# 4. Преобразовать слова «разработка», «администрирование», «protocol»,
# «standard» из строкового представления в байтовое и выполнить обратное
# преобразование (используя методы encode и decode).


def transform(obj, codec, do=1):
    return obj.encode(codec) if do else obj.decode(codec)


words = ('разработка', 'администрирование', 'protocol', 'standard')
codecs = ('utf-8', 'utf-16', 'cp1251', 'cp866')

for codec in codecs:
    for word in words:
        word = transform(word, codec)
        print(type(word), word, chardet.detect(word)['encoding'])

        word = transform(word, codec, 0)
        print(type(word), word)

# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать
# результаты из байтовового в строковый тип на кириллице.

sources = [
    ['ping', 'yandex.ru'],
    ['ping', 'youtube.com']
]

for source in sources:
    subproc = subprocess.Popen(source, stdout=subprocess.PIPE)
    for row in subproc.stdout:
        print(row.decode('cp866'))

# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор». Проверить кодировку файла
# по умолчанию. Принудительно открыть файл в формате Unicode и вывести его
# содержимое.

with open('test_file.txt', 'w') as file:
    file.writelines(['сетевое программирование\n', 'сокет\n', 'декоратор'])

print(file.encoding)

with open('test_file.txt', 'r', encoding='utf-8') as file:
    print(file.readlines())
