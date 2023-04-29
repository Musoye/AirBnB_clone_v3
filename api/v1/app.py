#!/usr/bin/python3
"""The Developnment of a REST API"""

from models import storage
from api.v1.views import app_views
from flask import Flask
import os


app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_app(exc):
    """when the app is close"""
    storage.close()


if __name__ == "__main__":
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = os.environ.get('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)
