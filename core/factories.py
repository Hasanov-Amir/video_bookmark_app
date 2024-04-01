import sys
import logging

from flask import jsonify, Flask
from flask.logging import default_handler

from core.extensions import db, ma, migrator
from app.data import models as _models


class SettingsError(Exception):
    def __init__(self):
        self.message = "Invalid setting"
        super().__init__(self.message)


settings = {
    "development": "core.settings.DevelopmentConfig",
    "production": "core.settings.ProductionConfig",
    "default": "core.settings.DevelopmentConfig"
}


def get_config(setting):
    if settings.get(setting, False):
        return settings.get(setting)
    raise SettingsError()


def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)
    migrator.init_app(app)


def register_logger(app):
    log_formatter = logging.Formatter(
        "[%(asctime)s] - %(levelname)s - %(name)s - %(message)s"
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(log_formatter)

    if app.config["DEBUG"]:
        handler.setLevel(logging.DEBUG)
    else:
        handler.setLevel(logging.INFO)

    app.logger.addHandler(handler)
    app.logger.removeHandler(default_handler)


def register_error_handlers(app):
    def create_error_handler(status_code, message):
        def error_handler(error):
            return jsonify(message=message), status_code
        return error_handler

    app.register_error_handler(400, create_error_handler(400, "Bad request"))
    app.register_error_handler(401, create_error_handler(401, "Unathorized"))
    app.register_error_handler(403, create_error_handler(403, "Forbidden"))
    app.register_error_handler(404, create_error_handler(404, "Not found"))


def create_app(config_name="default"):
    config_obj = get_config(config_name)

    flask_app = Flask(__name__)
    flask_app.config.from_object(config_obj)
    flask_app.app_context().push()

    register_logger(flask_app)
    register_extensions(flask_app)
    register_error_handlers(flask_app)

    return flask_app