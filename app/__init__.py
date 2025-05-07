from flask import Flask
import os

def create_app():
    app = Flask(__name__, static_url_path='/editor/static')
    app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), '..', 'saved_files')
    from . import routes
    app.register_blueprint(routes.bp, url_prefix='/editor')
    return app
