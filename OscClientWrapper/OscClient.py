from pythonosc.udp_client import UDPClient
from pythonosc.udp_client import SimpleUDPClient
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

    def addMessage(self, message = None):
        # 送信するメッセージを追加
        self.builder.add_arg(message)

    def build(self):
        # 送信するメッセージをビルドして格納
        self.data = self.builder.build()

    def send(self):
        # ビルドしたデータを送信
        self.client.send(self.data)


class OscSimpleClient(OscClientBase):
    def __init__(self, ip = None, port = None, address = None):
        super().__init__(ip, port, address)
        self.client = SimpleUDPClient(self.ip, self.port)

    def send(self, message = None):
        # メッセージを格納して送信
        self.client.send_message(self.address, message)
