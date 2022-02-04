from OscClientWrapper.OscClient import OscClient
from OscClientWrapper.OscClient import OscSimpleClient


def main():
    # OscClient
    oscClient = OscClient('127.0.0.1', 6700, '/address')
    oscClient.addMessage('abc')
    oscClient.build()
    oscClient.send()

    # OscSimpleClient
    oscClient = OscSimpleClient('127.0.0.1', 6700, '/address')
    oscClient.send('def')

if __name__ == '__main__':
    main()
