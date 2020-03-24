import datetime
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# импорт модуля из файла find_athlete.py

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







def convert_date(date):

    parts = date.birthdate.split("-")
    date_parts = map(int, parts)
    date = datetime.date(*date_parts)
    return date


def find_athlete_birthday(athletes, correct_date):
    """
    функция для поиска ближайшего атлета по дате рождения к
    юзеру
    """
    min_birthd = None
    id = 0
    birthday = ""
    for athlete in athletes:

        athlete_birthday = convert_date(athlete)
        a = abs(correct_date - athlete_birthday)

        if min_birthd is None or min_birthd >= a:
            min_birthd = a
            id = athlete.id
            birthday = athlete.birthdate
    return print("Ближайший по дате рождения атлет: ", id,"- родился", birthday)

def find_athlete_height(athletes, height_usr):
    """
    функция для поиска ближайшего атлета по росту
    """
    height_usr = float(height_usr)
    height = None

    id = 0
    athlet_height = float

    for athlete in athletes:
        height_diff = abs(height_usr - athlete.height)
        if height is None or height >= height_diff:
            height = height_diff
            id = athlete.id
            athlet_height = athlete.height

    return print("Ближайший по росту атлет: ", id, "- рост",athlet_height)

def main():

    db = connect_db(DB_PATH)
    checks = db.query(Users).all()

    id = int(input("Введите id юзера для поиска: "))
    check_id = [check.id for check in checks]

    if id in check_id:

        user_name = db.query(Users).filter(Users.id == id).first()
        correct_date = convert_date(user_name)
        height = str(user_name.height)


        athletes = db.query(Athelete).filter(Athelete.height).all()

        find_athlete_birthday(athletes, correct_date)

        find_athlete_height(athletes, height)
        input("Всё прошло гладко!!")
    else:
        input("Попробуйте сново!")
        main()

if __name__ == "__main__":
    main()


