"""Verifica los requisitos y que los errores no dañen datos válidos.

Ejecutar: python -m unittest discover -s pruebas -v
"""

from contextlib import redirect_stdout
from io import StringIO
import unittest

from main import crear_datos_demo, main, mostrar_reporte
from modelos.administrativo import Administrativo
from modelos.asignatura import Asignatura
from modelos.docente import Docente
from modelos.estudiante import Estudiante
from modelos.persona import Persona
from modelos.programa_academico import ProgramaAcademico


class PruebasSistema(unittest.TestCase):
    """Casos de aceptación y validaciones sobre objetos reales del sistema."""

    def setUp(self):
        self.programas, self.asignaturas, self.personas = crear_datos_demo()

    def test_catalogo_relacionado_con_programas(self):
        self.assertEqual(len(self.programas), 2)
        self.assertEqual(len(self.asignaturas), 3)
        self.assertIs(self.asignaturas[0].get_programa(), self.programas[0])
        self.assertIs(self.personas[0].get_programa(), self.programas[0])
        # Una actualización del programa se refleja en los objetos asociados.
        self.programas[0].set_nombre("Analítica de Datos Aplicada")
        self.assertIn("Analítica de Datos Aplicada",
                      self.asignaturas[0].mostrar_informacion())
        self.assertIn("Analítica de Datos Aplicada",
                      self.personas[0].mostrar_informacion())

    def test_seis_personas_dos_por_tipo_y_herencia(self):
        self.assertEqual(len(self.personas), 6)
        # Contar tipos es una comprobación de la prueba, no el reporte polimórfico.
        for clase in (Estudiante, Docente, Administrativo):
            self.assertEqual(sum(type(p) is clase for p in self.personas), 2)
        for persona in self.personas:
            self.assertIsInstance(persona, Persona)

    def test_constructores_y_campos_requeridos(self):
        persona = Persona("P001", "Persona de ejemplo", "persona@example.com")
        self.assertEqual(persona.get_identificacion(), "P001")
        self.assertEqual(persona.get_nombre(), "Persona de ejemplo")
        self.assertEqual(persona.get_correo(), "persona@example.com")
        self.assertEqual(self.personas[0].get_codigo_estudiantil(), "EST001")
        self.assertEqual(self.personas[0].get_semestre(), 2)
        self.assertEqual(self.personas[0].get_promedio(), 4.2)
        self.assertEqual(self.personas[1].get_numero_empleado(), "DOC001")
        self.assertEqual(self.personas[1].get_facultad(), "Ciencias e Ingenierías")
        self.assertEqual(self.personas[1].get_tipo_contratacion(), "Tiempo completo")
        self.assertEqual(self.personas[1].get_horas_semanales(), 40)
        self.assertEqual(self.personas[2].get_numero_empleado(), "ADM001")
        self.assertEqual(self.personas[2].get_dependencia(), "Registro Académico")
        self.assertEqual(self.personas[2].get_cargo(), "Coordinadora")
        self.assertEqual(self.personas[2].get_jornada(), "Diurna")
        self.assertEqual(self.programas[0].get_codigo(), "PAD")
        self.assertEqual(self.programas[0].get_semestres(), 8)
        self.assertEqual(self.asignaturas[0].get_codigo(), "PROG1")
        self.assertEqual(self.asignaturas[0].get_creditos(), 3)

    def test_modificaciones_validas(self):
        self.personas[0].set_correo("nuevo@example.com")
        self.programas[0].set_semestres(10)
        self.asignaturas[0].set_creditos(5)
        self.assertEqual(self.personas[0].get_correo(), "nuevo@example.com")
        self.assertEqual(self.programas[0].get_semestres(), 10)
        self.assertEqual(self.asignaturas[0].get_creditos(), 5)

    def test_correo_invalido_conserva_dato_anterior(self):
        persona = self.personas[0]
        anterior = persona.get_correo()
        for valor in ("", "   ", None, 123):
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    persona.set_correo(valor)
                self.assertEqual(persona.get_correo(), anterior)

    def test_semestres_invalidos_conservan_dato_anterior(self):
        programa = self.programas[0]
        anterior = programa.get_semestres()
        for valor in (0, -1, 2.5, "8", True, None):
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    programa.set_semestres(valor)
                self.assertEqual(programa.get_semestres(), anterior)

    def test_creditos_invalidos_conservan_dato_anterior(self):
        asignatura = self.asignaturas[0]
        anterior = asignatura.get_creditos()
        for valor in (0, -2, 1.5, "3", False, None):
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    asignatura.set_creditos(valor)
                self.assertEqual(asignatura.get_creditos(), anterior)

    def test_constructores_rechazan_datos_invalidos(self):
        with self.assertRaises(ValueError):
            Persona("P001", "Nombre", "")
        with self.assertRaises(ValueError):
            ProgramaAcademico("P", "Programa", "Facultad", 0)
        with self.assertRaises(ValueError):
            Asignatura("A", "Asignatura", 0, self.programas[0])

    def test_asociacion_rechaza_un_nombre_en_lugar_de_objeto(self):
        for objeto in (self.personas[0], self.asignaturas[0]):
            anterior = objeto.get_programa()
            with self.assertRaises(ValueError):
                objeto.set_programa("Ingeniería")
            self.assertIs(objeto.get_programa(), anterior)

    def test_reglas_adicionales_y_limites(self):
        estudiante = self.personas[0]
        for valor in (0, 5):
            estudiante.set_promedio(valor)
            self.assertEqual(estudiante.get_promedio(), valor)
        for valor in (-0.1, 5.1, True, "4.0", float("nan"), float("inf")):
            with self.subTest(promedio=valor):
                with self.assertRaises(ValueError):
                    estudiante.set_promedio(valor)
                self.assertEqual(estudiante.get_promedio(), 5)
        with self.assertRaises(ValueError):
            estudiante.set_semestre(0)
        with self.assertRaises(ValueError):
            self.personas[1].set_horas_semanales(0)
        with self.assertRaises(ValueError):
            self.personas[2].set_cargo(" ")

    def test_informacion_particular_y_actividades(self):
        estudiante, docente, administrativo = self.personas[:3]
        for campo in ("E001", "Ana Torres", "ana@example.com", "EST001",
                      "Ingeniería en Analítica de Datos", "Semestre: 2", "4.20"):
            self.assertIn(campo, estudiante.mostrar_informacion())
        for campo in ("D001", "Laura Méndez", "laura@example.com", "DOC001",
                      "Ciencias e Ingenierías", "Tiempo completo", "40"):
            self.assertIn(campo, docente.mostrar_informacion())
        for campo in ("A001", "Diana López", "diana@example.com", "ADM001",
                      "Registro Académico", "Coordinadora", "Diurna"):
            self.assertIn(campo, administrativo.mostrar_informacion())
        self.assertIn("cursa Ingeniería", estudiante.realizar_actividad_principal())
        self.assertIn("semestre 2", estudiante.realizar_actividad_principal())
        self.assertIn("orienta clases", docente.realizar_actividad_principal())
        self.assertIn("Ciencias e Ingenierías", docente.realizar_actividad_principal())
        self.assertIn("Coordinadora", administrativo.realizar_actividad_principal())
        self.assertIn("Registro Académico",
                      administrativo.realizar_actividad_principal())

    def test_reporte_admite_una_nueva_subclase_sin_modificarse(self):
        # Subclase local de prueba: demuestra que el reporte no depende de tipos.
        class Invitado(Persona):
            def mostrar_informacion(self):
                return "INFORMACIÓN DEL INVITADO"

            def realizar_actividad_principal(self):
                return "ACTIVIDAD DEL INVITADO"

        invitado = Invitado("I001", "Invitado", "invitado@example.com")
        salida = StringIO()
        with redirect_stdout(salida):
            mostrar_reporte(self.personas + [invitado])
        resultado = salida.getvalue()
        self.assertEqual(resultado.count("Actividad principal:"), 7)
        self.assertIn("INFORMACIÓN DEL INVITADO", resultado)
        self.assertIn("ACTIVIDAD DEL INVITADO", resultado)

    def test_ejecucion_completa_informa_errores_y_continua(self):
        salida = StringIO()
        with redirect_stdout(salida):
            main()
        resultado = salida.getvalue()
        self.assertEqual(resultado.count("RECHAZADO -"), 3)
        self.assertIn("Correo conservado: ana.torres@example.com", resultado)
        self.assertIn("Semestres conservados: 9", resultado)
        self.assertIn("Créditos conservados: 4", resultado)
        self.assertEqual(resultado.count("Actividad principal:"), 6)
        self.assertEqual(resultado.count("ESTUDIANTE\n"), 2)
        self.assertEqual(resultado.count("DOCENTE\n"), 2)
        self.assertEqual(resultado.count("ADMINISTRATIVO\n"), 2)


if __name__ == "__main__":
    unittest.main()
