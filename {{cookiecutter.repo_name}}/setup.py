#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='{{cookiecutter.project_name}}',
            version='1.0',
            packages=find_packages(),
            install_requires=[
                'Django==2.0.2',
                'django-environ',
                'django-filter==1.0.4',
                'djangorestframework==3.7.1',
                'drf-schema-adapter==0.9.42',
                'django-debug-toolbar',
                'graphene==2.0.dev20170802065539',
                'graphene-django==2.0.dev2017083101',
                'graphql-core==2.0.dev20171009101843',
                'graphql-relay==0.4.5',
                'psycopg2==2.7.3.1',
                'pygments==2.2.0',
                'pytest==3.2.2',
                'uwsgi',
                'django-cors-headers',
            ]
      )
