BASIC INFORMATION:

Django is a web framework designed to make it easier for us to get started with web development.

Django takes care of fundamental web components
which allows the developer to focus on the actual logic behind the web application.

**any files or lines of code that have been added or edited have an '#edit' comment indicating it did not come with the default Django set up**

COMMANDS:

(pip command to install Django with python 3)
pip3 install Django

(command to create a Django project)
django-admin startproject PROJECT_NAME
python -m django startproject PROJECT_NAME
(this will create some starter files for web application)

(run web application)
python manage.py runserver
(http://127.0.0.1:8000/)

(command to create an app in the Django project)
python manage.py startapp APP_NAME
(app name must be included under INSTALLED_APPS under settings.py under the Django project)

DJANGO PROJECT FILES:

(used to execute commands in project)
manage.py

(contains important default configuration/behavioral settings)
settings.py

("table of contents" for all urls that can be visited on web application)
urls.py