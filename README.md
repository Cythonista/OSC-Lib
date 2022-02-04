# OSC-Lib

OSC通信研究用リポジトリ

```
OscClientWrapper
|
├── OscClient.py
|   ├── OscClientBase   # 基底クラス
|   ├── OscClient       # フルクライアント
|   └── OscSimpleClient # 軽量版クライアント
|
└── sender.py           # クライアント利用プログラム

OscServerWrapper
|
├── OscServer.py
|   ├── OscServerBase      # 基底クラス
|   ├── OscBlockingServer  # プログラムをブロックする半永久的なサーバ
|   ├── OscThreadingServer # マルチスレッドな状態のサーバ
|   ├── OscForkingServer
|   └── OscAsyncServer
|
└── reciever.py            # サーバ利用プログラム
```
