"""Asignatura vinculada a un objeto ProgramaAcademico."""

from modelos.programa_academico import ProgramaAcademico
from modelos.validaciones import validar_entero_positivo, validar_texto


class Asignatura:
    """Conserva el programa como objeto, no como una copia de su nombre."""

    def __init__(self, codigo, nombre, creditos, programa):
        self.set_codigo(codigo)
        self.set_nombre(nombre)
        self.set_creditos(creditos)
        self.set_programa(programa)

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = validar_texto(codigo, "El código de la asignatura")

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = validar_texto(nombre, "El nombre de la asignatura")

    def get_creditos(self):
        return self.__creditos

    def set_creditos(self, creditos):
        """Solo admite una cantidad entera y positiva de créditos."""
        self.__creditos = validar_entero_positivo(creditos, "Los créditos")

    def get_programa(self):
        return self.__programa

    def set_programa(self, programa):
        # Esta comprobación valida una asociación; no selecciona comportamientos.
        if not isinstance(programa, ProgramaAcademico):
            raise ValueError("El programa debe ser un objeto ProgramaAcademico.")
        self.__programa = programa

    def mostrar_informacion(self):
        return (f"Asignatura: {self.__codigo} - {self.__nombre}\n"
                f"Número de créditos: {self.__creditos}\n"
                f"Programa: {self.__programa.get_nombre()}")
