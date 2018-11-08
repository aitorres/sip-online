# GUÍA DEL USUARIO

Este documento pretende servir como guía para el uso de la aplicación, de una manera sencilla y acompañada de guías visuales, para poder acceder a las diversas funcionalidades presentes. El documento se encuentra en constante actualización en el proceso de desarrollo del Sistema de Inscripción de Postgrado, e incluirá una guía de todas las acciones posibles.

Para revisar una documentación más técnica, puedes revisar la [guía del programador](GUIA-PROGRAMADOR.md).

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

![Listar](imagenes/listar.png "Vista de Listar Profesores")

El apartado de listar profesores es la vista por defecto de la página. Los profesores se distribuyen en una tabla dinámica que muestra la cédula, el nombre, el apellido, el departamento asociado y la lista de materias que puede dictar cada profesor. La tabla, en su parte inferior, cuenta con opciones de paginación para ver entre 10 y 100 profesores por página y avanzar entre ellas. En su parte superior, cuenta con un campo de búsqueda dinámico que puede filtrar por todos los campos mostrados con solo empezar a escribir. 

Las acciones posibles en cuanto a gestión de la información son:
- Agregar un profesor, haciendo clic en el botón azul que se encuentra encima de la tabla
- Ver detalles de un profesor, haciendo clic en el ícono de *ojo* en la celda de acciones de ese profesor
- Modificar un profesor, haciendo clic en el ícono de *lápiz* en la celda de acciones de ese profesor
- Eliminar un profesor, haciendo clic en el ícono de *papelera* en la celda de acciones de ese profesor

Esta vista incluye validaciones y mensajes de error o éxito en función del resultado de las acciones de gestión de la información.

### Agregar un profesor

![Agregar](imagenes/agregar.png "Vista de Agregar Profesores")

Al hacer clic al botón de agregar un profesor, se puede llenar el formulario de inclusión de los datos de profesores y hacer *envío* del mismo. Los campos de *asignaturas* y *disponibilidades* se muestran como listas desplegables *autocompletables*: se puede empezar a escribir y se filtrarán sus contenidos. Esta vista muestra errores de validación, como cédulas que se repiten.

### Visualizar detalles de profesor

![Ver detalles](imagenes/ver.png "Ver detalles de profesor")

Al hacer clic al ícono de ver un profesor (*ojo*), se puede visualizar la información almacenada de ese profesor en dos secciones. La primera, que se muestra en la imagen superior, lista los datos básicos y la lista de asignaturas que puede dictar un profesor.

![Ver disponibilidad de horarios](imagenes/ver_disponibilidad.png "Ver disponibilidad horaria de profesor")

Si se sigue revisando el contenido de la ventana emergente (modal), se verá una matriz que incluye la disponibilidad horaria del profesor según sus datos almacenados en el sistema, indicando con un mensaje afirmativo en qué horarios puede dictar asignaturas dentro de la Universidad Simón Bolívar.

### Editar un profesor

![Editar](imagenes/editar.png "Vista de Editar Profesores")

Al hacer clic al ícono de editar un profesor (*lápiz*), se puede visualizar el formulario de edición de sus datos y hacer *envío* del mismo. Los campos son los mismos que se muestran en el formulario de *Agregar un profesor* pero vienen pre-llenados con los datos actuales del profesor en cuestión. De igual manera, cuenta con validaciones y muestra los errores en caso de existir.

### Eliminar un profesor

![Eliminar](imagenes/eliminar.png "Vista de Eliminar Profesor")

Al hacer clic al ícono de eliminar un proefsor (*papelera*), se puede visualizar la ventana de confirmación de eliminación y hacer *confirmación* de la misma. Si se hace clic en el botón rojo, el profesor quedará eliminado del sistema. Si se hace clic en Cerrar o fuera de la ventana modal, se cerrará esta y no ocurrirá ningún cambio en la información.