"""Especialización de Persona para estudiantes."""

from modelos.persona import Persona
from modelos.programa_academico import ProgramaAcademico
from modelos.validaciones import (
    validar_entero_positivo, validar_promedio, validar_texto,
)


class Estudiante(Persona):
    """Reutiliza los datos generales y añade la información estudiantil."""

    def __init__(self, identificacion, nombre, correo, codigo_estudiantil,
                 programa, semestre, promedio):
        super().__init__(identificacion, nombre, correo)
        self.set_codigo_estudiantil(codigo_estudiantil)
        self.set_programa(programa)
        self.set_semestre(semestre)
        self.set_promedio(promedio)

    def get_codigo_estudiantil(self):
        return self.__codigo_estudiantil

    def set_codigo_estudiantil(self, codigo):
        self.__codigo_estudiantil = validar_texto(codigo, "El código estudiantil")

    def get_programa(self):
        return self.__programa

    def set_programa(self, programa):
        if not isinstance(programa, ProgramaAcademico):
            raise ValueError("El programa debe ser un objeto ProgramaAcademico.")
        self.__programa = programa

    def get_semestre(self):
        return self.__semestre

    def set_semestre(self, semestre):
        self.__semestre = validar_entero_positivo(semestre, "El semestre")

    def get_promedio(self):
        return self.__promedio

    def set_promedio(self, promedio):
        self.__promedio = validar_promedio(promedio)

    def actualizar_avance_academico(self, semestre, promedio):
        """Actualiza ambos datos solo cuando los dos valores son válidos.

        Si alguna validación falla, conserva el semestre y el promedio previos.
        Reutiliza las mismas reglas de los setters individuales.
        """
        nuevo_semestre = validar_entero_positivo(semestre, "El semestre")
        nuevo_promedio = validar_promedio(promedio)
        # Ningún atributo cambia hasta terminar las dos validaciones.
        self.__semestre = nuevo_semestre
        self.__promedio = nuevo_promedio

    def mostrar_informacion(self):
        """Sobrescribe el método y amplía los datos obtenidos de Persona."""
        return (f"ESTUDIANTE\n{super().mostrar_informacion()}\n"
                f"Código estudiantil: {self.__codigo_estudiantil}\n"
                f"Programa: {self.__programa.get_nombre()}\n"
                f"Semestre: {self.__semestre}\n"
                f"Promedio acumulado: {self.__promedio:.2f}")

    def realizar_actividad_principal(self):
        return (f"{self.get_nombre()} cursa {self.__programa.get_nombre()} "
                f"y se encuentra en el semestre {self.__semestre}.")
