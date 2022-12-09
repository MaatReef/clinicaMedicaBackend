from flask import Flask
from config import Config
from flask_wtf.csrf import CSRFProtect     
from flask_login import login_user, LoginManager, login_required, logout_user, current_user

csrf = CSRFProtect()
login_manager = LoginManager()

from .routes import global_scope
from .routes import delete_scope
from .routes import post_scope
from .routes import edit_scope
from .routes import view_scope
from .routes.errors import page_not_found

app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)

app.config.from_object(Config)
csrf.init_app(app)                      # Le paso la Instancia de CSRFProtect
login_manager.init_app(app)           # Para crear la sesión

app.register_blueprint(global_scope, url_prefix="/")    
app.register_blueprint(delete_scope, url_prefix="/")    
app.register_blueprint(post_scope, url_prefix="/")    
app.register_blueprint(edit_scope, url_prefix="/")    
app.register_blueprint(view_scope, url_prefix="/") 

app.register_error_handler(404, page_not_found) 