from flask import Flask
from flask.ext.openid import OpenID

app = Flask(__name__)
app.config.from_object('config')

from app import views#, models
