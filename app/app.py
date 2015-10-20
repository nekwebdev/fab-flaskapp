import os
from flask import Flask

def create_app(config_module=None):
    app = Flask(__name__)
    app.debug = True
    app.config.from_object(config_module or
                           os.environ.get('FLASK_CONFIG') or
                           'config')
    @app.route('/')
    def index():
        return 'Yo world!'

    return app