import requests
import json

# APIキーの指定
apikey = "7118df305d5ec83a65f148cc3349e651"

# 天気を調べたい都市の一覧 
cities = ["Tokyo,JP", "London,UK", "New York,US"]
# APIのひな型
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

# 温度変換(ケルビン→摂氏)
k2c = lambda k: k - 273.15

# 各都市の温度を取得する
for name in cities:
    # APIのURLを得る
    url = api.format(city=name, key=apikey)
    # 実際にAPIにリクエストを送信して結果を取得する
    r = requests.get(url)
    # 結果はJSON形式なのでデコードする
    data = json.loads(r.text)    
    # 結果を出力
    print("+ 都市=", data["name"])
    print("| 天気=", data["weather"][0]["description"])
    print("| 最低気温=", k2c(data["main"]["temp_min"]))
    print("| 最高気温=", k2c(data["main"]["temp_max"]))
    print("| 湿度=", data["main"]["humidity"])
    print("| 気圧=", data["main"]["pressure"])
    print("| 風向き=", data["wind"]["deg"])
    print("| 風速度=", data["wind"]["speed"])
    print("")

