from flask import Flask
from flask.ext.login import LoginManager

from pony.orm import Database

app = Flask(__name__)
app.secret_key = '67298adb-e195-4a8a-8385-ac6b0a3fa73b'
app.config['SESSION_TYPE'] = 'filesystem'

login_manager = LoginManager()
login_manager.init_app(app)
# login_manager.login_view = 'login'

db = Database('sqlite', 'dev-db', create_db=True)


import matchMeUp.controllers.login_controller
import matchMeUp.controllers.match_controller
