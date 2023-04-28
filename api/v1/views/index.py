#!/usr/bin/python3
"""define the router of the app_views blueprint"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def get_status():
    """return the status of the app"""
    return jsonify({"status": "OK"})
