import json
import socket
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('-c', '--config', type=str, required=False,
                    help='путь к файлу конфигурации')
args = parser.parse_args()

config = {'host': 'localhost',
          'port': 8008,
          'buffersize': 1024}

if args.config:
    with open(args.config) as file:
        config.update(json.load(file))

host, port = config['host'], config['port']

try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(99)
    print(f'Сервер запущен на {host}:{port}')

    while True:
        client, addr = sock.accept()
        print(f'Подключен клиент {addr[0]}:{addr[1]}')

        receive = client.recv(config['buffersize'])
        print(f'Получено сообщение:\n {receive.decode()}')

        client.send('Ваше сообщение получено'.encode())
        client.close()

except KeyboardInterrupt:
    print('\nСервер остановлен')
