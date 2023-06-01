#!/usr/bin/env bash

git clone git@github.com:srinidhi007/2nd-project-CI-CD.git
cd 2nd-project-CI-CD.git
python3 -m venv ~/.flask-ml-azure
source ~/.flask-ml-azure/bin/activate
az webapp up --name flask-ml-azure-sri--resource-group Udacity-2 --sku F1 --location "North Europe" --logs --runtime "PYTHON:3.97"