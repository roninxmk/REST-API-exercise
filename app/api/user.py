from flask import Blueprint, request
from app.model import User
from app.db import session
from flask import jsonify

user = Blueprint('user_api', __name__, url_prefix="/api/v1")


@user.route('/users', methods=['POST'])
def add_user():
    data = request.json
    username = data['username']

    payload = {}

    # Check if username exists
    user = session.query(User).filter(User.username == username).first()
    if user:
        payload['status'] = False
        payload['message'] = 'username %s already exists.' % (username)
        resp = jsonify(payload)
        resp.status_code = 403
        return resp

    try:
        # Add user to database
        new_user = User(username=username)
        session.add(new_user)
        session.commit()
    except:
        # Error saving event to database
        payload['status'] = False
        payload['message'] = 'error creating user.'
        resp = jsonify(payload)
        resp.status_code = 500
        return resp

    # Success response
    payload['status'] = True
    payload['message'] = 'user %s created successfuly.' % (username)
    resp = jsonify(payload)
    resp.status_code = 201
    return resp


@user.route('/users/<string:username>/', methods=['GET'])
def get_user_alert(username):

    payload = {}
    alerts = []

    # Check if username exists
    user = session.query(User).filter(User.username == username).first()
    if not user:
        payload['status'] = False
        payload['message'] = 'username %s does not exist.' % (username)
        resp = jsonify(payload)
        resp.status_code = 404
        return resp

    # Check every event of every rule to see if it exceeds the threshold
    for rule in user.rules:
        for event in rule.event:
            if event.value > rule.threshold:
                alerts.append({
                    'parameter': rule.parameter,
                    'value': event.value,
                    'threshold': rule.threshold,
                    'timestamp': event.timestamp})

    # Success response
    payload['status'] = True

    # Check if there is any alert
    if not alerts:
        payload['message'] = 'no alerts for the user %s.' % (username)
    else:
        payload['message'] = 'alerts for the user %s.' % (username)
        payload['alerts'] = alerts
    resp = jsonify(payload)
    resp.status_code = 200
    return resp
