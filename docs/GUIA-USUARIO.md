# GUÍA DEL USUARIO

Este documento pretende servir como guía para el uso de la aplicación, de una manera sencilla y acompañada de guías visuales, para poder acceder a las diversas funcionalidades presentes.

## Inicio

![Dashboard](imagenes/dashboard.png "Vista del Dashboard")

La sección de inicio de la aplicación muestra la barra de navegación lateral y tres contadores dinámicos de asignaturas, departamentos y profesores, además de mostrar un saludo al usuario en cuestión. Arriba a la derecha, se puede acceder a algunas opciones que trabajarán en un futuro, como perfil y cierre de sesión; sin embargo, ahorita no hacen nada, sirviendo solo de *mock-up* de la interfaz gráfica.

## Gestión de Profesores

El apartado de Gestión de profesores, al que se puede acceder con la barra de navegación lateral, permite realizar operaciones sobre los datos de profesores, como:

- Agregar un profesor nuevo con sus datos respectivos
- Modificar los datos de un profesor existente
- Eliminar un profesor existente
- Listar todos los profesores cargados en sistema
- Realizar búsquedas por cédula, nombre, apellido, código de departamento, nombre de departamento, código de asignatura y/o nombre de asignatura que puden dictar entre los profesores listados
- Ver los detalles de atributos, asignaturas que puede dictar y disponibilidad horaria de un profesor en particular

Todas las operaciones están concentradas en la misma vista.

### Listar profesores

El apartado de listar profesores es la vista por defecto de la página. Los profesores se distribuyen en una tabla dinámica que muestra la cédula, el nombre, el apellido, el departamento asociado y la lista de materias que puede dictar cada profesor. La tabla, en su parte inferior, cuenta con opciones de paginación para ver entre 10 y 100 profesores por página y avanzar entre ellas. En su parte superior, cuenta con un campo de búsqueda dinámico que puede filtrar por todos los campos mostrados con solo empezar a escribir. 

Las acciones posibles en cuanto a gestión de la información son:
- Agregar un profesor, haciendo clic en el botón azul que se encuentra encima de la tabla
- Ver detalles de un profesor, haciendo clic en el ícono de *ojo* en la celda de acciones de ese profesor
- Modificar un profesor, haciendo clic en el ícono de *lápiz* en la celda de acciones de ese profesor
- Eliminar un profesor, haciendo clic en el ícono de *papelera* en la celda de acciones de ese profesor


