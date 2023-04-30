#!/usr/bin/python3
"""define the router of the app_views blueprint"""

from api.v1.views import app_views
from flask import jsonify, Flask
from models import storage
from werkzeug.exceptions import NotFound


app = Flask(__name__)


@app_views.route('/status', strict_slashes=False)
def get_status():
    """return the status of the app"""
    return jsonify({"status": "OK"})

@app_views.route('/api/v1/stats', strict_slashes=False)
def stats():
    """Retrieves the number of each object by type"""
    return jsonify({
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    })

@app.errorhandler(NotFound)
def not_found(error):
    """Handles 404 errors"""
    return jsonify({'error': 'Not found'}), 404
