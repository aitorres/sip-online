release: python manage.py migrate --no-input && python manage.py loaddata gestion/fixtures/fixtures.json
web: python manage.py runserver 0.0.0.0:$PORT --noreload