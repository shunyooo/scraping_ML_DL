from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class items(Base):
	"""テーブルの定義"""
	__tablename__ = 'items'

	id = Column(Integer, primary_key=True)
	name = Column(Text)
	price = Column(Integer)


if __name__ == "__main__":
	# MySQLに接続。
	url = 'mysql+mysqldb://root:passward@localhost/test?charset=utf8'
	engine = create_engine(url, echo=True)

	engine.execute('DROP TABLE IF EXISTS {}'.format("items"))

	# テーブル作成
	Base.metadata.create_all(engine)

	# セッションの作成
	Session = sessionmaker(bind=engine)
	session = Session()

	data = [("Banana", 300),("Mango" , 640),("Kiwi"  , 280)]
	item_list = [items(name=d[0],price=d[1]) for d in data]

	session.add_all(item_list)

	for row in session.query(items).all():
	 	print(row.id,row.name,row.price)

	session.commit()

