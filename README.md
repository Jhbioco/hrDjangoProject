# webDjangoProject (basic web app)
This is a small django project for those who want to star developing web app using Django Framework (python framework).
The project is an app for human resources management. 
Wokflow:
  - We start installing necesary softwares in order to use django (you can see the requirments bellow).
  - After that, we create the projet using the command (django-admin.py startproject myproject).
    - When we create the project we can go to the project folder and then write in command line the command (python manage.py runserver).
    - If we go to the browser and write (localhost:8000) the django home page opens. That means your project has been set up correctly.
  - We then create the app called employees using the command (python manage.py runserver startapp employees).
  - Its necessary to create a supperuser (python manage.py createsuperuser) in order to take advantage of the django admin.
  - - The file called setting.py inside project folder have to be configure. We have to register the app (employees) in the installed App of the settings.py document.
  - Next steps follows the order:
    - Create (models--->register models in admin.py---> templates ---> urls ---> forms ---> views).

A boostrap free template was used to create the templates (you can download in: url: https://startbootstrap.com/previews/simple-sidebar/).
   
1 - Requirements
  - Install virtual environment (virtualenv virtual)
  - Install django-2.1.5 (pip install django)
  - Install pillow-5.4.1 (pip instal pillow)

2 - Create the project (myproject)
  - django-admin startproject myproject
  
3 - Create the app
  - python manage.py startapp employees

4 - Edit settings.py file
  - Add the app (employees)
  - configure staticfiles

5 - Create the folder templates (where we create the html files) inside the app (employees) 
6 - Create the static file inside the app and past the css e js folder from the free bootstrap template
7 - Start build the app (employees)
You can donwload these project into you computer.
See the django documentation for any support you need (https://docs.djangoproject.com/en/2.1/intro/)

