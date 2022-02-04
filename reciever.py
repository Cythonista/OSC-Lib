from OscServerWrapper.OscServer import OscBlockingServer
from OscServerWrapper.OscServer import OscThreadingServer
from OscServerWrapper.OscServer import OscForkingServer


def main():
    # OscBlockingServer
    oscServer = OscBlockingServer('127.0.0.1', 6700, '/address')
    oscServer.startServer()
    oscServer.stopServer()

    # OscThreadingServer
    # oscServer = OscThreadingServer('127.0.0.1', 6700, '/address')
    # oscServer.startThread()
    # oscServer.stopThread()

    # OscThreadingServer
    # oscServer = OscForkingServer('127.0.0.1', 6700, '/address')
    # oscServer.startThread()
    # oscServer.wait(5)
    # oscServer.stopThread()


if __name__ == '__main__':
    main()
