from flask import Flask
from config import Config
from flask_wtf.csrf import CSRFProtect          
csrf = CSRFProtect()

from .routes import global_scope

app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
app.config.from_object(Config)
csrf.init_app(app)                      # Le paso la Instancia de CSRFProtect

app.register_blueprint(global_scope, url_prefix="/")    

