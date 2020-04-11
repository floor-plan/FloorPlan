# FloorPlan

An application aimed at the construction industry to simplify work flow with a task management system. All users are allowed to view and mark tasks as complete, but only project managers are allowed to edit. When creating an account a user must select which group they belong and their permissions will be assigned to that username. It is easy to view other members of the team associated with the project and check the box to a task that has been completed, if assigned to the logged-in user.    


## Requirements

This app requires the use of Python 3.7.6, Django, and Gunicorn.


## Using this application

To run, simply clone this repository into an empty directory in your system by running:

git clone https://github.com/floor-plan/FloorPlan.git

Once in the directory run the following:

pipenv install 

pipenv shell 

./manage.py migrate

Then to open locally on your machine:

./manage.py runserver


