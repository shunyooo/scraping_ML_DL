# TinyDBを使うためライブラリのインポート
from tinydb import TinyDB, Query

# データベースに接続
filepath = "test-tynydb.json"
db = TinyDB(filepath)

# 既存のデータがあれば破棄
db.purge_table('fruits')

# テーブルを得る
table = db.table('fruits')

# データをデータベースに挿入
table.insert( {'name': 'Banana', 'price': 600} )
table.insert( {'name': 'Orange', 'price': 1200} )
table.insert( {'name': 'Mango', 'price': 840} )

# 全データを抽出して表示
print(table.all())

# 特定のデータを抽出して表示
# Orangeを検索
Item = Query()
res = table.search(Item.name == 'Orange')
print('Orange is ', res[0]['price'])

# 値段が800円以上のものを抽出
print("800円以上のもの:")
res = table.search(Item.price >= 800)
for it in res:
    print("-", it['name'])

