from flask import Flask
from flask.ext.login import LoginManager
from pony.orm import Database

app = Flask(__name__)
app.secret_key = '67298adb-e195-4a8a-8385-ac6b0a3fa73b'
app.config['SESSION_TYPE'] = 'filesystem'

# jinja extension
app.jinja_env.add_extension("jinja2.ext.with_")

login_manager = LoginManager()
login_manager.init_app(app)
# login_manager.login_view = 'login'

db = Database('sqlite', 'dev-db', create_db=True)

if True:
    import matchMeUp.controllers.admin_controller
    import matchMeUp.controllers.image_controller
    import matchMeUp.controllers.login_controller
    import matchMeUp.controllers.match_controller
    import matchMeUp.controllers.messages_controller
    import matchMeUp.controllers.profile_controller
    import matchMeUp.controllers.match_settings_controller
