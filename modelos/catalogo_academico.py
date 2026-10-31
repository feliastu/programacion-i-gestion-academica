"""Búsquedas sobre los mismos programas y asignaturas de la demostración."""

from excepciones import AsignaturaNoEncontradaError, ProgramaNoEncontradoError
from modelos.asignatura import Asignatura
from modelos.programa_academico import ProgramaAcademico
from modelos.validaciones import validar_texto


class CatalogoAcademico:
    """Agrupa referencias a programas y asignaturas ya creados."""

    def __init__(self, programas, asignaturas):
        self.__programas = list(programas)
        self.__asignaturas = list(asignaturas)
        if not all(isinstance(p, ProgramaAcademico) for p in self.__programas):
            raise ValueError("El catálogo requiere objetos ProgramaAcademico.")
        if not all(isinstance(a, Asignatura) for a in self.__asignaturas):
            raise ValueError("El catálogo requiere objetos Asignatura.")

    def buscar_programa(self, codigo):
        codigo = validar_texto(codigo, "El código del programa")
        for programa in self.__programas:
            if programa.get_codigo() == codigo:
                return programa
        raise ProgramaNoEncontradoError(f"No existe el programa {codigo}.")

    def buscar_asignatura(self, codigo):
        codigo = validar_texto(codigo, "El código de la asignatura")
        for asignatura in self.__asignaturas:
            if asignatura.get_codigo() == codigo:
                return asignatura
        raise AsignaturaNoEncontradaError(f"No existe la asignatura {codigo}.")
