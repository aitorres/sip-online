# encoding=utf-8

"""
Módulo de pruebas unitarias para el entorno de desarrollo Django
que utiliza una versión de PyUnit adaptada al framework y
ya incluida para realizar las pruebas de los modelos y funciones
asociadas.
"""

from django.test import TestCase
from gestion.models import Profesor, Departamento, Asignatura

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
        PRUEBA 1. Se verifica que se guarde el nombre del profesor
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
        PRUEBA 2. Se verifica que se guarde el apellido del profesor
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
        PRUEBA 3. Se verifica que se guarde el correo electrónico (email) del
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
        PRUEBA 4. Se verifica que la representación como cadena de caracteres
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

        dpto_qm = Departamento.objects.create(
            nombre="Departamento de Química",
            codigo="QM",
        )        

    def test_nombre_departamento(self):
        """
        PRUEBA 1. Se verifica que el nombre del Departamento se guarde
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
        PRUEBA 2. Se verifica que el código del Departamento se guarde
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
        PRUEBA 3. Se verifica que se asocie la cuenta de un profesor
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
        PRUEBA 4. Se verifica que la representación como cadena de caracteres
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
        PRUEBA 5. Verifica que el método "tiene_jefe()" del modelo Departamento
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
        PRUEBA 6. Verifica la coherencia en la jefatura de un Departamento, dada por la
        función jefe_coherente(), que chequea si el departamento al que está asociado
        el jefe es el departamento que dirige.

        PRIMERA CORRIDA: Falla porque el modelo Departamento no tiene el método dado.
        SIGUIENTE CORRIDA: La prueba pasa porque se creó el método requerido.
        """

        dpto_ci = Departamento.objects.get(codigo="CI")
        dpto_qm = Departamento.objects.get(codigo="QM")

        self.assertTrue(dpto_ci.jefe_coherente())
        self.assertRaises(ValueError, dpto_qm.jefe_coherente)

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
            nombre="Ingeniería de Software I",
            codigo_interno="3715",
            departamento=dpto_compu
        )

    def test_nombre_asignatura(self):
        """
        PRUEBA 1. Se verifica que el nombre de la Asignatura se guarde
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
        PRUEBA 2. Se verifica que el código interno de la Asignatura se guarde
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
        PRUEBA 3. Se verifica que se asocie un Departamento ya existente
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
        PRUEBA 4. Se verifica que la representación como cadena de caracteres
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
        PRUEBA 5. Verifica que el método codigo_completo() de Asignatura devuelva
        el código correcto de la asignatura.

        PRIMERA CORRIDA: Falla porque el método no existe aún.
        """

        asignatura = Asignatura.objects.get(codigo_interno="3715")
        self.assertEqual(
            asignatura.codigo_completo(),
            "CI3715"
        )
