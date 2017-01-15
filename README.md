# SurveySumo

Survey Sumo is a web application that allows you to create survey questions and serve them to potential users never allowing the same user to answer the same question twice.

## Installation instructions

### OSX

Install XCode https://itunes.apple.com/us/app/xcode/id497799835?mt=12

Install Homebrew http://brew.sh/

Install mysql ` brew install mysql `

Start mysql ` mysql.server start `

Install git ` brew install git `

Pull from this repo `git clone https://github.com/siracoj/SurveySumo.git`

Install requirements `sudo pip install -r SurveySumo/requirements.txt`

### Ubuntu / Debian

Install mysql ` sudo apt-get install mysql-server `

Start mysql ` mysqld --initialize ` (Dont put a password for root here)

Check if mysql is running ` service mysql status `

Install git ` sudo apt-get install git `

Pull from this repo `git clone https://github.com/siracoj/SurveySumo.git`

Install requirements `sudo pip install -r SurveySumo/requirements.txt`

### Centos / Fedora

Install mysql ` sudo yum install mysql-server `

Start mysql ` sudo /sbin/service mysqld start `

Initialize mysql ` sudo /usr/bin/mysql_secure_installation ` (Dont put a password for root here)

Install git ` sudo yum install git `

Pull from this repo `git clone https://github.com/siracoj/SurveySumo.git`

Install requirements `sudo pip install -r SurveySumo/requirements.txt`


## Django setup

Log in to mysql `mysql -u root`

Create the survey db `create database survey_sumo`

Change Directory to survey_sumo `cd SurveySumo/survey_sumo`

Run the django migration `python manage.py migrate`

Run the server `python manage.py runserver`

Now you should be able to access the site @ http://localhost:8000/



## Requirements

Create a simple Django Survey app using MySQL.

The app should allow an admin to enter survey questions with multiple choice answers.

When a guest visits the app in a browser it should present a random survey question to the guest and allow them to answer.

Record answers and display the survey results in an admin interface.

Avoid showing a previously answered question to the same guest.

Make sure the UI is mobile browser friendly and we can run it in a test environment.

Provide a clear README with instructions on how to setup and run the app.

Create a github.com repository with the app that we can pull from and test.
