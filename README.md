# CRUD Application Demo

We are going to perform CRUD operation in this project.


## Cloning the repository

Clone the repository using the command below :

```bash
  https://github.com/indrajeetydv/Django.git
```
Move into the directory where we have the project files :

```bash
  cd CrudApplicationDemo
```
## Setup the Django Application

Create a virtual environment :

```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname
```

Activate the virtual environment :
```bash
  envname\scripts\activate
```

install Django:
```bash
  pip install django
```
To create Django project
```bash
  django-admin startproject <projectname>
```

To create the apps 
```bash
  python manage.py startapp <appname>
```

## Running the App

To run the App, we use :
```bash
  python manage.py runserver
```

To Create the tables:

```bash
# It will create a migration file by Django which are basically commands on how to convert the model into a database table.
python manage.py makemigrations crud

# It will execute the commands and creates a table called User with the given attributes and conditions
python manage.py migrate
```


## Run Locally

the development server will be started Locally at below endpoint

```bash
  http://127.0.0.1:8000/
```
