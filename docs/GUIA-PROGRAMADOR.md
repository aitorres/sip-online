# GUÍA DEL PROGRAMADOR

Este documento pretende dar una idea general del proyecto desde el punto de vista del programador, sirviendo como guía a profundidad de los detalles de implementación, códigos, scripts, instalación, entre otros detalles, orientada a ser leída por un programador. El documento se encuentra en constante actualización en el proceso de desarrollo del Sistema de Inscripción de Postgrado, e incluirá una guía de entidades, métodos y shortcuts de instalación.

Para revisar una documentación más amigable al usuario y fácil de leer y entender sobre la funcionalidad del sistema, puedes revisar la [guía del usuario](GUIA-USUARIO.md).

## Versiones principales de paquetes

La versión de Python utilizada para desarrollar y ejecutar el servidor es **Python 3.6.6**. La versión de Django utilizada para ejecutar la aplicación es **Django 1.11.15**. El resto de paquetes requeridos están listados en el [archivo de requerimientos (requirements.txt)](../requirements.txt).

## Base de datos

Cada entidad de la base de datos cuenta con diversos métodos para permitir su gestión.
Todas las clases tienen un método __str__ para definir su impresión.

| Entidades     | Atributos                           | Métodos                             |
| ------------- |:-----------------------------------:|-----------------------------------:|
| Departamento  | nombre,código,jefe | tiene_jefe, jefe_coherente, __str__ |
| Profesor      | nombre, apellido, cedula, disponibilidad,departamentos,email,asignaturas,usuario| es_jefe  __str__ |
| Asignatura    | nombre,código,departamento,horas_laboratorio,horas_teoria,horas_practica,unidad_creditos,requisitos         | codigo_completo, tiene_requisito, horas_l, horas_p, horas_t, credito,profesores __str__                             |
| Oferta Trimestral | trimestre, departamento, es_final | nombre_completo,estado,asignaturas_ofertadas, __str__
| AsignacionProfesoral | oferta_trimestral,profesor,asignatura,es_final,tipo |
| Coordinacion  | nombre, codigo, asignaturas, coordinador | __str__, tiene_coordinador, ofertas_disponibles

La base de  datos posee 2 triggers.
El primero de ellos se encarga de crear un nuevo usuario automáticamente se crea un profesor en el sistema. Este usuario posee los datos de este profesor y es de tipo profesor.

El segundo trigger funciona de manera parecida al anterior pero con la eliminacion. Al eliminar un profesor, se eliminara el usuario asociado a este.

## Ejecución de pruebas

Para ejecutar las pruebas unitarias, en un terminal abierto se debe ejecutar:

```bash
python manage.py test
```

La salida de las pruebas está mejorada por el paquete *Django-nose* y muestra una breve descripción de cada prueba, así como los errores posibles (que, a fecha de redacción de este documento, no hay) y otros datos de las pruebas.

## Variables de entorno

El sistema utiliza las siguientes variables de entorno para poder trabajar. Todas tienen un comportamiento por defecto, en caso de que no se configuren:

- *CUR_DOMAIN*, el dominiio actual. Por defecto es *localhost*. Está enlazado a la base de datos que se utilice, y al manejador de correos usado.
- *DB_NAME*, nombre de la base de datos en producción
- *DB_USER*, usuario de la base de datos en producción
- *DB_PASS*, contraseña del usuario de la base de datos en producción
- *DB_HOST*, hostname de la base de datos en producción
- *EMAIL_HOST*, hostname del servidor SMTP de correo electrónico
- *EMAIL_HOST_USER*, usuario (correo) autorizado por el servidor de correos electrónicos

## Scripts de desarrollo

A continuación se listarán algunos scripts de desarrollo para facilitar la ejecución de algunas tareas para el programador del SIP Online.

Estos scripts están orientados a usuarios de sistemas operativos *Linux* con gestor de paquetes *apt*, como las distribuciones basadas en *Debian*, pero fácilmente pueden adaptarse a otros sistemas operativos si se usan como guía.

### Creación de un entorno virtual

En un terminal abierto desde la carpeta del proyecto, una vez hayas clonado el repositorio, ejecutar (una única vez):

```bash
sudo apt install python3-pip
pip3 install virtualenv
virtualenv -p /usr/bin/python3 software
```

### Ejecución del entorno virtual

En un terminal abierto desde la carpeta del proyecto, cada vez que se vaya a ejecutar el proyecto o realizarle modificaciones, ejecutar:

```bash
source software/bin/activate
```

### Instalar dependencias

En un terminal abierto desde la carpeta del proyecto, después de crear y ejecutar el entorno virtual,

```bash
pip install -r requirements.txt
```

### Creación de la base de datos

En un terminal abierto y desde un usuario que pueda hacer `sudo`, ejecuta:

```bash
./crear_db.sh
python manage.py migrate
```

El script mencionado procederá a crear una base de datos en el gestor PostgreSQL con los datos asociados para poder ejecutar la aplicación.

### Ejecución de migraciones

**IMPORTANTE**. Realizar esto cada vez que se notifica al equipo de un cambio en los modelos de la base de datos. Si no estás seguro si el cambio ha ocurrido, puedes ejecutarlo e igual no hará nada negativo.

En un terminal abierto desde la carpeta del proyecto, con la base de datos creada y ejecutando el entorno virtual con las dependencias instaladas, ejecutar:

```bash
git pull
python manage.py migrate
```

### Generación de migraciones

**IMPORTANTE**. Realizar esto cada vez que se modifique algún modelo de la base de datos y notificar al equipo de desarrollo de estos cambios. Si no estás seguro si el cambio ha ocurrido, puedes ejecutarlo e igual no hará nada negativo. Recuerda hacer *commit* del archivo de migraciones generado automáticamente y subirlo al repositorio **siempre** que se genere.

En un terminal abierto desde la carpeta del proyecto, con la base de datos creada y ejecutando el entorno virtual con las dependencias instaladas, ejecutar:

```bash
python manage.py makemigrations
```

### Inclusión de la data inicial

En un terminal abierto, con la base de datos cargada y migrada, ejecutar:

```bash
python manage.py loaddata gestion/fixtures/fixtures.json
```

Django cargará la data inicial de los bloques 1 a 12 para los días lunes a sábado, al igual que la data de los 27 departamentos existentes a la fecha (noviembre de 2018) en la estructura de la Universidad Simón Bolívar, tambien carga informacion de prueba de algunas asignaturas y profesores.

### Comandos importantes

A traves de la terminal se pueden realizar diversas acciones importantes para el manejo del sistema:

```bash
- python manage.py crear_jefe
```

```bash
- python manage.py asignar_jefe
```

```bash
- python manage.py crear_coordinador
```

```bash
- python manage.py asignar_coordinador
```

Estos comandos se documentan más adelante, en la sección de *Comandos de Administración*.

### Ejecutar el proyecto

En un terminal abierto desde la carpeta del proyecto, con la base de datos creada y migrada y desde el entorno virtual habiendo instalado previamente los requerimientos, hacer:

```bash
python manage.py runserver
```

## Comandos de Administración

Se han incorporado comandos de administración personalizados para el manejo inicial de algunos datos y carga de usuarios especiales, además de obtener cierta información. Se listan a continuación:

### Listar Coordinaciones

Para listar todas las Coordinaciones en sistema, incluyendo sus códigos únicos, ejecutar:

```bash
python manage.py listar_coordinaciones
```

### Listar Departamentos

Para listar todos los Departamentos en sistema, incluyendo sus códigos únicos, ejecutar:

```bash
python manage.py listar_departamentos
```

### Crear coordinador (nuevo)

Para crear un nuevo profesor y asignarlo como coordinador de una Coordinación existente, ejecutar lo siguiente y seguir los pasos en pantalla:

```bash
python manage.py crear_coordinador
```

### Crear jefe (nuevo)

Para crear un nuevo profesor y asignarlo como jefe de un Departamento existente, ejecutar lo siguiente y seguir los pasos en pantalla:

```bash
python manage.py crear_coordinador
```

### Asignar coordinador (ya existente)

Para asignar un profesor ya existente como coordinador de una Coordinación existente, ejecutar lo siguiente y seguir los pasos en pantalla:

```bash
python manage.py asignar_coordinador
```

### Asignar jefe (ya existente)

Para asignar un profesor ya existente como jefe de un Departamento existente, ejecutar lo siguiente y seguir los pasos en pantalla:

```bash
python manage.py asignar_coordinador
```
