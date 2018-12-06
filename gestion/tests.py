# encoding=utf-8
from django.core.exceptions import ObjectDoesNotExist
"""
Módulo de pruebas unitarias para el entorno de desarrollo Django
que utiliza una versión de PyUnit adaptada al framework y
ya incluida para realizar las pruebas de los modelos y funciones
asociadas.
"""

from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.db import IntegrityError
from gestion.models import Profesor, Departamento, Asignatura, Disponibilidad, OfertaTrimestral
from gestion.views import (
    Dashboard,
    AgregarProfesor,
    EditarProfesor,
    ListarProfesores,
    VerProfesor,
    EliminarProfesor
)

class ControladoresTest(TestCase):
    """
    Suite de pruebas para los distintos controladores, de manera que se pueda
    comprobar que están retornando los valores de código de respuesta (response)
    apropiados para su funcionamiento.
    """

    def setUp(self):
        """
        Método para crear los valores de la base de datos por defecto
        antes de iniciar cada prueba y los métodos que debe utilizar
        de manera especial para probar vistas.
        """

        # Creamos un deparatmento y procedemos a crear un profesor
        # asociado a ese departamento

        dpto_compu = Departamento.objects.create(
            nombre="Departamento de Computación y Tecnología de la Información",
            codigo="CI",
        )

        self.prof = Profesor.objects.create(
            nombre="Andrés",
            apellido="Medina",
            email="14-11082@usb.ve",
            cedula="V-22.252.123",
            departamento=dpto_compu
        )

        # Asociamos valores para los métodos de prueba
        self.factory = RequestFactory()
        self.user = AnonymousUser

    def test_dashboard(self):
        """
        PRUEBA DASHBOARD. Determina si se está ejecutando correctamente el
        controlador del Dashboard y si retorna el código de respuesta esperado.

        VALOR ESPERADO: 200 (response OK)
        PRIMERA EJECUCIÓN: La prueba pasa porque la vista retorna el valor esperado.

        Este comportamiento está bien ya que estas pruebas se están agregando luego de
        que las vistas ya existan, a manera de verificación final, y no como las otras
        pruebas que sí se agregaron antes y durante la implementación de funciones
        y métodos especiales.
        """

        # Accedemos a la vista
        request = self.factory.get('/')

        # Asociamos el usuario
        request.user = self.user

        # Obtenemos la respuesta
        response = Dashboard.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_agregar_profesor(self):
        """
        PRUEBA AGREGAR PROFESOR. Determina si se está ejecutando correctamente el
        controlador del form de agregar profesor y si retorna el código de respuesta esperado.

        VALOR ESPERADO: 200 (response OK)
        PRIMERA EJECUCIÓN: La prueba pasa porque la vista retorna el valor esperado.

        Este comportamiento está bien ya que estas pruebas se están agregando luego de
        que las vistas ya existan, a manera de verificación final, y no como las otras
        pruebas que sí se agregaron antes y durante la implementación de funciones
        y métodos especiales.
        """

        # Accedemos a la vista
        request = self.factory.get('/profesores/agregar')

        # Asociamos el usuario
        request.user = self.user

        # Obtenemos la respuesta
        response = AgregarProfesor.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_listar_profesores(self):
        """
        PRUEBA LISTAR PROFESORES. Determina si se está ejecutando correctamente el
        controlador de la vista para listar profesores y si retorna el código de
        respuesta esperado.

        VALOR ESPERADO: 200 (response OK)
        PRIMERA EJECUCIÓN: La prueba pasa porque la vista retorna el valor esperado.

        Este comportamiento está bien ya que estas pruebas se están agregando luego de
        que las vistas ya existan, a manera de verificación final, y no como las otras
        pruebas que sí se agregaron antes y durante la implementación de funciones
        y métodos especiales.
        """

        # Accedemos a la vista
        request = self.factory.get('/profesores/listar')

        # Asociamos el usuario
        request.user = self.user

        # Obtenemos la respuesta
        response = ListarProfesores.as_view()(request)
        self.assertEqual(response.status_code, 200)


class ProfesorModelTest(TestCase):
    """
    Suite de pruebas para el modelo Profesor, que incluye
    pruebas de frontera, de esquina y de malicia para los atributos
    del modelo Profesor, y para sus métodos asociados en caso de
    que se agreguen posteriormente.
    """

    def setUp(self):
        """
        Método para crear los valores de la base de datos por defecto
        antes de iniciar cada prueba.
        """

        dpto_compu = Departamento.objects.create(
            nombre="Departamento de Computación y Tecnología de la Información",
            codigo="CI",
        )

        Profesor.objects.create(
            nombre="Andrés",
            apellido="Medina",
            email="14-11082@usb.ve",
            cedula="V-22.252.123",
            departamento=dpto_compu
        )
        Profesor.objects.create(
            nombre="María",
            apellido="Jaimes",
            email="12-10042@usb.ve",
            cedula="V-25.766.738",
            departamento=dpto_compu
        )


    def test_nombre_profesor(self):
        """
        PRUEBA 1 PROFESOR. Se verifica que se guarde el nombre del profesor
        en la entidad, y que luego corresponda con el nombre guardado.

        PRIMERA CORRIDA: Falla porque el modelo profesor no tiene atributos.
        SIGUIENTE CORRIDA: La prueba se ejecuta correctamente.
        """
        profesor1 = Profesor.objects.get(cedula="V-22.252.123")
        profesor2 = Profesor.objects.get(cedula="V-25.766.738")

        self.assertEqual(profesor1.nombre, "Andrés")
        self.assertEqual(profesor2.nombre, "María")

    def test_apellido_profesor(self):
        """
        PRUEBA 2 PROFESOR. Se verifica que se guarde el apellido del profesor
        en la entidad, y que luego corresponda con el apellido guardado.

        PRIMERA CORRIDA: Falla porque el modelo profesor no tiene atributos.
        SIGUIENTE CORRIDA: La prueba se ejecuta correctamente.
        """

        profesor1 = Profesor.objects.get(cedula="V-22.252.123")
        profesor2 = Profesor.objects.get(cedula="V-25.766.738")

        self.assertEqual(profesor1.apellido, "Medina")
        self.assertEqual(profesor2.apellido, "Jaimes")

    def test_email_profesor(self):
        """
        PRUEBA 3 PROFESOR. Se verifica que se guarde el correo electrónico (email) del
        profesor en la entidad, y que luego el correo guardado corresponda
        con el apellido guardado.

        PRIMERA CORRIDA: Falla porque el modelo profesor no tiene atributos.
        SIGUIENTE CORRIDA: La prueba se ejecuta correctamente.
        """

        profesor1 = Profesor.objects.get(cedula="V-22.252.123")
        profesor2 = Profesor.objects.get(cedula="V-25.766.738")

        self.assertEqual(profesor1.email, "14-11082@usb.ve")
        self.assertEqual(profesor2.email, "12-10042@usb.ve")

    def test_string_profesor(self):
        """
        PRUEBA 4 PROFESOR. Se verifica que la representación como cadena de caracteres
        del modelo Profesor sea su nonmbre y su apellido.

        PRIMERA CORRIDA: Falla porque la representación por cadena de
        caracteres (string) del modelo es la por defecto de Django.
        SIGUIENTE CORRIDA: La prueba pasa porque se genera la representación como
        cadena de caracteres apropiada.
        """

        profesor1 = Profesor.objects.get(cedula="V-22.252.123")
        profesor2 = Profesor.objects.get(cedula="V-25.766.738")

        self.assertEqual(str(profesor1), "Andrés Medina")
        self.assertEqual(str(profesor2), "María Jaimes")

class DepartamentoModelTest(TestCase):
    """
    Suite de pruebas para el modelo Departamento, que incluye
    pruebas de frontera, de esquina y de malicia para los atributos
    de este modelo, y para sus métodos asociados en caso de
    que se agreguen posteriormente.
    """

    def setUp(self):
        """
        Método para crear los valores de la base de datos por defecto
        antes de iniciar cada prueba.
        """

        dpto_compu = Departamento.objects.create(
            nombre="Departamento de Computación y Tecnología de la Información",
            codigo="CI",
        )

        jefe_compu = Profesor.objects.create(
            nombre="Ángela",
            apellido="Di Serio",
            email="adiserio@usb.ve",
            cedula="V-14.241.234",
            departamento=dpto_compu
        )

        dpto_compu.jefe = jefe_compu
        dpto_compu.save()

        Departamento.objects.create(
            nombre="Departamento de Química",
            codigo="QM",
        )

    def test_nombre_departamento(self):
        """
        PRUEBA 1 DEPARTAMENTO. Se verifica que el nombre del Departamento se guarde
        correctamente en la entidad, y que luego el nombre guardado
        corresponda al departamento.

        PRIMERA CORRIDA: Falla porque el modelo Departamento no está creado.
        SIGUIENTE CORRIDA: La prueba se ejecuta correctamente.
        """

        dpto_ci = Departamento.objects.get(codigo="CI")
        self.assertEqual(
            dpto_ci.nombre,
            "Departamento de Computación y Tecnología de la Información"
        )

    def test_codigo_departamento(self):
        """
        PRUEBA 2 DEPARTAMENTO. Se verifica que el código del Departamento se guarde
        correctamente en la base de datos, y que corresponda al código
        que se quiso almacenar.

        PRIMERA CORRIDA: Falla porque el modelo Departamento no está creado.
        SIGUIENTE CORRIDA: La prueba se ejecuta correctamente.
        """

        dpto_ci = Departamento.objects.get(codigo="CI")
        self.assertEqual(
            dpto_ci.codigo, "CI"
        )

    def test_jefe_departamento(self):
        """
        PRUEBA 3 DEPARTAMENTO. Se verifica que se asocie la cuenta de un profesor
        en la base de datos como jefe del Departamento y que sea
        el usuario que se quiso almacenar.

        PRIMERA CORRIDA: Falla porque el modelo Departamento no está creado.
        SIGUIENTE CORRIDA: La prueba se ejecuta correctamente.
        """

        dpto_ci = Departamento.objects.get(codigo="CI")
        jefe = Profesor.objects.get(email="adiserio@usb.ve")
        self.assertEqual(
            dpto_ci.jefe,
            jefe
        )

    def test_string_departamento(self):
        """
        PRUEBA 4 DEPARTAMENTO. Se verifica que la representación como cadena de caracteres
        del modelo Departamento sea su nonmbre y su código.

        PRIMERA CORRIDA: Falla porque la representación por cadena de
        caracteres (string) del modelo es la por defecto de Django.
        SIGUIENTE CORRIDA: La prueba pasa porque se genera la representación como
        cadena de caracteres apropiada.
        """

        dpto_ci = Departamento.objects.get(codigo="CI")
        self.assertEqual(str(dpto_ci), "Departamento de Computación y Tecnología de la Información (CI)")

    def test_tiene_jefe_departamento(self):
        """
        PRUEBA 5 DEPARTAMENTO. Verifica que el método "tiene_jefe()" del modelo Departamento
        devuelva el resultado apropiado, en caso de que el Departamento posea o no
        un jefe ne el momento dado.

        PRIMERA CORRIDA: Falla porque el modelo Departamento no tiene un método llamado
        como tal asociado.
        SIGUIENTE CORRIDA: La prueba pasa porque se creó el método requerido.
        """

        dpto_ci = Departamento.objects.get(codigo="CI")
        dpto_qm = Departamento.objects.get(codigo="QM")

        self.assertTrue(dpto_ci.tiene_jefe())
        self.assertFalse(dpto_qm.tiene_jefe())

    def test_jefe_coherente_departamento(self):
        """
        PRUEBA 6 DEPARTAMENTO. Verifica la coherencia en la jefatura de un Departamento, dada por la
        función jefe_coherente(), que chequea si el departamento al que está asociado
        el jefe es el departamento que dirige.

        PRIMERA CORRIDA: Falla porque el modelo Departamento no tiene el método dado.
        SIGUIENTE CORRIDA: La prueba pasa porque se creó el método requerido.
        """

        dpto_ci = Departamento.objects.get(codigo="CI")
        dpto_qm = Departamento.objects.get(codigo="QM")

        self.assertTrue(dpto_ci.jefe_coherente())
        self.assertRaises(ValueError, dpto_qm.jefe_coherente)

    def test_nombre_corto(self):
        """
        PRUEBA 7 DEPARTAMENTO. Verifica si el método para obtener el nombre corto del Departamento existe,
        y se ejecuta correctamente retornando la palabra correcta.

        PRIMERA CORRIDA: Falla porque el modelo Departamento no tiene el método dado, aún.
        """

        dpto_ci = Departamento.objects.get(codigo="CI")
        dpto_qm = Departamento.objects.get(codigo="QM")

        self.assertEqual(dpto_ci.nombre_corto(), "Computación y Tecnología de la Información (CI)")
        self.assertEqual(dpto_qm.nombre_corto(), "Química (QM)")


class AsignaturaModelTest(TestCase):
    """
    Suite de pruebas para el modelo Asignatura, que incluye
    pruebas de frontera, de esquina y de malicia para los atributos
    de este modelo, y para sus métodos asociados en caso de
    que se agreguen posteriormente.
    """

    def setUp(self):
        """
        Método para crear los valores de la base de datos por defecto
        antes de iniciar cada prueba.
        """

        dpto_compu = Departamento.objects.create(
            nombre="Departamento de Computación y Tecnología de la Información",
            codigo="CI",
        )

        jefe_compu = Profesor.objects.create(
            nombre="Ángela",
            apellido="Di Serio",
            email="adiserio@usb.ve",
            cedula="V-14.241.234",
            departamento=dpto_compu
        )

        dpto_compu.jefe = jefe_compu
        dpto_compu.save()


        Asignatura.objects.create(
            nombre="Sistema de bases de datos I",
            codigo_interno="3311",
            departamento=dpto_compu,
            horas_laboratorio=0,
            horas_teoria=4,
            horas_practica=0,
            unidad_creditos = 3
        )

        Asignatura.objects.create(
            nombre="Ingeniería de Software I",
            codigo_interno="3715",
            departamento=dpto_compu,
            horas_laboratorio=0,
            horas_teoria=4,
            horas_practica=3,
            unidad_creditos = 5,
        )

    def test_nombre_asignatura(self):
        """
        PRUEBA 1 ASIGNATURA. Se verifica que el nombre de la Asignatura se guarde
        correctamente en la entidad, y que luego el nombre guardado
        corresponda al departamento.

        PRIMERA CORRIDA: Falla porque el modelo Asignatura no está creado.
        SIGUIENTE CORRIDA: La prueba se ejecuta correctamente.
        """

        asignatura = Asignatura.objects.get(codigo_interno="3715")
        self.assertEqual(
            asignatura.nombre,
            "Ingeniería de Software I"
        )

    def test_codigo_asignatura(self):
        """
        PRUEBA 2 ASIGNATURA. Se verifica que el código interno de la Asignatura se guarde
        correctamente en la base de datos, y que corresponda al código
        que se quiso almacenar.

        PRIMERA CORRIDA: Falla porque el modelo Asignatura no está creado.
        SIGUIENTE CORRIDA: La prueba se ejecuta correctamente.
        """

        asignatura = Asignatura.objects.get(codigo_interno="3715")
        self.assertEqual(
            asignatura.codigo_interno, "3715"
        )

    def test_departamento_asignatura(self):
        """
        PRUEBA 3 ASIGNATURA. Se verifica que se asocie un Departamento ya existente
        como el departamento asociado de la Asignatura.

        PRIMERA CORRIDA: Falla porque el modelo Asignatura no está creado.
        SIGUIENTE CORRIDA: La prueba se ejecuta correctamente.
        """

        asignatura = Asignatura.objects.get(codigo_interno="3715")
        dpto_compu = Departamento.objects.get(codigo="CI")
        self.assertEqual(
            asignatura.departamento,
            dpto_compu
        )

    def test_string_asignatura(self):
        """
        PRUEBA 4 ASIGNATURA. Se verifica que la representación como cadena de caracteres
        del modelo Asignatura sea su código completo y su nombre.

        PRIMERA CORRIDA: Falla porque la representación por cadena de
        caracteres (string) del modelo es la por defecto de Django.
        SIGUIENTE CORRIDA: La prueba pasa porque se genera la representación como
        cadena de caracteres apropiada.
        """

        asignatura = Asignatura.objects.get(codigo_interno="3715")
        self.assertEqual(
            str(asignatura),
            "(CI3715) Ingeniería de Software I"
        )

    def test_codigo_completo_asignatura(self):
        """
        PRUEBA 5 ASIGNATURA. Verifica que el método codigo_completo() de Asignatura devuelva
        el código correcto de la asignatura.

        PRIMERA CORRIDA: Falla porque el método no existe aún.
        SIGUIENTE CORRIDA: La prueba pasa satisfactoriamente.
        """

        asignatura = Asignatura.objects.get(codigo_interno="3715")
        self.assertEqual(
            asignatura.codigo_completo(),
            "CI3715"
        )

    def test_horas_positivas(self):
        """
        PRUEBA 6: Se probara que los campos de horas en el modelo Asignatura
        sean mayor o igual a 0.

        PRIMERA CORRIDA: FALLA, los metodos no existen.
        SEGUNDA CORRIDA: PASA.
        """
        asignatura = Asignatura.objects.get(codigo_interno="3715")
        self.assertGreaterEqual(asignatura.horas_l(),0)
        self.assertGreaterEqual(asignatura.horas_p(),0)
        self.assertGreaterEqual(asignatura.horas_t(),0)

    def test_creditos_positivos(self):
        """
        PRUEBA 7: Se probara que el campo unidad_creditos sea siempre positivo
        PRIMERA CORRIDA: FALLA, los metodo que devuelve el valor, no exite.
        SEGUNDA CORRIDA: PASA

        """
        asignatura = Asignatura.objects.get(codigo_interno="3715")
        self.assertGreaterEqual(asignatura.creditos(),0)


class DisponibilidadModelTest(TestCase):
    """
    Suite de pruebas para el modelo Disponibilidad, que incluye unas pocas
    pruebas de frontera, de esquina y de malicia para los atributos
    de este modelo, y para sus métodos asociados en caso de
    que se agreguen posteriormente.
    """

    def setUp(self):
        """
        Método para crear los valores de la base de datos por defecto
        antes de iniciar cada prueba.
        """

        Disponibilidad.objects.create(dia=1, bloque=6)
        self.cantidad_bloques = 12

    def test_matriz_bloques(self):
        """
        PRUEBA 1 DISPONIBILIDAD. Determina si el método matriz_bloques de la Clase, no la
        instancia, se ejecuta y retorna el valor adecuado de la matriz según
        sus días y bloques.

        PRIMERA CORRIDA: Falla porque el método no existe aún en la clase Disponibilidad.
        SIGUIENTE CORRIDA: La prueba pasa satisfactoriamente.
        """

        matriz_bloques = {
            1: [1, 13, 25, 36, 49, 61],
            2: [2, 14, 26, 38, 50, 62],
            3: [3, 15, 27, 39, 51, 63],
            4: [4, 16, 28, 40, 52, 64],
            5: [5, 17, 29, 41, 53, 65],
            6: [6, 18, 30, 42, 54, 66],
            7: [7, 19, 31, 43, 55, 67],
            8: [8, 20, 32, 44, 56, 68],
            9: [9, 21, 33, 45, 57, 69],
            10: [10, 22, 34, 46, 58, 70],
            11: [11, 23, 35, 47, 59, 71],
            12: [12, 24, 36, 48, 60, 72],
        }

        self.assertEqual(
            matriz_bloques,
            Disponibilidad.matriz_bloques()
        )

    def test_string_disponibilidad(self):
        """
        PRUEBA 2 DISPONIBILIDAD. Determina si se muestra correctamente como cadena de
        caracteres una instancia de la clase Disponibilidad.

        PRIMERA CORRIDA: Falla porque el método no ha sido extendido
        en la clase Disponibilidad, y usa el str por defecto.
        SIGUIENTE CORRIDA: La prueba pasa satisfactoriamente.
        """

        disponibilidad = Disponibilidad.objects.get(dia=1, bloque=6)
        self.assertEqual(
            str(disponibilidad),
            disponibilidad.get_dia_display() + ", bloque " + str(disponibilidad.bloque)
        )

    def test_id_unico_disponibilidad(self):
        """
        PRUEBA 3 DISPONIBILIDAD. Determina si se obtiene el identificador único de una instancia
        de la clase Disponibilidad en función de la biyección entre R² y R hallada.

        PRIMERA CORRIDA: Falla porque el método no existe aún en la clase Disponibilidad.
        SIGUIENTE CORRIDA: La prueba pasa satisfactoriamente.
        """

        disponibilidad = Disponibilidad.objects.get(dia=1, bloque=6)
        self.assertEqual(
            disponibilidad.identificador_unico(),
            self.cantidad_bloques * (disponibilidad.dia-1) + disponibilidad.bloque
        )

class ModelosBDTest(TestCase):
    """
    Suite de pruebas para probar el comportamiento de los modelos como una unidad.
    Se pretende crear un conjunto de departamentos con profesores asociados y asignaturas
    dictadas por dichos profesores.
    """


    def setUp(self):
        """
        Método para crear los valores de la base de datos por defecto
        antes de iniciar cada prueba.
        """

        dpto_compu = Departamento.objects.create(
            nombre="Departamento de Computación y Tecnología de la Información",
            codigo="CI",
        )

        dpto_meca = Departamento.objects.create(
            nombre="Departamento de Mecánica",
            codigo="MC",
        )

        dpto_materiales = Departamento.objects.create(
            nombre="Departamento de Materiales",
            codigo="MT",
        )

        asignaturaCI1 = Asignatura.objects.create(
            nombre="Ingeniería de Software I",
            codigo_interno="3715",
            departamento=dpto_compu
        )

        asignaturaCI2 = Asignatura.objects.create(
            nombre="Lenguajes de programación I",
            codigo_interno="3661",
            departamento=dpto_compu
        )

        asignaturaCI3 = Asignatura.objects.create(
            nombre="Organización del computador",
            codigo_interno="3815",
            departamento=dpto_compu
        )

        asignaturaMC1 = Asignatura.objects.create(
            nombre="Mecánica computacional I",
            codigo_interno="2421",
            departamento=dpto_meca
        )

        asignaturaMC2 = Asignatura.objects.create(
            nombre="Mecánica de materiales I",
            codigo_interno="2141",
            departamento=dpto_meca
        )

        asignaturaMT = Asignatura.objects.create(
            nombre="Ciencia de los materiales",
            codigo_interno="1113",
            departamento=dpto_materiales
        )

        profesorCI = Profesor.objects.create(
            nombre="Javier",
            apellido="Medina",
            email="14-4444@usb.ve",
            cedula="V-22.252.023",
            departamento=dpto_compu
        )

        profesorCI2 = Profesor.objects.create(
            nombre="Ricardo",
            apellido="Monad",
            email="rick@usb.ve",
            cedula="V-18.555.555",
            departamento=dpto_compu
        )

        profesorMC = Profesor.objects.create(
            nombre="Luis",
            apellido="Plaza",
            email="12-10314@usb.ve",
            cedula="V-25.666.768",
            departamento=dpto_meca
        )

        profesorMC1 = Profesor.objects.create(
            nombre="Marcela",
            apellido="Fernandez",
            email="12-10315@usb.ve",
            cedula="V-25.766.738",
            departamento=dpto_meca
        )

        dpto_compu.jefe = profesorCI
        dpto_compu.save()

        dpto_meca.jefe = profesorMC
        dpto_meca.save()

        profesorCI.asignaturas.add(asignaturaCI1)
        profesorCI.asignaturas.add(asignaturaCI2)
        profesorCI.asignaturas.add(asignaturaCI3)

        profesorCI2.asignaturas.add(asignaturaCI2)

        asignaturaCI1.requisitos.add(asignaturaCI2)

        profesorMC.asignaturas.add(asignaturaMC1)
        profesorMC.asignaturas.add(asignaturaMC2)

        profesorMC1.asignaturas.add(asignaturaMT)


    # Pruebas de malicia que prueban el comportamiento de la base de datos.

    def test_dpto_sin_jefe(self):
        """
        PRUEBA BD 1: se asocia un profesor como jefe de dpto y luego se elimina el profesor. Por
        lo tanto el departamento queda sin jefe asociado. Prueba de tipo maliciosa.

        Resultado de la prueba: error se elimina el departamento al eliminar el jefe.
        SIGUIENTES CORRIDAS: pasa la prueba ya que el modelo de BD se modificó.
        """

        Profesor.objects.get(cedula="V-25.666.768").delete()
        dpto_mc = Departamento.objects.get(codigo="MC")
        self.assertFalse(dpto_mc.tiene_jefe())

    def test_dpto_nuevo_sin_jefe(self):
        """
        PRUEBA BD 1.2: se crea un departamento nuevo, y se pide que se muestre su jefe.
        Prueba de tipo maliciosa.

        Resultado de la prueba: Exitoso. Dpto sin jefe
        """
        dpto_bio = Departamento.objects.create(
            nombre="Departamento de Biologia",
            codigo="BI",
        )

        self.assertFalse(dpto_bio.tiene_jefe())

    def test_agregar_prof_ci_exitente(self):
        """
        PRUEBA BD 2: se agrega un profesor con una cedula ya registrada en la base de datos.
        Los datos del profesor varian del profesor registrado en nombre y correo. Prueba de tipo
        malicia.

        Resultado de la prueba: no se agrega el profesor porque la cedula se repite. El programa
        lanza una excepcion.
        """

        dpto_mc = Departamento.objects.get(codigo="MC")
        with self.assertRaises(IntegrityError):
            Profesor.objects.create(
                nombre="Ysabel",
                apellido="Fernandez",
                email="ysa@usb.ve",
                cedula="V-25.766.738",
                departamento=dpto_mc
            )

    def test_agregar_asig_cod_existente(self):
        """
        PRUEBA BD 3: se agrega una asignatura con codigo ya registrado en la base de datos.
        El dato de la materia que varia es el nombre.

        Resultado de la prueba: no se agrega la materia ya que el codigo ya existe. El programa
        lanza una excepcion.
        """

        dpto_ci = Departamento.objects.get(codigo="CI")
        with self.assertRaises(IntegrityError):
            Asignatura.objects.create(
                nombre="Lenguajes de programación II",
                codigo_interno="3661",
                departamento=dpto_ci
            )

    def test_agregar_dept_cod_existente(self):
        """
        PRUEBA BD 4: se agrega un departamento con codigo ya registrado en la base de datos.
        El dato del departamento que varia es el nombre. Prueba de malicia.

        Resultado de la prueba: no se agrega el departamento ya que el codigo ya existe. El programa
        lanza una excepcion.
        """

        with self.assertRaises(IntegrityError):
            Departamento.objects.create(
                nombre="Departamento de Procesos y Sistemas",
                codigo="CI",
            )

    def test_asignar_2_jefes_a_un_dpto(self):

        """
        PRUEBA BD 5: Se asigna un profesor como jefe de dos departamentos distintos.

        PRIMERA CORRIDA: Falla. No se levanta IntegrityError porque el campo es de tipo 
        FOREINGKEY sin el atributo unique=True.

        SEGUNDA CORRIDA: Pasa. Se levanta la exc, dado que jefe es un campo de tipo
        OneToOneField.
        """
        profesorCI1 = Profesor.objects.get(cedula="V-22.252.023")

        dpto_ci = Departamento.objects.get(codigo="CI")
        dpto_mc = Departamento.objects.get(codigo="MC")
        with self.assertRaises(IntegrityError):
            dpto_ci.jefe = profesorCI1
            dpto_mc.jefe = profesorCI1
            dpto_ci.save()
            dpto_mc.save()

    def test_eliminar_asignatura_requisito(self):
        """
        PRUEBA 8: Se probara que si una materia es eliminada
        se elimina tambien como requisito de alguna otra materia.

        PRIMERA CORRIDA: FALLA porque el metodo no existe.
        SEGUNDA CORRIDA: PASA.
        """
        Asignatura.objects.get(codigo_interno="3661").delete()
        asignatura2 = Asignatura.objects.get(codigo_interno="3715")
        self.assertFalse(asignatura2.tiene_requisito())

    def test_es_jefe_mismo_dpto(self):
        """
        PRUEBA 9: Se probara que un profesor es jefe de su propio departamento

        PRIMERA CORRIDA: FALLA porq no existe el metodo.
        SEGUNDA CORRIDA: PASA

        """
        dpto_ci = Departamento.objects.get(codigo="CI")
        vicente=Profesor.objects.create(
                nombre="Vicente",
                apellido="Yriarte",
                email="vy@usb.ve",
                cedula="V-9.877.999",
                departamento=dpto_ci
            )
        dpto_ci.jefe = vicente
        dpto_ci.save()
        self.assertTrue(vicente.es_jefe())

    def test_eliminar_departamento_jefe(self):
        """
        PRUEBA 10: Se probara que al borrar un departamento, el metodo no funciona.

        PRIMERA CORRIDA: PASA 
        """
        dpto_ci = Departamento.objects.get(codigo="CI")
        vicente=Profesor.objects.create(
                nombre="Vicente",
                apellido="Yriarte",
                email="vy@usb.ve",
                cedula="V-9.877.999",
                departamento=dpto_ci
            )
        dpto_ci.jefe = vicente
        dpto_ci.save()
        try:
            Departamento.objects.get(codigo="CI").delete()
            self.assertFalse(vicente.es_jefe())
        except:
            pass

    def test_cambio_dpto(self):
        """
        PRUEBA 11: Se probara que se agrega un dpto correcto y 
        luego uno incorrecto a un profesor y el metodo funciona.
        """ 
        dpto_ci = Departamento.objects.get(codigo="CI")
        dpto_mc = Departamento.objects.get(codigo="MC")
        vicente=Profesor.objects.create(
                nombre="Vicente",
                apellido="Yriarte",
                email="vy@usb.ve",
                cedula="V-9.877.999",
                departamento=dpto_ci
            )
        dpto_ci.jefe = vicente
        dpto_ci.save()
        self.assertTrue(vicente.es_jefe())
        vicente.departamento = dpto_mc
        vicente.save()
        self.assertFalse(vicente.es_jefe())

    def test_nombre_oferta(self):
        """
        PRUEBA 12: Se prueba el metodo que retorna eel nombre y el estado.
        PRIMERA CORRIDA: FALLA
        SEGUNDA CORRIDA: PASA
        """

        oferta = OfertaTrimestral.objects.create(
            trimestre="EM18",
            es_final=False
            )
        self.assertEqual(oferta.nombre_completo(),"Enero - Marzo 2018")

    def test_estado_oferta(self):
        """
        PRUEBA 13: Se prueba el campo booleano estado.
        PRIMERA CORRIDA: PASA
        """ 
        oferta = OfertaTrimestral.objects.create(
            trimestre="EM18",
            es_final=False
            )
        self.assertEqual(oferta.estado(),"preliminar")
