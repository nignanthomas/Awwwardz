# awwwardz

###  Author
nignanthomas

### Description
awwwardz is a clone of the website Awwwards. It allows a user to post a project he/she has created and get it reviewed by his/her peers.

### User Stories
1. View posted projects and their details
2. Post a project to be rated/reviewed
3. Rate/ review other users' projects
4. Search for projects
5. View projects overall score
6. View my profile page

### How to use
To use awwwardz, you must login/register. Once logged in, you will be able to see projects posted by other users.
You can add your own projects from your profile page to get them reviewed.
As a user you can rated others projects only once and leave a comment by the way.
You also have the possibility to edit your profile and view the projects that you have submitted.


### Tech used
1. HTML and CSS
2. Python
3. Django
1. Postgres
1. Heroku for deployment

## Set up and Installation
### Prerequisites
You will need to install git, django, postgres and python3.6+ installed in your machine.
To install these packages, you can use the following commands
```
#git
$ sudo apt install git-all

#python3.6
$ sudo apt-get install python3.6.

#django
$ pip install django==1.11

#postgres
$ sudo apt-get install postgresql postgresql-contrib libpq-dev
```

### Installation
1. To access this application on your command line, you need to clone it
`git clone https://github.com/nignanthomas/Awwwardz.git`
1. Create a requirements.txt in the root folder and copy the requirements above.
1. Install the required technologies with
`pip install -r requirements.txt`
1. Create a .env file and copy the .env code above
1. You can then run the server with:
`python3.6 manage.py runserver`
1. You can make changes to the db with
`python3.6 manage.py makemigrations clone`
`python3.6 manage.py migrate`
4. You can run tests:
`python3.6 manage.py test clone`



### Known Bugs
No known bugs.

### Live link
https://github.com/nignanthomas/Awwwardz

### Licence
This project is under the [MIT](https://github.com) licence

Copyright (c) 2018 nignanthomas
