#!/usr/bin/python3
"""
view for State objects that handles all default RESTFul API actions
"""
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models import storage
from models.state import State

states = []
states_dict = storage.all(State)
for k, v in states_dict.items():
    states.append(v.to_dict())

@app_views.route('/states')
def get_states():
    """Retrieves the list of all State objects """
    return jsonify(states)

@app_views.route('/states/<id>')
def get_state(id):
    """Retrieves a State object based on id, raises a 404 error
    if id is not linked to any State object"""
    state = [state for state in states if state['id'] == id]
    if len(state) == 0:
        abort(404)
    return jsonify(state[0])

@app_views.route('/states/<id>', methods=['DELETE'])
def delete_state(id):
    """Deletes a State Object"""
    state = [state for state in states if state['id'] == id]
    if len(state) == 0:
        abort(404)
    states.remove(state[0])
    return jsonify({}), 200

@app_views.route('/states', methods=['POST'])
def add_state():
    """creates a State"""
    if not request.get_json(force = True, silent = True):
        return (jsonify(error="Not a JSON"), 404)
    if 'name' not in request.get_json():
        return (jsonify(message="Missing name"), 404)
    request_data = request.get_json()
    new_state = State(name=request_data['name'])
    states.append(new_state.to_dict())
    return jsonify(new_state.to_dict()), 201

def update_state():
    