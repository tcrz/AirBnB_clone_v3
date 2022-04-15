#!/usr/bin/python3
"""
view for Place  objects that handles all default RESTFul API actions
"""
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.city import City
from models.place import Place
from models.user import User

users = []
users_dict = storage.all(User)
for k, v in users_dict.items():
    users.append(v.to_dict())

places = []
places_dict = storage.all(Place)
for k, v in places_dict.items():
    places.append(v.to_dict())

cities = []
cities_dict = storage.all(City)
for k, v in cities_dict.items():
    cities.append(v.to_dict())


@app_views.route('/cities/<city_id>/places')
def get_cities_of_places(city_id):
    linked_places = []
    """Retrieves the list of all Place objects linked to a City"""
    city = [city for city in cities if city['id'] == city_id]
    if len(city) == 0:
        abort(404)
    for place in places:
        if place['city_id'] == city_id:
            linked_places.append(place)
    return jsonify(linked_places)


@app_views.route('/places/<place_id>')
def get_place(place_id):
    """"Retrieves a Place object"""
    place = [place for place in places if place['id'] == place_id]
    if len(place) == 0:
        abort(404)
    return jsonify(place[0])


@app_views.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    """Deletes a Place object"""
    place = [place for place in places if place['id'] == place_id]
    if len(place) == 0:
        abort(404)
    places.remove(place[0])
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'])
def add_place(city_id):
    """creates a Place (linked to a City by id)"""
    city = [city for city in cities if city['id'] == city_id]
    if len(city) == 0:
        abort(404)
    if not request.get_json(force=True, silent=True):
        return ("Not a JSON\n", 400)
    if 'name' not in request.get_json():
        return ("Missing name\n", 400)
    if 'user_id' not in request.get_json():
        return ("Missing user_id\n", 400)
    else:
        if 'user_id' in request.get_json():
            user = [user for user in users
                    if user['id'] == request.get_json()['user_id']]
            if len(user) == 0:
                abort(404)
    request_data = request.get_json()
    new_place = Place(name=request_data['name'],
                      user_id=request_data['user_id'],
                      city_id=city_id)
    places.append(new_place.to_dict())
    return jsonify(new_place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    """updates a place"""
    place = [place for place in places if place['id'] == place_id]
    if len(place) == 0:
        abort(404)
    if not request.get_json(force=True, silent=True):
        return ("Not a JSON\n", 400)
    request_data = request.get_json()
    request_data.pop('id', None)
    request_data.pop('user_id', None)
    request_data.pop('city_id', None)
    request_data.pop('created_at', None)
    request_data.pop('updated_at', None)
    place[0].update(request_data)
    return jsonify(place[0]), 200
