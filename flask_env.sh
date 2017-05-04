#!/bin/bash

export FLASK_APP=/home/ubuntu/moltres-radio/index.py
export FLASK_DEBUG=1

flask run -h 0.0.0.0 -p 8080

