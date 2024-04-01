# Hangman_Game
## Requirements
- python3
- pip
- django

It is recommended to create and activate a virtual environment:
```
$ python -m venv .venv

# LINUX
$ . .venv/bin/activate

# WINDOWS
$ . .venv/Scripts/activate
```

# Install the Django modules

pip install django
pip install djangorestframework
pip install django-cors-headers

# How to setup a project.

To create the Django project run the below command in the command prompt/ terminal

```django-admin startproject <name of the project>```


To run the project 

```python manage.py runserver```

The project will be running on the port `8000` sometimes port may differ.

You can copy the local host url  [LOCAL HOST](http://127.0.0.1:8000/) and paste it in the browser.


# How to setup app

To create an app run below command.

    ```python manage.py startapp <Name of the app>```

Let's consider the app name as `HangManGame`

Now Register app and the required modules in settings.py file in the installed project section.

In the below I have added `rest_framework, corsheaders and HangManGame` to the installed apps.

INSTALLED_APPS = [
    ...
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "HangManGame.apps.HangmangameConfig",
]


Add the `corsheaders` in the MIDDLEWARE. 

MIDDLEWARE = [
    ...
    "corsheaders.middleware.CorsMiddleware",
]

----

If you want to enable all domains to access the API's , you can add instruction to enable.

    CORS_ORIGIN_ALLOW_ALL = True
Not recommended.

----


Once you write your code.

### Make migrations and migrate to create the database schema:

python manage.py makemigrations
python manage.py migrate


To run the Django development server run 

```
python manage.py runserver

```

# Testing

## To test using Postman

- POST http://127.0.0.1:8000/api/game/new/

- POST http://127.0.0.1:8000/api/game/1/guess/
   
    provide below information in the json format. 
        
    postman> body>r aw> json
    ```
    {
    "guess": “a”
    }
    ```
* GET http://127.0.0.1:8000/api/game/1/

