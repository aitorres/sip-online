# Sistema de Inscripción de Postgrado Online (SIP)
Repositorio del Sistema de Inscripción de Postgrado Online, proyecto de desarrollo de la asignatura **Ingeniería de Software I (CI-3715)** durante el trimestre *Septiembre-Diciembre 2018* en la **Universidad Simón Bolívar**.

## Sobre el SIP Online
El Sistema de Inscripción de Postgrado Online es un sistema de gestión de profesores, asignaturas y trámites de inscripción trimestral para los estudiantes de postgrado. Permite gestionar la información necesaria para realizar la planificación trimestral a nivel de Departamento, consignar las disponibilidades horarias de los profesores, y permitir a los estudiantes el acceso a los trámites de manera digital, fácil, rápida y eficiente.

### Funcionalidades

Actualmente, el SIP Online permite:
- Gestionar los profesores de postgrado de un departamento (listar, ver detalles, agregar, modificar, eliminar)

### Desarrollo

El SIP Online se encuentra en desarrollo actualmente. El desarrollo se hace utilizando *Python 3.6.6* y *Django 1.11*. El resto de requerimientos se encuentran en el [archivo de requerimientos (requirements.txt)](requirements.txt).

## Documentación 
*En proceso*.

### Creación de la base de datos
En un terminal abierto y desde un usuario que pueda hacer `sudo`, ejecuta:
```bash
./crear_db.sh
python manage.py migrate
```

El script mencionado procederá a crear una base de datos en el gestor PostgreSQL con los datos asociados para poder ejecutar la aplicación.

### Inclusión de la data inicial
En un terminal abierto, con la base de datos cargada y migrada, ejecutar:
```bash
python manage.py loaddata gestion/fixtures/fixtures.json 
```

Django cargará la data inicial de los bloques 1 a 12 para los días lunes a sábado.


## Autores
- Andrés Ignacio Torres
- Javier Medina
- Mariagabriela Jaimes
- María Grimaldi
- Francisco Marcos
- Javier Vivas
- Julio Pérez
- Giacomo Tosone

## Contacto

Puede contactar al líder del equipo, Andrés Ignacio Torres, a través de su correo institucional 14-11082@usb.ve.