## User Authentication
User Authentication basic overview.
<br><br>
- User can signup, login and see a users list.
- User can also login from Google social Login.
<br><br>

### Install virualenv
```
    ├── pip install virtualenv
```

### Create virtualenv
```
    ├── virtualenv <your-env>
```

### Activate virtualenv (Windows)
```
    ├── path\<your-env>\Scripts\activate
```

### Activate virtualenv (MAC)
```
    ├── source path\<your-env>\bin\activate
```

### Activate virtualenv (Linux)
```
    ├── path\<your-env>\bin\activate
```

### After activate virtualenv Install Libraries
```
    ├── pip install -r requirements.txt
```


Create database called 'DATABASE-NAME'

### Configure database in .env file
```
    ├── ENGINE = 'django.db.backends.postgresql'
    ├── DB_HOST = 'HOST-NAME'
    ├── DB_PORT = 'PORT'
    ├── DB_NAME = 'DATABASE-NAME'
    ├── DB_USER = 'DATABASE-USER-NAME'
    ├── DB_PASSWORD = 'DATABASE-USER-PASSWORD'
```

### Configure Social Auth
GOOGLE_OAUTH2_KEY, GOOGLE_OAUTH2_SECRET in .env file
```
    ├── GOOGLE_OAUTH2_KEY = 'GOOGLE_OAUTH2_KEY'
    ├── GOOGLE_OAUTH2_SECRET = 'GOOGLE_OAUTH2_SECRET'
```

### Configure Google Email
Configure your Gmail Account as mentioned in this URL - https://dev.to/abderrahmanemustapha/how-to-send-email-with-django-and-gmail-in-production-the-right-way-24ab
```
    ├── EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    ├── EMAIL_HOST = 'smtp.gmail.com'
    ├── EMAIL_PORT = 587
    ├── EMAIL_HOST_USER = '<YOUR-EMAIL>'
    ├── EMAIL_HOST_PASSWORD = '<YOUR-EMAIL-PASSWORD>'
    ├── EMAIL_USE_TLS = True
```

### Run Migrations
```
    ├── python manage.py makemigrations
    ├── python manage.py migrate
```

### Run server
```
    ├── python manage.py runserver
```

### Open a browser and visit
```
    ├── http://127.0.0.1:8000/login
```
