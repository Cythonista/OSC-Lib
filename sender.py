from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder


def main():
    ip = '127.0.0.1'
    port = 6700

    client = udp_client.UDPClient(ip, port)

    args = [0, 228, 122]
    data = OscMessageBuilder(address='/address')
    data.add_arg(args)
    data = data.build()

    client.send(data)


if __name__ == '__main__':
    main()
