import os.path
from app.models import Person
from app import db


def is_first_launch():
    if not os.path.isfile('isCached'):
        f = open('isCached', 'w+')
        f.close()
        return True
    else:
        return False


def fill_db(data):
    for person in data['results']:
        person_data = dict()
        person_data['gender'] = person['gender']
        person_data['name'] = person['name']
        person_data['email'] = person['email']
        person_data['picture'] = person['picture']['medium']
        new_person = Person(person_data)
        db.session.add(new_person)
        db.session.commit()
