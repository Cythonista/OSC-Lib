from pythonosc.udp_client import UDPClient
from pythonosc.osc_message_builder import OscMessageBuilder

class OscClientBase(object):
    def __init__(self, ip = None, port = None, address = None):
        self.ip = ip
        self.port = port
        self.address = address

    def getIp(self):
        return self.ip

    def getPort(self):
        return self.port

    def getAddress(self):
        return self.address

class OscClient(OscClientBase):
    def __init__(self, ip = None, port = None, address = None):
        super().__init__(ip, port, address)
        self.client = UDPClient(self.ip, self.port)
        self.builder = OscMessageBuilder(address=self.address)
        self.data = None

    def build(self, args):
        self.builder.add_arg(args)
        self.data = self.builder.build()

    def send(self):
        self.client.send(self.data)


class OscSimpleClient(OscClientBase):
    pass
