"""Punto de entrada: evolución del mismo sistema de AC1 a AC2.

Ejecutar desde esta carpeta: python main.py
Todos los registros de la demostración son ficticios.
"""

from excepciones import (
    AsignaturaNoEncontradaError, CapacidadMaximaError,
    EstudianteNoMatriculadoError, EstudianteYaMatriculadoError,
    ProgramaNoEncontradoError,
)
from modelos.administrativo import Administrativo
from modelos.asignatura import Asignatura
from modelos.catalogo_academico import CatalogoAcademico
from modelos.docente import Docente
from modelos.estudiante import Estudiante
from modelos.grupo_academico import GrupoAcademico
from modelos.persona import Persona
from modelos.programa_academico import ProgramaAcademico


def crear_datos_demo():
    """Construye objetos relacionados que también reutilizan las pruebas."""
    analitica = ProgramaAcademico(
        "PAD", "Ingeniería en Analítica de Datos", "Ciencias e Ingenierías", 8
    )
    contaduria = ProgramaAcademico(
        "CON", "Contaduría Pública", "Ciencias Contables", 9
    )
    programas = [analitica, contaduria]
    asignaturas = [
        Asignatura("PROG1", "Programación I", 3, analitica),
        Asignatura("EST1", "Estadística I", 3, analitica),
        Asignatura("CONT1", "Contabilidad I", 4, contaduria),
    ]

    # Una única lista heterogénea: dos objetos de cada subclase, intercalados.
    personas = [
        Estudiante("E001", "Ana Torres", "ana@example.com", "EST001",
                   analitica, 2, 4.2),
        Docente("D001", "Laura Méndez", "laura@example.com", "DOC001",
                "Ciencias e Ingenierías", "Tiempo completo", 40),
        Administrativo("A001", "Diana López", "diana@example.com", "ADM001",
                       "Registro Académico", "Coordinadora", "Diurna"),
        Estudiante("E002", "Carlos Ríos", "carlos@example.com", "EST002",
                   contaduria, 4, 4.5),
        Docente("D002", "Julián Vega", "julian@example.com", "DOC002",
                "Ciencias Contables", "Hora cátedra", 12),
        Administrativo("A002", "Andrés Mora", "andres@example.com", "ADM002",
                       "Biblioteca", "Auxiliar", "Mixta"),
    ]
    return programas, asignaturas, personas


def mostrar_reporte(personas):
    """Polimorfismo: un ciclo y las mismas llamadas para cualquier persona."""
    for persona in personas:
        print(persona.mostrar_informacion())
        print("Actividad principal:", persona.realizar_actividad_principal())
        print()


def demostrar_grupos(programas, asignaturas, personas):
    """Usa los objetos de AC1 para demostrar la oferta y la matrícula de AC2."""
    catalogo = CatalogoAcademico(programas, asignaturas)
    asignatura = catalogo.buscar_asignatura("PROG1")
    print("\n6. CLASE ABSTRACTA Y OFERTA DE GRUPOS\n")
    try:
        Persona("P000", "Persona sin rol", "persona@example.com")
    except TypeError:
        print("CONTROLADO - PersonaAbstracta: no se puede crear Persona; "
              "se debe elegir Estudiante, Docente o Administrativo.")
    print("CONTINÚA: se crean dos grupos con horarios propios.\n")

    grupo_a = GrupoAcademico("PROG1-A", asignatura, personas[1], 1,
                            "Lunes", "08:00", "10:00", "A101")
    grupo_b = GrupoAcademico("PROG1-B", asignatura, personas[4], 2,
                            "Miércoles", "14:00", "16:00", "B202")
    grupos = [grupo_a, grupo_b]
    for grupo in grupos:
        print(grupo.mostrar_informacion_grupo())
        print(grupo.mostrar_estudiantes(), "\n")

    print("7. MATRÍCULA Y RETIRO CON EXCEPCIONES PERSONALIZADAS\n")
    ana, carlos = personas[0], personas[3]
    grupo_a.matricular_estudiante(ana)
    grupo_b.matricular_estudiante(carlos)
    print("MATRÍCULA CORRECTA: EST001 en PROG1-A y EST002 en PROG1-B.")

    try:
        grupo_a.matricular_estudiante(ana)
    except EstudianteYaMatriculadoError as error:
        print("CONTROLADO - EstudianteYaMatriculadoError:", error)
    print("CONTINÚA: PROG1-A conserva", len(grupo_a.get_estudiantes()), "matrícula.")

    try:
        grupo_a.matricular_estudiante(carlos)
    except CapacidadMaximaError as error:
        print("CONTROLADO - CapacidadMaximaError:", error)
    print("CONTINÚA: PROG1-A conserva", grupo_a.get_cupos_disponibles(), "cupos libres.")

    retirado = grupo_a.retirar_estudiante("EST001")
    print("RETIRO CORRECTO:", retirado.get_codigo_estudiantil(), "de PROG1-A.")
    print("Cupos después del retiro:", grupo_a.get_cupos_disponibles())

    try:
        grupo_a.retirar_estudiante("EST999")
    except EstudianteNoMatriculadoError as error:
        print("CONTROLADO - EstudianteNoMatriculadoError:", error)
    print("CONTINÚA: el cupo liberado permite matricular a EST002.")
    grupo_a.matricular_estudiante(carlos)

    print("\n8. BÚSQUEDAS EN EL CATÁLOGO\n")
    try:
        catalogo.buscar_asignatura("ASIG999")
    except AsignaturaNoEncontradaError as error:
        print("CONTROLADO - AsignaturaNoEncontradaError:", error)
    print("CONTINÚA: asignatura válida:",
          catalogo.buscar_asignatura("PROG1").get_nombre())

    try:
        catalogo.buscar_programa("PROG999")
    except ProgramaNoEncontradoError as error:
        print("CONTROLADO - ProgramaNoEncontradoError:", error)
    print("CONTINÚA: programa válido:", catalogo.buscar_programa("PAD").get_nombre())

    print("\n9. ESTADO FINAL DE LOS GRUPOS\n")
    for grupo in grupos:
        print(grupo.mostrar_informacion_grupo())
        print(grupo.mostrar_estudiantes(), "\n")
    print("FIN: demostración completada después de controlar todas las excepciones.")
    return grupos


def main():
    programas, asignaturas, personas = crear_datos_demo()

    print("SISTEMA DE GESTIÓN ACADÉMICA\nDatos ficticios de demostración\n")
    print("1. PROGRAMAS ACADÉMICOS Y ASIGNATURAS\n")
    for programa in programas:
        print(programa.mostrar_informacion(), "\n")
    for asignatura in asignaturas:
        print(asignatura.mostrar_informacion(), "\n")

    print("2. MODIFICACIONES VÁLIDAS MEDIANTE MÉTODOS\n")
    print("Correo anterior:", personas[0].get_correo())
    personas[0].set_correo("ana.torres@example.com")
    print("Correo actualizado:", personas[0].get_correo())
    print("Semestres anteriores:", programas[0].get_semestres())
    programas[0].set_semestres(9)
    print("Semestres actualizados:", programas[0].get_semestres())
    print("Créditos anteriores:", asignaturas[0].get_creditos())
    asignaturas[0].set_creditos(4)
    print("Créditos actualizados:", asignaturas[0].get_creditos())

    # Los errores se capturan para informar y continuar con el mismo sistema.
    print("\n3. TRES INTENTOS DE MODIFICACIÓN INVÁLIDA\n")
    try:
        personas[0].set_correo("")
    except ValueError as error:
        print("RECHAZADO - correo vacío:", error)
    print("Correo conservado:", personas[0].get_correo())

    try:
        programas[0].set_semestres(0)
    except ValueError as error:
        print("RECHAZADO - cero semestres:", error)
    print("Semestres conservados:", programas[0].get_semestres())

    try:
        asignaturas[0].set_creditos(-2)
    except ValueError as error:
        print("RECHAZADO - créditos negativos:", error)
    print("Créditos conservados:", asignaturas[0].get_creditos())

    print("\n4. ACTUALIZACIÓN CONJUNTA DEL AVANCE ACADÉMICO\n")
    estudiante = personas[0]
    print("Avance anterior:", estudiante.get_semestre(),
          "| Promedio:", estudiante.get_promedio())
    estudiante.actualizar_avance_academico(3, 4.6)
    print("Avance actualizado:", estudiante.get_semestre(),
          "| Promedio:", estudiante.get_promedio())

    # El semestre 4 es válido, pero el promedio 5.5 invalida toda la operación.
    try:
        estudiante.actualizar_avance_academico(4, 5.5)
    except ValueError as error:
        print("RECHAZADO - actualización conjunta:", error)
    print("Avance conservado:", estudiante.get_semestre(),
          "| Promedio:", estudiante.get_promedio())

    print("\n5. REPORTE POLIMÓRFICO DE LAS SEIS PERSONAS\n")
    mostrar_reporte(personas)
    demostrar_grupos(programas, asignaturas, personas)


if __name__ == "__main__":
    main()
