from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)



from app import routes, models
from app.utils import is_first_launch, fill_db
import requests
import json

def init_db():
    if is_first_launch():
        response = requests.get('https://randomuser.me/api/?results=100')
        fill_db(json.loads(response.text))


init_db()