# #!/usr/bin/python3
# """
# view for city  objects that handles all default RESTFul API actions
# """
# from api.v1.views import app_views
# from flask import jsonify, abort, request, make_response
# from models import storage
# from models.city import City
# from models.state import State

# states = []
# cities = []
# states_dict = storage.all(State)
# cities_dict = storage.all(City)
# for k, v in states_dict.items():
#     states.append(v.to_dict())
# for k, v in cities_dict.items():
#     cities.append(v.to_dict())
# """for stat in states:
#     for city in stat.cities:
#         cscity.append(city)"""


# @app_views.route('/states/<state_id>/cities')
# def get_states_cities(state_id):
#     nill = []
#     """Retrieves the list of all State objects """
#     state = [state for state in states if state['id'] == state_id]
#     if len(state) == 0:
#         abort(404)
#     for city in cities:
#         if city['state_id'] == state_id:
#             nill.append(city)
#     return jsonify(nill)


# @app_views.route('/cities/<city_id>')
# def get_cities(city_id):
#     """"Retrieves the list of all City objects """
#     city = [city for city in cities if city['id'] == city_id]
#     if len(city) == 0:
#         abort(404)
#     return jsonify(city[0])


# @app_views.route('/cities/<city_id>', methods=['DELETE'])
# def delete_city(city_id):
#     """Deletes a city Object"""
#     city = [city for city in cities if city['id'] == city_id]
#     if len(city) == 0:
#         abort(404)
#     cities.remove(city[0])
#     return jsonify({}), 200


# @app_views.route('/states/<state_id>/cities', methods=['POST'])
# def add_city():
#     """creates a City"""
#     state = [state for state in states if state['id'] == state_id]
#     if len(state) == 0:
#         abort(404)
#     if not request.get_json(force=True, silent=True):
#         return ("Not a JSON\n", 400)
#         # return (jsonify(error="Not a JSON"), 404)
#     if 'name' not in request.get_json():
#         return ("Missing name\n", 400)
#         # return (jsonify(message="Missing name"), 404)
#     request_data = request.get_json()
#     new_city = City(name=request_data['name'], state_id=state_id)
#     cities.append(new_city.to_dict())
#     return jsonify(new_city.to_dict()), 201


# @app_views.route('/cities/<city_id>', methods=['PUT'])
# def update_city(city_id):
#     """updates a city"""
#     city = [city for city in cities if city['id'] == city_id]
#     if len(city) == 0:
#         abort(404)
#     if not request.get_json(force=True, silent=True):
#         return ("Not a JSON\n", 400)
#         # return (jsonify(error="Not a JSON"), 400)
#     request_data = request.get_json()
#     request_data.pop('id', None)
#     request_data.pop('created_at', None)
#     request_data.pop('updated_at', None)
#     city[0].update(request_data)
#     return jsonify(city[0]), 200
