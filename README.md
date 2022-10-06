# About this Ecommerce Project 
Django is a Python web framework that is open source and used for rapid development, pragmatic, maintainable, clean design, and website security. A web application framework is a toolkit that contains all of the components required for application development.

This is a simple Ecommerce site where customers can place orders and have goods delivered to their homes.

# Tutorial 
To get this project up and running locally on your computer follow the following steps.

## Setup
The first thing to do is to clone the repository:

`$ git clone https://github.com/roberwangunda/Study-portal.git.` <br /> 
`$ cd Study-portal`

Set up a python virtual environment on windows and activate it  <br /> 
`python3 -m venv [Virtual Environment Name]` <br /> 
`.\Scripts\activate`

Then install the dependencies:

`pip install -r requirements.txt`

Make migrations by running the command 

`python manage.py migrate`

Create the Admin

`python manage.py createsuperuser`

Start Django App

`python manage.py runserver`
