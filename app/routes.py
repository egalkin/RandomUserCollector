from flask import render_template
from app import app
from app.models import Person
from app.utils import check_first_launch



@app.route('/')
def init_caching():
    check_first_launch()
    return 'Hello World!'


@app.route('/user')
def get_users():
    check_first_launch()
    persons_list = Person.query.all()
    return render_template('all_users.html', persons_list=persons_list)


@app.route('/user/<id>')
def user(id):
    check_first_launch()
    user = Person.query.filter_by(id=id).first()
    print(user.get_avatar())
    return render_template('user_profile.html', user=user)


if __name__ == '__main__':
    app.run()
