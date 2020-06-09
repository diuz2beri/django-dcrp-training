# 

**Open-Source Web App** coded in **Django Framework** on top of **Argon Dashboard** design. **Features**:

- SQLite, Django native ORM
- Modular design
- Session-Based authentication (login, register)
- Forms validation
- UI Kit: **Argon Dashboard** provided by **Creative-Tim**

## How to use it

```bash
$ # Get the code
$
$ cd django-dcrp-database
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env #Linux
$ source env/bin/activate
$ Virtualenv modules installation (Windows based systems)
$ # virtualenv --no-site-packages env
$ # .\env\Scripts\activate
$ 
$ # Install modules
$ # Postgres as Database
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```



