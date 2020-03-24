import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# импорт модуля из файла find_athlete.py
from find_athlete import convert_date, find_athlete_birthday, find_athlete_height

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


class Athelete(Base):
    """
    Описывает таблицу атлетов, будем брать из неё
    данные для вывода
    """
    __tablename__ = "athelete"

    id = sa.Column(sa.INTEGER, primary_key=True)

    age = sa.Column(sa.INTEGER)
    birthdate = sa.Column(sa.TEXT)
    gender = sa.Column(sa.TEXT)
    height = sa.Column(sa.INTEGER)
    name = sa.Column(sa.Text)
    weight = sa.Column(sa.INTEGER)
    gold_medals = sa.Column(sa.INTEGER)
    silver_medals = sa.Column(sa.INTEGER)
    bronze_medals = sa.Column(sa.INTEGER)
    total_medals = sa.Column(sa.INTEGER)
    sport = sa.Column(sa.TEXT)
    country = sa.Column(sa.TEXT)


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
    choise = input("Выберите вариант:\n1 - создаб пользователя\n2 - найти 2-х атлетов похожих на Юзера\n")

    db = connect_db(DB_PATH)
    if choise == "1":


        new_user = request_data()
        db.add(new_user)
        db.commit()

    elif choise == "2":
        id = input("Введите id юзера для поиска: ")
        user_name = db.query(Users).filter(Users.id == id).first()
        correct_date = convert_date(user_name)
        height = str(user_name.height)


        athletes = db.query(Athelete).filter(Athelete.height).all()

        find_athlete_birthday(athletes, correct_date)

        find_athlete_height(athletes, height)

if __name__ == "__main__":
    main()
