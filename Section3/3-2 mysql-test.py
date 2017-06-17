import sqlalchemy as sa

# MySQLに接続。
url = 'mysql+mysqldb://root:passward@localhost/test?charset=utf8'
engine = sa.create_engine(url, echo=True)

# テーブルを作成
engine.execute('''
	CREATE TABLE items (
	item_id INTEGER PRIMARY KEY AUTO_INCREMENT,
	name TEXT, 
	price INTEGER
	)
	''')

# データを挿入。
# SQL文に「?」が使用できないので、代わりに「%s」を使用
ins = "INSERT INTO items (name, price) VALUES (%s, %s)"
data = [("Banana", 300),("Mango" , 640),("Kiwi"  , 280)]
for d in data:
	engine.execute(ins,d)

# データを抽出
rows = engine.execute('SELECT * FROM items')

# 表示
for row in rows:
    print(row)