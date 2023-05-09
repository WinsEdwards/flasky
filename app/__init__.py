from flask import Flask

# import SQLALCHEMY
from flask_sqlalchemy import SQLAlchemy

# import migrate
from flask_migrate import Migrate

# import libraries for grabbing environment variables
from dotenv import load_dotenv

# import to read environment variables
import os

# gives us access to database operations
db = SQLAlchemy()
migrate = Migrate()

# load the values fom our .env file for os module to use
load_dotenv()

def create_app(test_config=None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    # set up database
    if not test_config:
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    else:
        app.config["TESTING"] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
        # 'postgresql+psycopg2://postgres:postgres@localhost:5432/flasky_development'

    # connect the db and migrate our flask app
    db.init_app(app)
    migrate.init_app(app, db)

    # import routes
    from .routes import crystal_bp

    # register the blueprint
    app.register_blueprint(crystal_bp)

    from app.models.crystal import Crystal
    from app.models.healer import Healer

    return app