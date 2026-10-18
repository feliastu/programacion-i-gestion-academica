"""Información común a estudiantes, docentes y administrativos."""

from modelos.validaciones import validar_texto


class Persona:
    """Centraliza los datos generales y sus métodos de acceso."""

    def __init__(self, identificacion, nombre, correo):
        # El constructor reutiliza las validaciones de los setters.
        self.set_identificacion(identificacion)
        self.set_nombre(nombre)
        self.set_correo(correo)

    def get_identificacion(self):
        return self.__identificacion

    def set_identificacion(self, identificacion):
        self.__identificacion = validar_texto(identificacion, "La identificación")

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = validar_texto(nombre, "El nombre")

    def get_correo(self):
        return self.__correo

    def set_correo(self, correo):
        """Rechaza un correo vacío sin perder el correo anterior."""
        self.__correo = validar_texto(correo, "El correo")

    def mostrar_informacion(self):
        """Devuelve los datos generales para su impresión desde main.py."""
        return (f"Identificación: {self.__identificacion}\n"
                f"Nombre: {self.__nombre}\n"
                f"Correo: {self.__correo}")

    def realizar_actividad_principal(self):
        """Comportamiento general que cada subclase sobrescribe."""
        return f"{self.__nombre} participa en la comunidad académica."
