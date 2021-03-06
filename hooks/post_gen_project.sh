#!/bin/bash


USER="{{ cookiecutter.user_name }}"
EMAIL="{{ cookiecutter.email }}"
if [ `which virtualenv|grep virtualenv 2>/dev/null` ]
then
      virtualenv -p {{ cookiecutter.python_version }} venv
  else
      {{cookiecutter.python_version}} -m venv venv
fi

source venv/bin/activate
echo "Installing  dependencies"
pip install --upgrade pip setuptools
pip install -r requirements.txt
pip freeze --local > requirements.txt
cp environ.py.dist environ.py


echo "Installing front end dependencies"

yarn install

cp node_modules/bootstrap/dist/css/bootstrap.min.css {{cookiecutter.repo_name}}/static/css
cp -r node_modules/bootstrap/dist/js {{cookiecutter.repo_name}}/static/

rm -fr node_modules


echo "Activating virtualenv & starting django server"
source venv/bin/activate
python manage.py migrate

echo "Creating superuser {{cookiecutter.user_name}}"
python manage.py createsuperuser --username {{cookiecutter.user_name}} --email {{cookiecutter.email}}

git init .
git add .
git commit -m 'initial commit'

python manage.py runserver
