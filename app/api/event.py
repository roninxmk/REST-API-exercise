from flask import Blueprint, request
from ..model import Rule, Event
from ..db import session
from flask import jsonify

event = Blueprint('event_api', __name__, url_prefix="/api/v1")


@event.route('/events', methods=['POST'])
def add_event():
    data = request.json
    parameter = data['parameter']
    value = data['value']

    payload = {}

    rule = session.query(Rule).filter(Rule.parameter == parameter).first()
    # Check if rule exists
    if not rule:
        payload['status'] = False
        payload['message'] = 'parameter %s does not exist.' % (parameter)
        resp = jsonify(payload)
        resp.status_code = 404
        return resp

    try:
        new_event = Event(value=value, rule=rule)
        session.add(new_event)
        session.commit()
    except:
        # Error saving event to database
        payload['status'] = False
        payload['message'] = 'error creating event.'
        resp = jsonify(payload)
        resp.status_code = 500
        return resp

    # Success response
    payload['status'] = True
    payload['message'] = 'event for %s with value %d created successfuly.' % (parameter, value)
    resp = jsonify(payload)
    resp.status_code = 201
    return resp
