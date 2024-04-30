# DJANGO AUTHORITZATION AND AUTHENICATION

## WHAT IT DOES?

This is a simple Blog Application where a user can perform CRUD operations over blogs, in addition I have implemented Authorization & Authentication system to keep the blog app safe & secure with throttle checks. IThere are permissions based on the group to which a user is assigned. A normal user has some simple permissions to create, read blogs, edit/delete his own blog but an Admin user can also delete any blog that he would wish, giving him more power over a normal blog user.

## HOW I BUILT IT?

* I have used Django throughout the project, used inbuilt templating engine (DTL), regarding the frontend side I have used Bootstrap for styling various components of the application with a minimal custom CSS.

* Function based views are used for more customization over class based views.

## To run this project: 

* Python must be installed in your local system before you start following next steps.

* Install the requirements:- `pip install django`
  
* Go inside the root project directory (Miniblog).
  
* Run migrations `python manage.py makemigrations` followed by `python manage.py migarte`
  
* Run server `python manage.py runserver`
