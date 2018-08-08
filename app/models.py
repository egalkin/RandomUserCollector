from app import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(64), index=True)
    firs_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64), index=True)
    avatar_url = db.Column(db.String(255), index=True)

    def __init__(self, person_info):
        self.gender = person_info['gender']
        self.firs_name = person_info['name']['first']
        self.last_name = person_info['name']['last']
        self.email = person_info['email']
        self.avatar_url = person_info['picture']

    def __repr__(self):
        return 'gender : {gender}, first name : {fname}, last name : {lname}, email : {email}'.format(
            gender=self.gender, fname=self.firs_name, lname=self.last_name, email=self.email)

    def get_full_name(self):
        return '{fname} {lname}'.format(fname=self.firs_name, lname=self.last_name).title()

    def get_avatar(self):
        return self.avatar_url
