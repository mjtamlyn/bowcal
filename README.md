# BowCal - archery tournament diary

BowCal is the archery tournament diary designed for archers. Search for
tournaments which suit you, see which of your friends are going, keep track of
shoots you're thinking about.

## Setup for development

You will need:
- A Unix based system (linux, osx)
- Python 3.4
- PostgreSQL
- Git

Instructions:
1. Clone the repository `git clone git@github.com:mjtamlyn/squads.git`
2. Create a virtual environment `virtualenv bowcal`
3. Install the requirements `pip install -r requirements.txt`
4. Create a database `psql -c "CREATE DATABASE bowcal"`
5. Migrate the database `python manage.py migrate`
6. Create a superuser account `python manage.py createsuperuser`
7. Run the server `python manage.py runserver`
