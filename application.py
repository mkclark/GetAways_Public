from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# setup db
db = SQLAlchemy()

def create_app(**config_overrides):
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile('settings.py')

    # apply overrides for tests
    app.config.update(config_overrides)

    # initialize db
    db.init_app(app)
    migrate = Migrate(app, db)

    # import blueprints
    from booking.views import booking_app
    from hosting.views import hosting_app

    # register blueprints
    app.register_blueprint(booking_app)
    app.register_blueprint(hosting_app)

    return app
