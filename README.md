# TODO list API for Artistanbul

### created with django rest framework 

# Description

It is a To-Do Application developed with Django Rest Framework.


## End Points

* `GET /api/task-list/`
* `GET /api/task-detail/{pk}`
* `POST /api/task-update/{pk}`
* `DELETE /api/task-delete/{pk}`


## Get the code
* Clone the repository
`git clone https://github.com/ahmetumitbayram/todo-app-django-rest-framework.git`

## Install the project dependencies

`pip install -r requirements/requirements.txt`

## Run the command to generate the database
`python manage.py migrate`

## Generate super user
`python manage.py createsuperuser`

## Run the server
`python manage.py runserver` the application will be running on port 8000 **http://0.0.0.0:8000/**

## Run the test
`python manage.py test`
