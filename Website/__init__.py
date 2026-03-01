from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Mom246800@'

    # ✅ MySQL connection (CHANGE THESE 3 VALUES)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Mom246800%40@localhost/flask_notes_app'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .views import views
    from .auth import auth
    from .models import User, Note

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    with app.app_context():
        db.create_all()   # Creates tables inside MySQL automatically

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)   

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app