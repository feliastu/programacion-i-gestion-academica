"""Especialización de Persona para docentes."""

from modelos.persona import Persona
from modelos.validaciones import validar_entero_positivo, validar_texto


class Docente(Persona):
    """Añade la vinculación laboral y académica del docente."""

    def __init__(self, identificacion, nombre, correo, numero_empleado,
                 facultad, tipo_contratacion, horas_semanales):
        super().__init__(identificacion, nombre, correo)
        self.set_numero_empleado(numero_empleado)
        self.set_facultad(facultad)
        self.set_tipo_contratacion(tipo_contratacion)
        self.set_horas_semanales(horas_semanales)

    def get_numero_empleado(self):
        return self.__numero_empleado

    def set_numero_empleado(self, numero):
        self.__numero_empleado = validar_texto(numero, "El número de empleado")

    def get_facultad(self):
        return self.__facultad

    def set_facultad(self, facultad):
        self.__facultad = validar_texto(facultad, "La facultad")

    def get_tipo_contratacion(self):
        return self.__tipo_contratacion

    def set_tipo_contratacion(self, tipo):
        self.__tipo_contratacion = validar_texto(tipo, "El tipo de contratación")

    def get_horas_semanales(self):
        return self.__horas_semanales

    def set_horas_semanales(self, horas):
        self.__horas_semanales = validar_entero_positivo(horas, "Las horas semanales")

    def mostrar_informacion(self):
        return (f"DOCENTE\n{super().mostrar_informacion()}\n"
                f"Número de empleado: {self.__numero_empleado}\n"
                f"Facultad: {self.__facultad}\n"
                f"Tipo de contratación: {self.__tipo_contratacion}\n"
                f"Horas semanales: {self.__horas_semanales}")

    def realizar_actividad_principal(self):
        return f"{self.get_nombre()} orienta clases en {self.__facultad}."
