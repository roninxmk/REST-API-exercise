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
	
def main():
    response = createUser("rvitorino")
    pprint.pprint(response.json())
    response = createUser("fmonsanto")
    pprint.pprint(response.json())
    response = createUser("andre")
    pprint.pprint(response.json())

main()