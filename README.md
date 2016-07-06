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


