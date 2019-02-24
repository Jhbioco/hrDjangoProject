# DjangoProject (simple web app)
This project is a simple django web app for human resources management.
#
Wokflow:
   
1. Install Requirements
  ```
  virtualenv virtual
  ```
  ```
  source virtual/bin/activate
  ```
  ```
  pip install django
  ```
  ```
  pip install pillow
  ```
  
#
2. Create the project (myproject)
  ```
  django-admin startproject myproject
  ```
  
3. Create the app
  ```
  python manage.py startapp employees
  ```

#
4. Edit settings.py file

  - Add the app (employees)
  ```
  INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'employees',

]
  ``` 
  
  - Configure static files
  ```
  
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATICFILES_DIRS = [
    'statics',
]
  ```

#
5. Create the folder templates (where we create the html files) inside the app (employees) 

  A boostrap free template was used to create the templates (you can download in: url: https://startbootstrap.com/previews/simple-sidebar/).

6. Create the static file inside the app and past the css e js folder from the free bootstrap template

7. Start developing the app (employees)

You can donwload these project into you computer and adjust as you want.

See the django documentation for any support you need (https://docs.djangoproject.com/en/2.1/intro/)

