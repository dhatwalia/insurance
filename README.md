# Insurance Advisor

Lakehead University COMP-9800 Project Winter - Spring/Summer 2021

## Steps to install
### On Google Cloud Platform(GCP) API Credentials

1.  Authorized Javascript Origins: http://127.0.0.1:8000

2.  Authorized Redirect URIs: http://127.0.0.1:8000/accounts/google/login/callback/

Note the Client ID and Client secret.

### On your device
1. Install MySQL and create a database named “insurance”

2. Run the following commands
    ``` 
    $ pip install -r required.txt

    $ python ./configure.py

    $ python manage.py makemigrations
        
    $ python manage.py migrate
        
    $ python manage.py createsuperuser

    $ python manage.py runserver
    ```

3.  Go to http://127.0.0.1:8000/admin and login with the superuser credentials.

4.  Update the domain and display name from example to "127.0.0.1:8000".

5. Go to Social Accounts/ Social applications and create a new record. For Provider select "Google", copy and paste the Google Client id and Secret key from GCP and choose example for sites.  

## Steps to run
1. Run the following command
```
$ python manage.py runserver
```

2. Go to http://127.0.0.1:8000/ in your browser.

Note: You must consistently use http://localhost:8000/ OR http://127.0.0.1:8000/ everywhere to match the URL pattern on GCP to make OAuth work.
