from OscClientWrapper import OscClient


def main():
    # OscClient
    oscClient = OscClient.OscClient('127.0.0.1', 6700, '/address')
    oscClient.addMessage('abc')
    oscClient.build()
    oscClient.send()

    # OscSimpleClient
    oscClient = OscClient.OscSimpleClient('127.0.0.1', 6700, '/address')
    oscClient.send('def')

if __name__ == '__main__':
    main()
