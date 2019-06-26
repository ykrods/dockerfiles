#!/bin/bash

if [ ! -d ${VENV_PATH} ]; then
    python3 -m venv ${VENV_PATH}
fi

if [ -f ${PROJECT_PATH}/requirements.txt ]; then
    ${VENV_PATH}/bin/pip install -r ${PROJECT_PATH}/requirements.txt
fi
