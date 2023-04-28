#!/usr/bin/python3
"""The Developnment of a REST API"""

from models import storage
from api.v1.views import app_views
from flask import Flask
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_app():
    """when the app is close"""
    storage.close()


if __name__ == "__main__":
    host = getenv(HBNB_API_HOST) if getenv(HBNB_API_HOST) else "0.0.0.0"
    port = getenv(HBNB_API_PORT) if getenv(HBNB_API_PORT) else 50000
    app.run(host=host, port=port, threaded=True)
