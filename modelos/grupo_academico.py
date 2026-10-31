"""Oferta de una asignatura con docente, cupos, estudiantes y horario propio."""

from excepciones import (
    CapacidadMaximaError, EstudianteNoMatriculadoError,
    EstudianteYaMatriculadoError,
)
from modelos.asignatura import Asignatura
from modelos.docente import Docente
from modelos.estudiante import Estudiante
from modelos.horario import Horario
from modelos.validaciones import validar_entero_positivo, validar_texto


class GrupoAcademico:
    """Asocia objetos existentes y construye internamente su propio Horario."""

    def __init__(self, codigo, asignatura, docente, capacidad_maxima,
                 dia, hora_inicio, hora_fin, salon):
        self.__codigo = validar_texto(codigo, "El código del grupo")
        if not isinstance(asignatura, Asignatura):
            raise ValueError("La asignatura debe ser un objeto Asignatura.")
        if not isinstance(docente, Docente):
            raise ValueError("El docente debe ser un objeto Docente.")
        self.__asignatura = asignatura
        self.__docente = docente
        self.__capacidad_maxima = validar_entero_positivo(
            capacidad_maxima, "La capacidad máxima"
        )
        self.__estudiantes = []
        self.__horario = Horario(dia, hora_inicio, hora_fin, salon)

    def get_codigo(self):
        return self.__codigo

    def get_asignatura(self):
        return self.__asignatura

    def get_docente(self):
        return self.__docente

    def get_capacidad_maxima(self):
        return self.__capacidad_maxima

    def get_estudiantes(self):
        """Devuelve una copia de la lista para proteger las matrículas."""
        return self.__estudiantes.copy()

    def get_horario(self):
        return self.__horario

    def get_cupos_disponibles(self):
        return self.__capacidad_maxima - len(self.__estudiantes)

    def cambiar_horario(self, dia, hora_inicio, hora_fin, salon):
        """Reemplaza el horario solo si el nuevo objeto se construye sin error."""
        self.__horario = Horario(dia, hora_inicio, hora_fin, salon)

    def matricular_estudiante(self, estudiante):
        if not isinstance(estudiante, Estudiante):
            raise ValueError("Solo se puede matricular un objeto Estudiante.")
        codigo = estudiante.get_codigo_estudiantil()
        for matriculado in self.__estudiantes:
            if matriculado.get_codigo_estudiantil() == codigo:
                raise EstudianteYaMatriculadoError(
                    f"El estudiante {codigo} ya está matriculado en {self.__codigo}."
                )
        # El duplicado se comprueba antes del cupo para informar la causa precisa.
        if self.get_cupos_disponibles() == 0:
            raise CapacidadMaximaError(
                f"El grupo {self.__codigo} alcanzó su capacidad máxima "
                f"de {self.__capacidad_maxima} estudiantes."
            )
        self.__estudiantes.append(estudiante)

    def retirar_estudiante(self, codigo_estudiantil):
        codigo = validar_texto(codigo_estudiantil, "El código estudiantil")
        for estudiante in self.__estudiantes:
            if estudiante.get_codigo_estudiantil() == codigo:
                self.__estudiantes.remove(estudiante)
                return estudiante
        raise EstudianteNoMatriculadoError(
            f"El estudiante {codigo} no está matriculado en {self.__codigo}."
        )

    def mostrar_estudiantes(self):
        if not self.__estudiantes:
            return "No hay estudiantes matriculados."
        lineas = []
        for estudiante in self.__estudiantes:
            lineas.append(
                f"{estudiante.get_codigo_estudiantil()} - {estudiante.get_nombre()}"
            )
        return "\n".join(lineas)

    def mostrar_informacion_grupo(self):
        return (f"Grupo: {self.__codigo}\n"
                f"Asignatura: {self.__asignatura.get_codigo()} - "
                f"{self.__asignatura.get_nombre()}\n"
                f"Docente: {self.__docente.get_nombre()}\n"
                f"Capacidad máxima: {self.__capacidad_maxima}\n"
                f"Matriculados: {len(self.__estudiantes)}\n"
                f"Cupos disponibles: {self.get_cupos_disponibles()}\n"
                f"Horario: {self.__horario.mostrar_informacion()}")
