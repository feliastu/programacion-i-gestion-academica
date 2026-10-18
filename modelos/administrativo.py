"""Especialización de Persona para personal administrativo."""

from modelos.persona import Persona
from modelos.validaciones import validar_texto


class Administrativo(Persona):
    """Añade dependencia, cargo y jornada a la información común."""

    def __init__(self, identificacion, nombre, correo, numero_empleado,
                 dependencia, cargo, jornada):
        super().__init__(identificacion, nombre, correo)
        self.set_numero_empleado(numero_empleado)
        self.set_dependencia(dependencia)
        self.set_cargo(cargo)
        self.set_jornada(jornada)

    def get_numero_empleado(self):
        return self.__numero_empleado

    def set_numero_empleado(self, numero):
        self.__numero_empleado = validar_texto(numero, "El número de empleado")

    def get_dependencia(self):
        return self.__dependencia

    def set_dependencia(self, dependencia):
        self.__dependencia = validar_texto(dependencia, "La dependencia")

    def get_cargo(self):
        return self.__cargo

    def set_cargo(self, cargo):
        self.__cargo = validar_texto(cargo, "El cargo")

    def get_jornada(self):
        return self.__jornada

    def set_jornada(self, jornada):
        self.__jornada = validar_texto(jornada, "La jornada")

    def mostrar_informacion(self):
        return (f"ADMINISTRATIVO\n{super().mostrar_informacion()}\n"
                f"Número de empleado: {self.__numero_empleado}\n"
                f"Dependencia: {self.__dependencia}\n"
                f"Cargo: {self.__cargo}\n"
                f"Jornada: {self.__jornada}")

    def realizar_actividad_principal(self):
        return (f"{self.get_nombre()} desempeña el cargo de {self.__cargo} "
                f"en {self.__dependencia}.")
