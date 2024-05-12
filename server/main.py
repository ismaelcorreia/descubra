import os
# App Initialization
from connection.connection_alq import db
from flask import Flask, jsonify, request, url_for, send_from_directory
from routes.config_routes import register_routes
from urllib.parse import quote

from flask_cors import CORS,  cross_origin
# from sqlalchemy.orm import DeclarativeBase
from config.config import config
from connection.connection_alq import db

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.config.from_object(config[os.getenv('CONFIG_MODE')])
db.init_app(app)
    

PORT = os.getenv('PORT')
HOST = os.getenv('HOST')


register_routes(app)

# Specify the directory to serve files from
file_directory = os.environ.get("UPLOAD_PATH")


@app.route('/')
def index():
    return f'server: {HOST}:{PORT}'


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()

    return len(defaults) >= len(arguments)


@app.route("/site-map-all")
def site_map_routes():
    routes = []

    for rule in app.url_map.iter_rules():
        if has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            routes.append((url, rule.endpoint))
    print(routes)
    return routes


# File Server
@app.route('/api/images/<filename>', methods=['GET'])
def get_image(filename):
    # images_directory = os.path.join(app.root_path, 'images')

    # Check if the file exists
    file_path = os.path.abspath(os.path.join(file_directory, filename))
    if os.path.exists(file_path):
        # Return the image file
        return send_from_directory(os.path.dirname(file_path), filename)
    else:
        # Return a JSON response if the file is not found
        return jsonify({'error': 'Image not found'}), 404


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create tables
        # db.init_app(app)
    app.run(port=PORT, host='0.0.0.0', debug=True)
