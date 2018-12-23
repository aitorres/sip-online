# Sistema de Inscripción de Postgrado Online (SIP)

Repositorio del Sistema de Inscripción de Postgrado Online, proyecto de desarrollo de la asignatura **Ingeniería de Software I (CI-3715)** durante el trimestre *Septiembre-Diciembre 2018* en la **Universidad Simón Bolívar**.

## Sobre el SIP Online

El Sistema de Inscripción de Postgrado Online es un sistema de gestión de profesores, asignaturas y trámites de inscripción trimestral para los estudiantes de postgrado. Permite gestionar la información necesaria para realizar la planificación trimestral a nivel de Departamento, consignar las disponibilidades horarias de los profesores, y permitir a los estudiantes el acceso a los trámites de manera digital, fácil, rápida y eficiente.

### Funcionalidades

Actualmente, el SIP Online permite:

- Gestionar los profesores de postgrado de un departamento (listar, ver detalles, agregar, modificar, eliminar)
- Gestionar las asignaturas de postgrado de un departamento (listar, ver detalles, agregar, modificar, eliminar)
- Realizar, como Jefe de Departamento, la asignacion profesoral de la oferta.
- Seleccionar, como Profesor, las preferencias sobre las asignaturas a ser ofertadas.
- Declarar las ofertas como preliminares o finales
- Editar asignaciones de profesores y agregarlas o quitarlas de una oferta
- Modificar las ofertas finales para incorporar nuevas asignaturas o nuevos profesores.
- Enviar a las Coordinaciones la oferta que requieran según las asignaturas que necesiten para sus carreras
- Ver y discutir entre Jefe de Departamento y Coordinador las ofertas trimestrales finales en Mesas de Negociación tipo chat.

### Desarrollo

El SIP Online se encuentra en desarrollo actualmente. El desarrollo se hace utilizando *Python 3.6.6* y *Django 1.11.15*. El resto de requerimientos se encuentran en el [archivo de requerimientos (requirements.txt)](requirements.txt).

## Documentación

La documentación del SIP Online se encuentra repartida en los siguientes lugares:

- **Comentarios del código**, que aseguran la legibilidad del mismo siguiendo todos los estándares de calidad y convenciones de redacción de comentarios para Python y Django.
- **Guía del usuario**, documento de fácil lectura y acompañado de guías visuales para entender las funcionalidades del sistema, disponible aquí: [guía del usuario](docs/GUIA-USUARIO.md).
- **Guía del programador**, documento técnico con detalles de implementación y scripts para comprender los detalles de diseño y código del sistema, disponible aquí:  [guía del programador](docs/GUIA-PROGRAMADOR.md).

Estos artefactos de documentación se irán actualizando progresivamente conforme se desarrolle el sistema.

## Pruebas

El sistema tiene una serie de suites y casos de prueba alojados en el archivo [*gestion/tests.py*](gestion/tests.py), que se pueden ejecutar con el siguiente comando en el terminal:

```bash
python manage.py test
```

Las pruebas verifican integridad de modelos, métodos adicionales y algunos controladores con sus respuestas, para garantizar la calidad del código del producto.

## Autores

Equipo de desarrollo de software **BIG Developers**.

- Andrés Ignacio Torres (14-11082)
- Javier Medina (12-10400)
- Mariagabriela Jaimes (14-10526)
- María Grimaldi (14-10444)
- Francisco Marcos (11-10569)
- Javier Vivas (12-11067)
- Julio Pérez (14-10820)
- Giacomo Tosone (14-11085)

## Contacto

Puede contactar al líder del equipo, Andrés Ignacio Torres, a través de su correo institucional 14-11082@usb.ve.
