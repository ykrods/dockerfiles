#!/bin/bash

if [ ! -d /venvs/venv ]; then
    python3 -m venv /venvs/venv
fi

if [ -f /code/requirements.txt ]; then
    /venvs/venv/bin/pip install -r /code/requirements.txt
fi
