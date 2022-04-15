#!/usr/bin/python3
"""
view for State objects that handles all default RESTFul API actions
"""
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.user import User

users = []
users_dict = storage.all(User)
for k, v in users_dict.items():
    users.append(v.to_dict())


@app_views.route('/users')
def get_users():
    """Retrieves the list of all User objects """
    return jsonify(users)


@app_views.route('/users/<user_id>')
def get_user(user_id):
    """Retrieves a User object based on user_id, raises a 404 error
    if user_id is not linked to any User object"""
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    return jsonify(user[0])


@app_views.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Deletes a User Object"""
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    users.remove(user[0])
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'])
def add_user():
    """creates a User"""
    if not request.get_json(force=True, silent=True):
        return ("Not a JSON\n", 400)
        # return (jsonify(error="Not a JSON"), 404)
    if 'name' not in request.get_json():
        return ("Missing name\n", 400)
        # return (jsonify(message="Missing name"), 404)
    request_data = request.get_json()
    new_user = User(name=request_data['name'])
    users.append(new_user.to_dict())
    return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """updates a user"""
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    if not request.get_json(force=True, silent=True):
        return ("Not a JSON\n", 400)
        # return (jsonify(error="Not a JSON"), 400)
    request_data = request.get_json()
    request_data.pop('id', None)
    request_data.pop('created_at', None)
    request_data.pop('updated_at', None)
    user[0].update(request_data)
    return jsonify(user[0]), 200
