import json
import requests
import pprint

# Create users:
def createUser(user):
    url = 'http://localhost:5000/api/v1/users' 
    data = {
        "username":user, 
    }
    data_json = json.dumps(data)
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=data_json, headers=headers)
    return response

def createRule(parameter, threshold, users):
    url = 'http://localhost:5000/api/v1/rules'
    data = {
        "parameter": parameter,
        "threshold": threshold,
        "usernames": users
    }
    data_json = json.dumps(data)
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=data_json, headers=headers)
    return response

def editRule(parameter, threshold, users):
    url = 'http://localhost:5000/api/v1/rules/' + parameter
    print(url)
    data = {
        "parameter": parameter,
        "threshold": threshold,
        "usernames": users
    }
    data_json = json.dumps(data)
    headers = {'Content-type': 'application/json'}
    response = requests.put(url, data=data_json, headers=headers)
    return response

def createEvent(parameter, value):
    url = 'http://localhost:5000/api/v1/events'
    data = {
        "parameter": parameter,
        "value": value
    }
    data_json = json.dumps(data)
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=data_json, headers=headers)
    return response

def getUserAlert(user):
    url = 'http://localhost:5000/api/v1/users/' + user
    print(url)
    response = requests.get(url)
    return response
	
def main():
    response = createUser("rvitorino")
    pprint.pprint(response.json())
    response = createUser("fmonsanto")
    pprint.pprint(response.json())
    response = createUser("andre")
    pprint.pprint(response.json())

    response = createRule("CO", 20000, ["rvitorino", "fmonsanto"])
    pprint.pprint(response.json())

    response = editRule("CO", 25000, ["rvitorino", "fmonsanto"])
    pprint.pprint(response.json())

    response = createEvent("CO", 30000)
    pprint.pprint(response.json())

    response = getUserAlert("fmonsanto")
    pprint.pprint(response.json())
	
	
main()