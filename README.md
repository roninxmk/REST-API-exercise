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
* [Python 3.6](http://www.python.org/)
* [Pip](https://pypi.python.org/pypi/pip)
* [MySQL 5.x](http://www.mysql.com/) 

## Instalation
* `git clone https://github.com/andrefrmacedo/REST-API-exercise.git` or better fork from the original project.
* `cd REST-API-exercise`
* `pip install -r requirements.txt`
* Create a MySQL database named `rest_exercise` and grant permissions to the username `exercise` with password `Exercise123.` You can register a free account at freemysqlhosting.net for a MySQL 5.5 Server. It is not working with MySQL 8.x.
 
## Running the API server
* use [CMDER](http://cmder.net/) for Windows to run `sh bootstrap.sh`. Check this [source](https://auth0.com/blog/developing-restful-apis-with-python-and-flask/) for more information about `bootstrap.sh`.
* If you are not using a virtualized environment, then you can comment the `source` line from `bootstrap.sh`.

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
 
Send a `PUT` request to the address `http://localhost:5000/api/v1/rules/<parameter>` following this example json data sctrucure (in this case `<parameter` was replaced by `CO`):
```json
{
    "parameter":"CO",
    "threshold": 20000,
    "usernames":["rvitorino", "fmonsanto"]
}
```

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

# Executing the task

In order to execute the assigned task, the student needs to `pip install requests`.

