# sip-online
Repositorio del Sistema de Inscripción de Postgrado Online

## Creación de la base de datos
En un terminal abierto y desde un usuario que pueda hacer `sudo`, ejecuta:
```bash
./crear_db.sh
python manage.py migrate
```

El script mencionado procederá a crear una base de datos en el gestor PostgreSQL con los datos asociados para poder ejecutar la aplicación.

## Inclusión de la data inicial
En un terminal abierto, con la base de datos cargada y migrada, ejecutar:
```bash
python manage.py loaddata gestion/fixtures/fixtures.json 
```

Django cargará la data inicial de los bloques 1 a 12 para los días lunes a sábado.
