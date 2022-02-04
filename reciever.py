from OscServerWrapper import OscServer


def main():
    # OscBlockingServer
    # oscServer = OscServer.OscBlockingServer('127.0.0.1', 6700, '/address')
    # oscServer.startServer()
    # oscServer.stopServer()

    # OscThreadingServer
    # oscServer = OscServer.OscThreadingServer('127.0.0.1', 6700, '/address')
    # oscServer.startThread()
    # oscServer.stopThread()

    # OscThreadingServer
    # oscServer = OscServer.OscForkingServer('127.0.0.1', 6700, '/address')
    # oscServer.startThread()
    # oscServer.wait(5)
    # oscServer.stopThread()


if __name__ == '__main__':
    main()
