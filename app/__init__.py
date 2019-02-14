#! /usr/bin/env python3

from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
# from config import Config
from werkzeug.contrib.cache import MemcachedCache
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
# app.config.from_object(Config)
# print(app.config['FLASK_APP'])
print(app.config['SECRET_KEY'])
Session(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

# from app import routes