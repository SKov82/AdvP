import json
import socket
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('-c', '--config', type=str, required=False,
                    help='путь к файлу конфигурации')
args = parser.parse_args()

config = {'host': '127.0.0.1',
          'port': 8008,
          'buffersize': 1024}

if args.config:
    with open(args.config) as file:
        config.update(json.load(file))

host, port = config['host'], config['port']

try:
    sock = socket.socket()
    sock.connect((host, port))
    print('Соединение установлено')

    msg = input('Введите сообщение: ')

    sock.send(msg.encode())
    print(f'Отправлено сообщение:\n {msg}')

    receive = sock.recv(config['buffersize'])
    print(f'Сообщение от сервера:\n {receive.decode()}')
except KeyboardInterrupt:
    print('\nКлиент остановлен')
