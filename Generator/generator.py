import random

from Data.data import Person

from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(20,50),
        department=faker_ru.job(),
        salary=random.randint(1000,5000),

        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),

        mobile = faker_ru.msisdn(),
        birth_date=faker_ru.date(),

    )

def generated_file():
    path=rf'C:\Users\user\AquaProjects\AutoTestingPython\filetest{random.randint(0,999)}.txt'
    file=open(path, "w+")
    file.write(f'Hello World{random.randint(0,999)} , but path {path}, by Alex')
    file.close()
    return file.name, path
