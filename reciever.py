import time
from pythonosc import osc_server
from pythonosc.dispatcher import Dispatcher

def handler(none, args):
    print('{} {} {} {}'.format(none, args[0], args[1], args[2]))

def main():
    ip = '127.0.0.1'
    port = 6700

    # URLにコールバック関数を割り当てる
    dispatcher = Dispatcher()
    dispatcher.map('/address', handler)
    # サーバを起動する
    server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)
    print('Server Start IP={} PORT={}'.format(ip, port))
    server.serve_forever()


if __name__ == '__main__':
    main()
