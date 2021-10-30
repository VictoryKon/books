The project is in implementation of a simpliest api that allows to create, list and filter the books.

## Running project locally

### Cloning the repository

First thing first, you need to clone the git repository.

### Virtual environment 
Ensure that you have python version >= 3.6 installed and run in the project root folder:

```
python -m venv env
``` 
Activate the virtual environment

```
source env/bin/activate
``` 
### Install dependencies

Run this command from the project root
```
pip install -r requirements.txt
```

### Start working with the database

Make migrations: run this command from the project root

```
python manage.py makemigrations books
```
After you've created migrations, apply them

```
python manage.py migrate
```

### Create createsuperuser

```
python manage.py createsuperuser --username=<yousername> --email=<email>
```

### Run server locally

In order to start running server locally, run:
```
python manage.py runserver
```
The api will be available at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
