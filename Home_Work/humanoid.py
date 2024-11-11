import random
from datetime import datetime, timedelta


class Human:
    def __init__(self, name, surname, patronymic, birthdate):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.birthdate = birthdate

    def __str__(self):
        return f"{self.name} {self.surname} {self.patronymic}, born on {self.birthdate.strftime('%d.%m.%Y')}"

    def get_age(self):
        return datetime.now().year - self.birthdate.year


names = ["Иван", "Петр", "Сидор", "Сергей"]
surnames = ["Иванов", "Петров", "Сидоров", "Сергеев"]
patronymics = ["Иванович", "Петрович", "Сидорович", "Сергеевич"]

errors_count = 0
added_people_count = 0
people_dict = {}


def add_person_to_dict(name, surname, patronymic, birthdate):
    global errors_count, added_people_count

    person_key = f"{surname} {name[0]}. {patronymic}"

    if person_key in people_dict:
        print(f"Человек с ФИО '{person_key}' уже существует в словаре.")
        errors_count += 1
    else:
        new_person = Human(name, surname, patronymic, birthdate)
        people_dict[person_key] = new_person
        print(f"Добавлен новый человек: {new_person}")
        print(f"Возраст: {new_person.get_age()} лет")
        added_people_count += 1


def generate_random_person():
    min_year = 1943
    max_year = 2023

    # Генерация случайного года рождения
    birth_year = random.randint(min_year, max_year)

    # Генерация случайной даты внутри выбранного года
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Предполагаем, что месяц имеет не более 28 дней

    # Создание даты рождения
    birthdate = datetime(birth_year, month, day)

    return random.choice(names), random.choice(surnames), random.choice(patronymics), birthdate


while True:
    try:
        name, surname, patronymic, birthdate = generate_random_person()
        add_person_to_dict(name, surname, patronymic, birthdate)

        if errors_count == 4:
            break
    except Exception as e:
        print(f"Ошибка при генерации человека: {str(e)}")
        errors_count += 1

print(f"\nВсего добавлено людей: {added_people_count}")
print(f"Количество ошибок добавления: {errors_count}")