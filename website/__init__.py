from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .views import views

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "app123"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
    
    from .models import User
    from .auth import auth
    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix= "/")
    
    loginManager = LoginManager()
    loginManager.login_view = "auth.login"
    loginManager.init_app(app)
    
    with app.app_context():
        db.create_all()
        
    @loginManager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    
    return app