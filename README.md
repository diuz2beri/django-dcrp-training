# 

**Open-Source Web App** coded in **Django Framework** on top of **Argon Dashboard** design. **Features**:

- Postgres, Django native ORM
- Modular design
- Session-Based authentication (login, register)
- Forms validation
- UI Kit: **Argon Dashboard** 


You will need to install:
Python 3.8
PostgreSQL 12
Django 3.0.7


<br />


## How to use it

```bash
$ # Get the code

$ cd django-dcrp-database

$ cd django-dcrp-training
$
$ #Create a virtual enviroment 
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env #Linux
$ source env/bin/activate
$ Virtualenv modules installation (Windows based systems)
$ # virtualenv --no-site-packages env
$ # .\env\Scripts\activate
$ 
$ # Install modules
$ # Postgres as Database (Change setting.py for database connection)

$ #pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver or python manage.py runserver 127.0.0.1:<portnumber>
$
$ # Access the web app in browser: http://127.0.0.1:8000/ or 127.0.0.1:<portnumber you specified above>
``` 

<br />

## Credits & Links

- Django Boilerplate
- Django Framework
- CreativeTim
- Appspeed



