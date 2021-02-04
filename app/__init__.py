from flask import Flask

# from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# from flask_caching import Cache

# mail = Mail()
db = SQLAlchemy(session_options={"autoflush": False, "autocommit": False})
migrate = Migrate()
# cache = Cache(config={"CACHE_TYPE": "simple"})


def create_app(config_name="default"):
    application = Flask(__name__, instance_relative_config=True)

    # CONFIG
    from config import configs

    application.config.from_object(configs[config_name])

    # APPS
    # mail.init_app(application)
    db.init_app(application)
    migrate.init_app(application, db)
    # cache.init_app(application)

    # LOGGING
    # from .config.config_logging import db_handler, gunicorn_logger

    # application.logger.addHandler(gunicorn_logger)
    # application.logger.addHandler(db_handler)

    # CONTROLLERS
    from .controllers import register_all_controllers  # noqa: F401

    register_all_controllers(application)

    from .controllers import register_error_handlers  # noqa: F401

    register_error_handlers(application)

    # MODULES

    # from .auth import create_module as auth_create_module

    # auth_create_module(application)

    return application
