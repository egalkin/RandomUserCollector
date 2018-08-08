from flask import render_template
from app import app
from app.models import Person
from app.utils import check_first_launch
from flask import request


@app.route('/')
def init_caching():
    check_first_launch()
    return 'Hello World!'


@app.route('/user')
def get_users():
    check_first_launch()
    args = request.args
    query = Person.query
    for k in args:
        if k == 'gender':
            query = query.filter_by(gender=args['gender'])
        if k == 'email':
            query = query.filter_by(email=args['email'])
        if k == 'first_name':
            query = query.filter_by(first_name=args['first_name'].lower())
        if k == 'last_name':
            query = query.filter_by(last_name=args['last_name'].lower())
    persons_list = query.all()
    return render_template('all_users.html', persons_list=persons_list)


@app.route('/user/<id>')
def user(id):
    check_first_launch()
    user = Person.query.filter_by(id=id).first()
    print(user.get_avatar())
    return render_template('user_profile.html', user=user)


if __name__ == '__main__':
    app.run()
