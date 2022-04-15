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


@app_views.route('/states/<state_id>')
def get_state(state_id):
    """Retrieves a State object based onstate_id, raises a 404 error
    if state_id is not linked to any State object"""
    state = [state for state in states if state['id'] == state_id]
    if len(state) == 0:
        abort(404)
    return jsonify(state[0])


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """Deletes a State Object"""
    state = [state for state in states if state['id'] == state_id]
    if len(state) == 0:
        abort(404)
    states.remove(state[0])
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'])
def add_state():
    """creates a State"""
    if not request.get_json(force=True, silent=True):
        return ("Not a JSON\n", 400)
        # return (jsonify(error="Not a JSON"), 404)
    if 'name' not in request.get_json():
        return ("Missing name\n", 400)
        # return (jsonify(message="Missing name"), 404)
    request_data = request.get_json()
    new_state = State(name=request_data['name'])
    states.append(new_state.to_dict())
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """updates a state"""
    state = [state for state in states if state['id'] == state_id]
    if len(state) == 0:
        abort(404)
    if not request.get_json(force=True, silent=True):
        return ("Not a JSON\n", 400)
    request_data = request.get_json()
    request_data.pop('id', None)
    request_data.pop('created_at', None)
    request_data.pop('updated_at', None)
    state[0].update(request_data)
    state[0].save()
    return jsonify(state[0]), 200
