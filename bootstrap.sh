#!/bin/sh
export FLASK_APP=./app/app.py
export FLASK_DEBUG=1
# source /c/Users/Buster/.virtualenvs/REST-API-exercise-Oypl-3Vg/Scripts/activate
source $(pipenv --venv)\\Scripts\\activate
flask run -h 0.0.0.0
