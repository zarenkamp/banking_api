import os
from flask_swagger_ui import get_swaggerui_blueprint


class BaseConfig:
    JSON_SORT_KEYS = False

    # swagger config
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.yaml'

    SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': 'Internal Banking API'
        }
    )


class LocalConfig(BaseConfig):
    ENV = 'local'
    DEBUG = True
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    ENV = 'dev'
    DEBUG = True


class ProductionConfig(BaseConfig):
    ENV = 'prod'
    DEBUG = False


class Testing(BaseConfig):
    ENV = 'testing'
    DEBUG = True
    # This creates an in-memory sqlite db
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


config = {
    'testing': Testing,
    'local': LocalConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

