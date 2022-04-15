# #!/usr/bin/python3
# """
# view for State objects that handles all default RESTFul API actions
# """
# from api.v1.views import app_views
# from flask import jsonify, abort, request, make_response
# from models import storage
# from models.amenity import Amenity

# amenities = []
# amenities_dict = storage.all(Amenity)
# for k, v in amenities_dict.items():
#     amenities.append(v.to_dict())


# @app_views.route('/amenities')
# def get_amenities():
#     """Retrieves the list of all Amenity objects """
#     return jsonify(amenities)


# @app_views.route('/amenities/<amenity_id>')
# def get_amenity(amenity_id):
#     """Retrieves a amenity object based onstate_id, raises a 404 error
#     if amenity_id is not linked to any Amenity object"""
#     amenity = [amenity for amenity in amenities if amenity['id'] == amenity_id]
#     if len(amenity) == 0:
#         abort(404)
#     return jsonify(amenity[0])


# @app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
# def delete_amenity(amenity_id):
#     """Deletes a amenity Object"""
#     amenity = [amenity for amenity in amenities if amenity['id'] == amenity_id]
#     if len(amenity) == 0:
#         abort(404)
#     amenities.remove(amenity[0])
#     return jsonify({}), 200


# @app_views.route('/amenities', methods=['POST'])
# def add_amenity():
#     """creates a amenity"""
#     if not request.get_json(force=True, silent=True):
#         return ("Not a JSON\n", 400)
#         # return (jsonify(error="Not a JSON"), 404)
#     if 'name' not in request.get_json():
#         return ("Missing name\n", 400)
#         # return (jsonify(message="Missing name"), 404)
#     request_data = request.get_json()
#     new_amenity = Amenity(name=request_data['name'])
#     amenities.append(new_amenity.to_dict())
#     return jsonify(new_amenity.to_dict()), 201


# @app_views.route('/amenities/<amenity_id>', methods=['PUT'])
# def update_amenity(amenity_id):
#     """updates an amenity"""
#     amenity = [amenity for amenity in amenities if amenity['id'] == amenity_id]
#     if len(amenity) == 0:
#         abort(404)
#     if not request.get_json(force=True, silent=True):
#         return ("Not a JSON\n", 400)
#         # return (jsonify(error="Not a JSON"), 400)
#     request_data = request.get_json()
#     request_data.pop('id', None)
#     request_data.pop('created_at', None)
#     request_data.pop('updated_at', None)
#     amenity[0].update(request_data)
#     return jsonify(amenity[0]), 200
