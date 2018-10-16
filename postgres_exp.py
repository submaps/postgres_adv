import sqlalchemy
from sqlalchemy.orm import mapper
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker

print("version SQLAlchemy:", sqlalchemy.__version__)  # посмотреть версию SQLALchemy
engine = create_engine('sqlite:///:memory:', echo=True)

metadata = MetaData()
users_table = Table('users', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('name', String),
                        Column('fullname', String),
                        Column('password', String)
                    )

metadata.create_all(engine)


class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)


print(mapper(User, users_table))  # и отобразить. Передает класс User и нашу таблицу
user = User("Вася", "Василий", "qwerty")
print(user)  # Напечатает <User('Вася', 'Василий', 'qweasdzxc'>
print(user.id)  # Напечатает None

Session = sessionmaker(bind=engine)

session = Session()
vasiaUser = User("vasia", "Vasiliy Vasiliev", "vasia2000")
session.add(vasiaUser)

ourUser = session.query(User).filter_by(name="vasia").first()
print(ourUser)
