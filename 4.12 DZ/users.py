import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_PATH = "sqlite:///sochi_athletes.sqlite3"
# создаём переменную которая подключает наш класс к базе
Base = declarative_base()


def connect_db(path):
    """
    Функиця подключения к сессии
    """
    engine = sa.create_engine(path)
    # Base.metadata.create_all(engine)
    Sessions = sessionmaker(engine)
    session = Sessions()
    return session

class Users(Base):
    """
    описываем таблицу юзеров, для последующей
    работы с ним (добавление новых пользователей)
    """
    __tablename__ = "user"

    id = sa.Column(sa.INTEGER, primary_key=True)

    first_name = sa.Column(sa.TEXT)
    last_name = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    email = sa.Column(sa.TEXT)
    birthdate = sa.Column(sa.TEXT)
    height = sa.Column(sa.REAL)


def request_data():
    first_name = input("Введите ваше имя: ")
    last_name = input("Введите вашу фамилию: ")
    gender = input("Введите ваш пол: ")
    email = input("Введите ваш email: ")
    birthdate = input("Введите вашу дату рождения ГГГГ-ММ-ДД: ")
    height = input("Введите ваш рост m.cm: ")

    user = Users(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=height
    )
    return user


def main():


    db = connect_db(DB_PATH)
    new_user = request_data()
    db.add(new_user)
    db.commit()

    input("Пользователь успешно добавлен.")


if __name__ == "__main__":
    main()
