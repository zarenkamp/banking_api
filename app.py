import os
from flask import Flask, make_response

from database import db
from init_marshmallow import ma
from api.route.customer_route import customer_route
from api.route.account_route import account_route
from api.route.transfer_route import transfer_route
from config import config
from create_db import create_test_database


def create_app(config_name):
    application = Flask(__name__)
    application.config.from_object(config[config_name])

    db.init_app(application)
    ma.init_app(application)

    application.register_blueprint(customer_route)
    application.register_blueprint(account_route)
    application.register_blueprint(transfer_route)
    application.register_blueprint(application.config['SWAGGER_BLUEPRINT'], url_prefix=application.config['SWAGGER_URL'])

    @application.errorhandler(400)
    def handle_400_error(_error):
        return make_response({'error': 'bad request'}, 400)

    @application.errorhandler(404)
    def handle_404_error(_error):
        return make_response({'error': 'resource not found, check spelling'}, 404)

    @application.errorhandler(405)
    def handle_405_error(_error):
        return make_response({'error': 'method not allowed'}, 405)

    @application.errorhandler(500)
    def handle_500_error(_error):
        return make_response({'error': 'internal error'}, 500)

    if application.config['ENV'] == 'local':
        create_test_database(application)

    return application


flask_env = os.getenv('FLASK_ENV') or 'local'
app = create_app(flask_env)






