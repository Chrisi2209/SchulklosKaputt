from flask import Flask 
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

import os
import logging.config

def setup_logging():
    filename  = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),"..","logs/schulkloskaputt.log"))
    dirname = os.path.dirname(filename)

    if not os.path.exists(dirname):
        os.mkdir(dirname)

    global logger

    logger = logging.getLogger("schulkloskaputt")
    logger.level = logging.INFO
    
    file_handler = logging.handlers.RotatingFileHandler(filename, maxBytes=100000000, backupCount=1)
    file_handler.setFormatter(logging.Formatter("%(levelname)-7s %(asctime)s: %(message)s"))
    logger.addHandler(file_handler)

setup_logging()

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from app import routes, models