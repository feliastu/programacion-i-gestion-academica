"""Errores propios de los procesos del Sistema de Gestión Académica."""


class ErrorAcademico(Exception):
    """Base común de las excepciones del dominio académico."""


class EstudianteYaMatriculadoError(ErrorAcademico):
    """El código estudiantil ya aparece en el grupo."""


class CapacidadMaximaError(ErrorAcademico):
    """No hay cupos disponibles para otra matrícula."""


class EstudianteNoMatriculadoError(ErrorAcademico):
    """No se encuentra al estudiante que se quiere retirar."""


class AsignaturaNoEncontradaError(ErrorAcademico):
    """El código de la asignatura no existe en el catálogo."""


class ProgramaNoEncontradoError(ErrorAcademico):
    """El código del programa no existe en el catálogo."""
