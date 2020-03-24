import datetime


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




