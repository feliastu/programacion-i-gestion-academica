"""Representación de un programa académico."""

from modelos.validaciones import validar_entero_positivo, validar_texto


class ProgramaAcademico:
    """Programa al que pueden asociarse estudiantes y asignaturas."""

    def __init__(self, codigo, nombre, facultad, semestres):
        self.set_codigo(codigo)
        self.set_nombre(nombre)
        self.set_facultad(facultad)
        self.set_semestres(semestres)

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = validar_texto(codigo, "El código del programa")

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = validar_texto(nombre, "El nombre del programa")

    def get_facultad(self):
        return self.__facultad

    def set_facultad(self, facultad):
        self.__facultad = validar_texto(facultad, "La facultad")

    def get_semestres(self):
        return self.__semestres

    def set_semestres(self, semestres):
        """Solo reemplaza el número de semestres si el valor es válido."""
        self.__semestres = validar_entero_positivo(semestres, "Los semestres")

    def mostrar_informacion(self):
        return (f"Programa: {self.__codigo} - {self.__nombre}\n"
                f"Facultad: {self.__facultad}\n"
                f"Número de semestres: {self.__semestres}")
