# Django CI_CD Sample Project


## Set up Environment
env_name='django_ci'
python3 -m venv ~/.venvs/${env_name}     

## Activate environment
source ~/.venvs/${env_name}/bin/activate

## Pip upgrade
pip install --upgrade pip

## Installing django, django-admin
pip install django-admin
pip install Django

## Create a project
django-admin startproject core .
## Update the env 
set keys

## Create a project
django-admin startapp blog .
## Updated the requirements 
pip freeze > requirements_production.txt

## Install all the dependencies
pip install -r requirements_production.txt -U



