from time import sleep
from asyncio import get_event_loop
from threading import Thread
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
from pythonosc.osc_server import ThreadingOSCUDPServer
from pythonosc.osc_server import ForkingOSCUDPServer

class OscServerBase(object):
    def __init__(self, ip = None, port = None, address = None):
        self.ip = ip
        self.port = port
        self.address = address
        self.dispatcher = Dispatcher()

    def getIp(self):
        return self.ip

    def getPort(self):
        return self.port

class OscBlockingServer(OscServerBase):
    def __init__(self, ip = None, port = None, address = None):
        super().__init__(ip, port, address)
        self.dispatcher.map(self.address, print)
        self.server = BlockingOSCUDPServer((self.ip, self.port), self.dispatcher)

    def startServer(self):
        print('OscBlockingServer Start IP:{} PORT:{}'.format(self.ip, self.port))
        self.server.serve_forever()

class OscThreadingServer(OscServerBase):
    def __init__(self, ip = None, port = None, address = None):
        super().__init__(ip, port, address)
        self.dispatcher.map(self.address, print)
        self.server = ThreadingOSCUDPServer((self.ip, self.port), self.dispatcher)
        self.thread = Thread(target=self.server.serve_forever)

    def startThread(self):
        print('OscThreadingServer Start IP:{} PORT:{}'.format(self.ip, self.port))
        self.thread.start()

    def wait(self, num):
        sleep(num)

    def stopThread(self):
        self.server.shutdown()

class OscForkingServer(OscServerBase):
    def __init__(self, ip = None, port = None, address = None):
        super().__init__(ip, port, address)
        self.dispatcher.map(self.address, print)
        self.server = ForkingOSCUDPServer((self.ip, self.port), self.dispatcher)
        self.thread = Thread(target=self.server.serve_forever)

    def startThread(self):
        print('OscForkingServer Start IP:{} PORT:{}'.format(self.ip, self.port))
        self.thread.start()

    def wait(self, num):
        sleep(num)

    def stopThread(self):
        self.server.shutdown()
