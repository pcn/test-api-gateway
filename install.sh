#!/bin/bash

mkdir /v
python3 -m venv /v

. /v/bin/activate

pip3 install flask jsonschema black mypy

chmod +x /app/service.sh
