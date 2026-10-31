"""Pruebas de abstracción, composición, matrícula y búsquedas de AC2."""

from contextlib import redirect_stdout
from io import StringIO
import unittest

from excepciones import (
    AsignaturaNoEncontradaError, CapacidadMaximaError, ErrorAcademico,
    EstudianteNoMatriculadoError, EstudianteYaMatriculadoError,
    ProgramaNoEncontradoError,
)
from main import crear_datos_demo, demostrar_grupos, main
from modelos.catalogo_academico import CatalogoAcademico
from modelos.estudiante import Estudiante
from modelos.grupo_academico import GrupoAcademico
from modelos.horario import Horario
from modelos.persona import Persona


class PruebasActividadDos(unittest.TestCase):
    def setUp(self):
        self.programas, self.asignaturas, self.personas = crear_datos_demo()
        self.ana, self.carlos = self.personas[0], self.personas[3]
        self.grupo = self.crear_grupo()
        self.catalogo = CatalogoAcademico(self.programas, self.asignaturas)

    def crear_grupo(self, **cambios):
        datos = dict(codigo="G1", asignatura=self.asignaturas[0],
                     docente=self.personas[1], capacidad_maxima=1,
                     dia="Lunes", hora_inicio="08:00", hora_fin="10:00", salon="A101")
        datos.update(cambios)
        return GrupoAcademico(**datos)

    def test_persona_no_se_puede_instanciar(self):
        with self.assertRaises(TypeError):
            Persona("P1", "Nombre", "correo@example.com")

    def test_subclase_sin_metodo_abstracto_no_se_puede_instanciar(self):
        class PersonaIncompleta(Persona):
            pass

        with self.assertRaises(TypeError):
            PersonaIncompleta("P1", "Nombre", "correo@example.com")

    def test_subclases_concretas_conservan_comportamientos_distintos(self):
        respuestas = [persona.realizar_actividad_principal()
                      for persona in self.personas[:3]]
        self.assertIn("cursa", respuestas[0])
        self.assertIn("orienta clases", respuestas[1])
        self.assertIn("desempeña el cargo", respuestas[2])

    def test_grupos_comparten_asignatura_pero_tienen_horarios_propios(self):
        otro = self.crear_grupo(codigo="G2")
        self.assertIs(self.grupo.get_asignatura(), self.asignaturas[0])
        self.assertIs(otro.get_asignatura(), self.grupo.get_asignatura())
        self.assertIs(self.grupo.get_docente(), self.personas[1])
        self.assertIsInstance(self.grupo.get_horario(), Horario)
        self.assertIsNot(self.grupo.get_horario(), otro.get_horario())
        self.grupo.cambiar_horario("Martes", "09:00", "11:00", "A102")
        self.assertEqual(otro.get_horario().get_dia(), "Lunes")
        self.assertEqual(self.grupo.get_horario().get_dia(), "Martes")

    def test_grupo_consulta_los_objetos_asociados_actuales(self):
        self.asignaturas[0].set_nombre("Programación aplicada")
        self.personas[1].set_nombre("Docente actualizado")
        texto = self.grupo.mostrar_informacion_grupo()
        self.assertIn("Programación aplicada", texto)
        self.assertIn("Docente actualizado", texto)

    def test_grupo_valida_asociaciones_capacidad_y_codigo(self):
        casos = [dict(asignatura="PROG1"), dict(docente="Laura"),
                 dict(docente=self.ana), dict(codigo=" ")]
        casos += [dict(capacidad_maxima=v) for v in (0, -1, True, 1.5, "2")]
        for datos in casos:
            with self.subTest(datos=datos):
                with self.assertRaises(ValueError):
                    self.crear_grupo(**datos)

    def test_horario_valido_y_campos_consultables(self):
        horario = Horario(" lunes ", "00:00", "23:59", " A101 ")
        self.assertEqual(horario.get_dia(), "Lunes")
        self.assertEqual(horario.get_hora_inicio(), "00:00")
        self.assertEqual(horario.get_hora_fin(), "23:59")
        self.assertEqual(horario.get_salon(), "A101")
        self.assertIn("Lunes, 00:00 a 23:59, salón A101", horario.mostrar_informacion())

    def test_horario_rechaza_dia_salon_formato_e_intervalos_invalidos(self):
        casos = [dict(dia="Feriado"), dict(salon=" "), dict(hora_inicio="8:00"),
                 dict(hora_inicio="24:00"), dict(hora_fin="10:60"),
                 dict(hora_fin="08:00"), dict(hora_fin="07:00"),
                 dict(hora_inicio=None), dict(hora_fin="10:00:00")]
        for datos in casos:
            with self.subTest(datos=datos):
                with self.assertRaises(ValueError):
                    self.crear_grupo(**datos)

    def test_cambio_de_horario_invalido_conserva_el_anterior(self):
        anterior = self.grupo.get_horario()
        with self.assertRaises(ValueError):
            self.grupo.cambiar_horario("Martes", "14:00", "12:00", "A102")
        self.assertIs(self.grupo.get_horario(), anterior)

    def test_matricula_correcta_conserva_referencia_y_ocupa_cupo(self):
        self.grupo.matricular_estudiante(self.ana)
        self.assertIs(self.grupo.get_estudiantes()[0], self.ana)
        self.assertEqual(self.grupo.get_cupos_disponibles(), 0)
        self.assertIn("EST001 - Ana Torres", self.grupo.mostrar_estudiantes())
        self.assertIn("Matriculados: 1", self.grupo.mostrar_informacion_grupo())

    def test_duplicado_mismo_objeto_y_mismo_codigo_no_alteran_el_grupo(self):
        self.grupo.matricular_estudiante(self.ana)
        otro_objeto = Estudiante("E099", "Otra ficha", "otra@example.com",
                                 "EST001", self.programas[0], 1, 4)
        for estudiante in (self.ana, otro_objeto):
            with self.subTest(estudiante=estudiante):
                with self.assertRaises(EstudianteYaMatriculadoError):
                    self.grupo.matricular_estudiante(estudiante)
                self.assertEqual(self.grupo.get_estudiantes(), [self.ana])
                self.assertEqual(self.grupo.get_cupos_disponibles(), 0)

    def test_exceso_de_capacidad_no_agrega_al_estudiante(self):
        self.grupo.matricular_estudiante(self.ana)
        with self.assertRaises(CapacidadMaximaError):
            self.grupo.matricular_estudiante(self.carlos)
        self.assertEqual(self.grupo.get_estudiantes(), [self.ana])

    def test_retiro_devuelve_el_objeto_y_permite_otra_matricula(self):
        self.grupo.matricular_estudiante(self.ana)
        retirado = self.grupo.retirar_estudiante(" EST001 ")
        self.assertIs(retirado, self.ana)
        self.assertEqual(self.grupo.get_cupos_disponibles(), 1)
        self.assertEqual(self.ana.get_nombre(), "Ana Torres")
        self.grupo.matricular_estudiante(self.carlos)
        self.assertEqual(self.grupo.get_estudiantes(), [self.carlos])

    def test_retiro_inexistente_no_modifica_matriculas(self):
        self.grupo.matricular_estudiante(self.ana)
        with self.assertRaises(EstudianteNoMatriculadoError):
            self.grupo.retirar_estudiante("EST999")
        self.assertEqual(self.grupo.get_estudiantes(), [self.ana])

    def test_grupo_vacio_se_puede_consultar_y_rechaza_retiro(self):
        self.assertEqual(self.grupo.mostrar_estudiantes(), "No hay estudiantes matriculados.")
        with self.assertRaises(EstudianteNoMatriculadoError):
            self.grupo.retirar_estudiante("EST001")

    def test_matricula_rechaza_nombre_o_persona_de_otro_rol(self):
        for valor in ("Ana", self.personas[1], None):
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    self.grupo.matricular_estudiante(valor)
        self.assertEqual(self.grupo.get_estudiantes(), [])

    def test_lista_de_consulta_no_permite_modificar_matriculas(self):
        self.grupo.matricular_estudiante(self.ana)
        copia = self.grupo.get_estudiantes()
        copia.clear()
        copia.append(self.carlos)
        self.assertEqual(self.grupo.get_estudiantes(), [self.ana])

    def test_matriculas_de_dos_grupos_son_independientes(self):
        otro = self.crear_grupo(codigo="G2")
        self.grupo.matricular_estudiante(self.ana)
        otro.matricular_estudiante(self.ana)
        self.grupo.retirar_estudiante("EST001")
        self.assertEqual(self.grupo.get_estudiantes(), [])
        self.assertEqual(otro.get_estudiantes(), [self.ana])

    def test_busquedas_validas_devuelven_objetos_originales(self):
        self.assertIs(self.catalogo.buscar_asignatura(" PROG1 "), self.asignaturas[0])
        self.assertIs(self.catalogo.buscar_programa("PAD"), self.programas[0])

    def test_asignatura_inexistente_lanza_excepcion_y_permite_buscar_despues(self):
        with self.assertRaises(AsignaturaNoEncontradaError):
            self.catalogo.buscar_asignatura("NO-EXISTE")
        self.assertIs(self.catalogo.buscar_asignatura("PROG1"), self.asignaturas[0])

    def test_programa_inexistente_lanza_excepcion_y_permite_buscar_despues(self):
        with self.assertRaises(ProgramaNoEncontradoError):
            self.catalogo.buscar_programa("NO-EXISTE")
        self.assertIs(self.catalogo.buscar_programa("PAD"), self.programas[0])

    def test_catalogo_vacio_lanza_las_excepciones_correspondientes(self):
        vacio = CatalogoAcademico([], [])
        with self.assertRaises(AsignaturaNoEncontradaError):
            vacio.buscar_asignatura("A")
        with self.assertRaises(ProgramaNoEncontradoError):
            vacio.buscar_programa("P")

    def test_catalogo_copia_las_listas_y_valida_los_objetos(self):
        self.programas.clear()
        self.asignaturas.clear()
        self.assertEqual(self.catalogo.buscar_programa("PAD").get_codigo(), "PAD")
        self.assertEqual(self.catalogo.buscar_asignatura("PROG1").get_codigo(), "PROG1")
        with self.assertRaises(ValueError):
            CatalogoAcademico(["PAD"], [])
        with self.assertRaises(ValueError):
            CatalogoAcademico([], ["PROG1"])

    def test_excepciones_personalizadas_son_clases_propias(self):
        clases = (EstudianteYaMatriculadoError, CapacidadMaximaError,
                  EstudianteNoMatriculadoError, AsignaturaNoEncontradaError,
                  ProgramaNoEncontradoError)
        self.assertEqual(len(set(clases)), 5)
        for clase in clases:
            self.assertTrue(issubclass(clase, ErrorAcademico))

    def test_demostracion_de_grupos_termina_con_estado_coherente(self):
        with redirect_stdout(StringIO()):
            grupos = demostrar_grupos(self.programas, self.asignaturas, self.personas)
        self.assertEqual(len(grupos), 2)
        self.assertEqual(grupos[0].get_estudiantes(), [self.carlos])
        self.assertEqual(grupos[1].get_estudiantes(), [self.carlos])
        self.assertEqual(grupos[0].get_cupos_disponibles(), 0)
        self.assertEqual(grupos[1].get_cupos_disponibles(), 1)

    def test_main_captura_cada_excepcion_y_continua(self):
        salida = StringIO()
        with redirect_stdout(salida):
            main()
        texto = salida.getvalue()
        nombres = ("PersonaAbstracta", "EstudianteYaMatriculadoError",
                   "CapacidadMaximaError", "EstudianteNoMatriculadoError",
                   "AsignaturaNoEncontradaError", "ProgramaNoEncontradoError")
        for nombre in nombres:
            marca = f"CONTROLADO - {nombre}:"
            self.assertEqual(texto.count(marca), 1)
            self.assertIn("CONTINÚA:", texto.split(marca, 1)[1].split("\n", 2)[1])
        self.assertIn("RETIRO CORRECTO: EST001", texto)
        self.assertIn("FIN: demostración completada", texto)
        self.assertEqual(texto.count("Actividad principal:"), 6)


if __name__ == "__main__":
    unittest.main()
