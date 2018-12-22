release: python manage.py migrate --no-input && python manage.py loaddata gestion/fixtures/fixtures.json
web: gunicorn sip.wsgi