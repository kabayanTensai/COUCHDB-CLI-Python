#!/bin/sh
export PYTHONPATH=$(pwd)/src/py
set -a
exec poetry run python app.py $@
