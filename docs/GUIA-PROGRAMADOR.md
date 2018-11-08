# GUÍA DEL PROGRAMADOR

Este documento pretende dar una idea general del proyecto desde el punto de vista del programador, sirviendo como guía a profundidad de los detalles de implementación, códigos, scripts, instalación, entre otros detalles, orientada a ser leída por un programador. El documento se encuentra en constante actualización en el proceso de desarrollo del Sistema de Inscripción de Postgrado, e incluirá una guía de entidades, métodos y shortcuts de instalación.

Para revisar una documentación más amigable al usuario y fácil de leer y entender sobre la funcionalidad del sistema, puedes revisar la [guía del usuario](GUIA-USUARIO.md).

## Base de datos

Cada entidad de la base de datos cuenta con diversos métodos para permitir su gestión.
Todas las clases tienen un método __str__ para definir su impresión.

| Entidades     | Atributos                           | Métodos                             |
| ------------- |:-----------------------------------:|-----------------------------------:|
| Departamento  | nombre,código,jefe | Tiene jefe, jefe_coherente, __str__ |
| Profesor      | nombre, apellido, cedula, disponibilidad,departamentos,email,asignaturas|   codigo_completo,__str__ |
| Asignatura    | nombre,código,departamento          | __str__                             |

## Ejecución de pruebas

Para ejecutar las pruebas unitarias, en un terminal abierto se debe ejecutar:

```bash
python manage.py test
```

La salida de las pruebas está mejorada por el paquete *Django-nose* y muestra una breve descripción de cada prueba, así como los errores posibles (que, a fecha de redacción de este documento, no hay) y otros datos de las pruebas.

## Scripts de desarrollo

A continuación se listarán algunos scripts de desarrollo para facilitar la ejecución de algunas tareas para el programador del SIP Online.

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

Django cargará la data inicial de los bloques 1 a 12 para los días lunes a sábado, al igual que la data de los 27 departamentos existentes a la fecha (noviembre de 2018) en la estructura de la Universidad Simón Bolívar.