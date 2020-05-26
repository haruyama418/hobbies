import requests


url = "https://notify-api.line.me/api/notify"
api_token = "SZrru0e25Z84YJs9e9ffLSjZqzy4cjrgrDAxwPThIiq" # ここは先ほど発行したトークン
headers = {"Authorization": "Bearer " + api_token}

message = '今日は3件の予定があります'
payload = {'message': message}
r = requests.post(url, headers=headers, params=payload)
