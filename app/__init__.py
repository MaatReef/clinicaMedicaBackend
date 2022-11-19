from flask import Flask
from config import Config
from flask_wtf.csrf import CSRFProtect     
# from flask_login import LoginManager

csrf = CSRFProtect()
# login_manager = LoginManager()

from .routes import global_scope

app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
app.config.from_object(Config)
csrf.init_app(app)                      # Le paso la Instancia de CSRFProtect
# login_manager.init_app(app)             # Para crear la sesión

app.register_blueprint(global_scope, url_prefix="/")    

