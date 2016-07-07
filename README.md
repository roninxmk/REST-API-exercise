# REST-API-exercise
REST API exercise for carbon monoxide spike detection

### Exercise
Create a REST API for carbon monoxide spike detection, with 3 main services:
* Create rule: The service should accept the environmental parameter to monitor (e.g. "CO"), alert threshold and users to alert (list of usernames)
* Create event: The service should accept the registered parameter, its value and timestamp
* Get alerts: The service should accept the username and return the registered alerts for that user. Information to be returned:
  * Monitored parameter
  * Registered value
  * Alert threshold
  * Timestamp

There is no need to safeguard user authentication and authorization. The is also no restrictions for the programming language and data storage.

Typical utilization flow for the REST API:
* Create rule for "CO" monitorization, with an alert threshold of 20000 units and alerts to the users "rvitorino, fmonsanto".
* Register 10 eventos for the parameter "CO", with values varying between 10000 and 30000.
* Verify which alerts are registered for the user "fmonsanto".


## Pre requisites
* [Python](http://www.python.org/)
* [Pip](https://pypi.python.org/pypi/pip)
* [MySQL](http://www.mysql.com/)


## Instalation
* `git clone https://github.com/andrefrmacedo/REST-API-exercise.git` 
* `cd REST-API-exercise`
* `pip install -r requirements.txt`
* Create a MySQL database named `rest_exercise` and grant permissions to the username `exercise` with password `Exercise123.`
 
## Running the API server
* `python run.py` 

## Available methods
* <b>Create Rule</b>

 Send a `POST` request to the address `http://localhost:5000/api/v1/rules` following this example json data sctrucure:
```json
{
    "parameter":"CO",
    "threshold": 25000,
    "usernames":["rvitorino", "fmonsanto"]
}
```
* <b>Edit rule</b>
 
Send a `PUT` request to the address `http://localhost:5000/api/v1/rules/<parameter>` following this example json data sctrucure:
```json
{
    "parameter":"CO",
    "threshold": 20000,
    "usernames":["rvitorino", "fmonsanto"]
}
```
In this case `<parameter` whould be replaced by `CO`.

* <b>Create event</b>

 Send a `POST` request to the address `http://localhost:5000/api/v1/events` following this example json data sctrucure:
```json
{
    "parameter":"CO",
    "value": 30000
}
```

* <b>Create user</b>

Send a `POST` request to the address `http://localhost:5000/api/v1/users` following this example json data sctrucure:
```json
{
    "username":"andre"
}
```

* <b>Get user alerts</b>

Send a `GET` request to the address `http://localhost:5000/api/v1/users/<username>`. Following the examples above and replacing `<username>` for `fmonsanto` the API would return something like this:
```json
{
  "alerts": [
    {
      "parameter": "CO",
      "threshold": 20000,
      "timestamp": "Wed, 06 Jul 2016 00:15:32 GMT",
      "value": 30000
    }
  ],
  "message": "alerts for the user fmonsanto.",
  "status": true
}
```
