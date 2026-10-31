"""Horario de un grupo: día, intervalo de horas y salón."""

from datetime import time
import re

from modelos.validaciones import validar_texto


class Horario:
    """Valida todos sus datos al crearse y permite consultarlos."""

    def __init__(self, dia, hora_inicio, hora_fin, salon):
        dia = validar_texto(dia, "El día").capitalize()
        if dia not in ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes",
                       "Sábado", "Domingo"):
            raise ValueError("El día debe ser un día de la semana en español.")
        inicio = self.__convertir_hora(hora_inicio)
        fin = self.__convertir_hora(hora_fin)
        if fin <= inicio:
            raise ValueError("La hora de finalización debe ser posterior al inicio.")
        self.__dia = dia
        self.__hora_inicio = inicio
        self.__hora_fin = fin
        self.__salon = validar_texto(salon, "El salón")

    @staticmethod
    def __convertir_hora(valor):
        texto = validar_texto(valor, "La hora")
        if re.fullmatch(r"[0-9]{2}:[0-9]{2}", texto) is None:
            raise ValueError("La hora debe usar el formato HH:MM de 24 horas.")
        try:
            return time.fromisoformat(texto)
        except ValueError as error:
            raise ValueError("La hora debe estar entre 00:00 y 23:59.") from error

    def get_dia(self):
        return self.__dia

    def get_hora_inicio(self):
        return self.__hora_inicio.isoformat(timespec="minutes")

    def get_hora_fin(self):
        return self.__hora_fin.isoformat(timespec="minutes")

    def get_salon(self):
        return self.__salon

    def mostrar_informacion(self):
        return (f"{self.__dia}, {self.get_hora_inicio()} a {self.get_hora_fin()}, "
                f"salón {self.__salon}")
