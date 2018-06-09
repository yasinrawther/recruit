# recruit
Recruitment Site

## Description:

This project used to submit the recruit form from anonymous user and Admin can able to Accept and Reject the Form.

I have used only two urls:

- `/recruitment/recruiters` This url to submit the form
- `/recruitment/recruiters_list` This url admin only can access and he can able to accept and reject the form


## Technology Used:

- Python3.4
- Django
- Jquery
- Javscript
- PostgreSql

## Project Setup Procedure:
Create virtalenv by command

`virtualenv -p /usr/bin/python3.4 recruit`

Activate the virtualenv by:

`source recruit/bin/activate`

Install the pip packages from requirements.txt file:

`pip install -r requirements.txt`

Create the role and database in postgresSql:

Enter to psql shell:

`sudo -U postgres psql`

Create role:

`create role recruit with login password '123';`

Create Database: 

`create database recruit owner recruit;`

For migrations:

In the source code I have added the migrations script so you can just run the below command to migrate the schema:

`python manage.py migrate`

Then create the superuser:

From the project directory run:

`python manage.py createsuperuser`

Then start the project by the command: 

`python manage.py runserver`
