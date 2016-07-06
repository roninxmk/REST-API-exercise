from flask import Blueprint, request
from ..model import User
from ..db import session
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

    pass
