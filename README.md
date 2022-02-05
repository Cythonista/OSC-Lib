# OSC-Lib

OSC通信研究用リポジトリ
以下を実行して利用
```
pip install python-osc
```

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
|   └── OscForkingServer   # 重たい処理用
|
└── reciever.py            # サーバ利用プログラム
```
