HEROKU:
pip install gunicorn
pip install django-heroku

PAGE:
python manage.py startapp herokuapp
add to settings.py
python manage.py migrate
Procfile:web: gunicorn djangoherokuapp.wsgi --log-file -
runtime.txt: python-version
pip install gunicorn dj-database-url whitenoise psycopg2
pip freeze > requirements.txt
