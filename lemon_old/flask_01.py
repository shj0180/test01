# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
# if __name__ == '__main__':
#     app.run()

########## GEMINI行情接口 ##########
## https://api.gemini.com/v1/pubticker/:symbol

import json
import requests

gemini_ticker = 'https://api.gemini.com/v1/pubticker/{}'
symbol = 'btcusd'
btc_data = requests.get(gemini_ticker.format(symbol)).json()
print(json.dumps(btc_data, indent=4))

########## 输出 ##########
#
# {
#    "bid": "8825.88",
#    "ask": "8827.52",
#    "volume": {
#        "BTC": "910.0838782726",
#        "USD": "7972904.560901317851",
#        "timestamp": 1560643800000
#    },
#    "last": "8838.45"
# }