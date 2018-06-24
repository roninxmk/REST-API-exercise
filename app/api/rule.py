from flask import Blueprint, request
from app.model import User, Rule
from app.db import session
from flask import jsonify

rule = Blueprint('rule_api', __name__, url_prefix="/api/v1")


@rule.route('/rules', methods=['POST'])
def add_rule():
    data = request.json
    parameter = data['parameter']
    threshold = data['threshold']

    user_list = []
    payload = {}

    # Check if rule exists
    if session.query(Rule).filter(Rule.parameter == parameter).first():
        payload['status'] = False
        payload['message'] = 'parameter %s already exists. Edit the rule instead.' % (parameter)
        resp = jsonify(payload)
        resp.status_code = 403
        return resp

    for username in data['usernames']:
        user = session.query(User).filter(User.username == username).first()

        # Check if all usernames exist
        if user:
            user_list.append(user)

        # If a username does not exist, send an error message
        else:
            payload['status'] = False
            payload['message'] = 'username %s does not exist.' % (username)
            resp = jsonify(payload)
            resp.status_code = 404
            return resp

    try:
        # Add rule to database
        new_rule = Rule(parameter=parameter,
                        threshold=threshold,
                        user=user_list)
        session.add(new_rule)
        session.commit()

    except:
        # Error saving rule to database
        payload['status'] = False
        payload['message'] = 'error creating rule.'
        resp = jsonify(payload)
        resp.status_code = 500
        return resp

    # Success response
    payload['status'] = True
    payload['message'] = 'rule for %s with threshold %d created successfuly.' % (parameter, threshold)
    resp = jsonify(payload)
    resp.status_code = 201
    return resp


@rule.route('/rules/<string:parameter>', methods=['PUT'])
def edit_parameter(parameter):
    data = request.json
    threshold = data['threshold']

    user_list = []
    payload = {}

    # Check if rule exists
    rule = session.query(Rule).filter(Rule.parameter == parameter).first()
    if not rule:
        payload['status'] = False
        payload['message'] = 'parameter %s does not exist.' % (parameter)
        resp = jsonify(payload)
        resp.status_code = 404
        return resp

    for username in data['usernames']:
        user = session.query(User).filter(User.username == username).first()

        # Check if all usernames exist
        if user:
            user_list.append(user)

        # If a username does not exist, send an error message
        else:
            payload['status'] = False
            payload['message'] = 'username %s does not exist.' % (username)
            resp = jsonify(payload)
            resp.status_code = 404
            return resp

    try:
        # Edit rule
        rule.parameter = parameter
        rule.threshold = threshold
        rule.user = user_list
        session.commit()

    except:
        # Error editing rule
        payload['status'] = False
        payload['message'] = 'error editing rule.'
        resp = jsonify(payload)
        resp.status_code = 500
        return resp

    # Success response
    payload['status'] = True
    payload['message'] = 'rule for %s with threshold %d edited successfuly.' % (parameter, threshold)
    resp = jsonify(payload)
    resp.status_code = 200
    return resp
