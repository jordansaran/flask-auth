"""App Flask"""
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix
from core.settings import Settings


db: SQLAlchemy = SQLAlchemy()


def create_app():
    """"Create app Flask - API"""
    settings: Settings = Settings()
    app: Flask = Flask(__name__)
    migrate: Migrate = Migrate()
    jwt: JWTManager = JWTManager()
    app.config.from_object(settings)
    if settings.debug_is_enabled():
        app.wsgi_app = ProxyFix(app.wsgi_app)

    with app.app_context():
        from api.blueprints import api_bp_pipeline
        app.register_blueprint(api_bp_pipeline)
        db.init_app(app)
        jwt.init_app(app)
        migrate.init_app(app, db)

    return app


if __name__ == '__main__':
    app = create_app()
