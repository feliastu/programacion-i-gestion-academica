# Sistema de Gestión Académica

**Programación I · Universidad de Manizales · Actividad colaborativa 2**

Evolución del proyecto de la primera actividad: el mismo sistema incorpora una
clase abstracta, grupos académicos con horario propio y manejo de excepciones
personalizadas. Conserva los modelos, las validaciones, el avance académico y
el reporte polimórfico desarrollados en AC1.

**Estudiante responsable:** Hernan Felipe Astudillo Peña (`feliastu`).  
**Modalidad:** individual.  
**Verificación:** 42 pruebas correctas y demostración completa con Python 3.12.14.

## Entrega y versiones

El repositorio es público y es el mismo de la primera actividad:
[feliastu/programacion-i-gestion-academica](https://github.com/feliastu/programacion-i-gestion-academica).

- [Entrega_AC1](https://github.com/feliastu/programacion-i-gestion-academica/tree/Entrega_AC1)
  identifica el commit `aa1f190`, anterior a esta ampliación. Su contenido se conserva.
- [Entrega_AC2](https://github.com/feliastu/programacion-i-gestion-academica/tree/Entrega_AC2)
  identifica la segunda entrega. Los cambios posteriores deben usar nuevos commits
  sin mover las etiquetas.
- Documento de Decisiones de Diseño: [PDF](docs/Decisiones_Diseno_AC2.pdf),
  [Word](docs/Decisiones_Diseno_AC2.docx) y [lectura en GitHub](docs/DECISIONES_DISENO_AC2.md).
- [Aporte individual](docs/APORTE_INDIVIDUAL.md), [pruebas](docs/PRUEBAS.md)
  y [orientaciones de entrega](docs/ENTREGA_GITHUB.md).

## Ejecutar y comprobar

Requiere Python 3.10 o superior y solo usa su biblioteca estándar. Descargar el
repositorio con **Code > Download ZIP**, descomprimirlo y abrir una terminal en
la carpeta que contiene `main.py`. En Windows:

```powershell
py main.py
py -m unittest discover -s pruebas -v
```

En Linux o macOS se puede usar `python3` en lugar de `py`. La demostración es
automática, no pide datos por teclado ni requiere internet. El resultado esperado
de la suite es **Ran 42 tests / OK**.

`main.py` crea dos programas, tres asignaturas y seis personas. Primero muestra
los cambios válidos e inválidos de AC1 y el reporte de los tres roles. Después
comprueba que no se pueda instanciar Persona, crea dos grupos y demuestra
matrícula, duplicado, falta de cupo, retiro válido, retiro inexistente y búsqueda
de asignatura y programa inexistentes. Tras cada error previsto continúa y muestra
el estado final de los grupos.

## Organización

| Archivo o carpeta | Responsabilidad |
| --- | --- |
| `main.py` | Único punto de entrada y demostración integrada de AC1 y AC2 |
| `modelos/persona.py` | Base abstracta con identificación, nombre y correo |
| `modelos/estudiante.py` | Rol de estudiante y actualización del avance académico |
| `modelos/docente.py` y `administrativo.py` | Roles y comportamientos específicos |
| `modelos/programa_academico.py` y `asignatura.py` | Programas y asignaturas relacionados mediante objetos |
| `modelos/grupo_academico.py` | Oferta de asignatura, docente, cupos, matrícula y retiro |
| `modelos/horario.py` | Día, hora inicial, hora final y salón del grupo |
| `modelos/catalogo_academico.py` | Búsqueda de programas y asignaturas existentes |
| `modelos/validaciones.py` | Reglas comunes para los atributos encapsulados |
| `excepciones.py` | Base ErrorAcademico y cinco excepciones específicas |
| `pruebas/test_sistema.py` | 16 pruebas del comportamiento heredado y su integración |
| `pruebas/test_ac2.py` | 26 pruebas de abstracción, grupos, composición y errores |
| `docs/` | Decisiones de diseño, guía de estudio y evidencias reales de ejecución |

## Abstracción y polimorfismo

`Persona` hereda de `ABC` y declara `realizar_actividad_principal()` con
`@abstractmethod`. Estudiante, Docente y Administrativo implementan el método y
mantienen sus versiones de `mostrar_informacion()`. Persona conserva el constructor,
los getters y los setters compartidos; intentar crear una Persona directamente
produce `TypeError`.

El reporte mantiene una lista heterogénea y un solo ciclo, sin condiciones por rol:

```python
for persona in personas:
    print(persona.mostrar_informacion())
    print("Actividad principal:", persona.realizar_actividad_principal())
    print()
```

Los controles `isinstance()` en constructores y matrículas validan los objetos
recibidos; no deciden el comportamiento de este reporte.

## Relaciones y composición

Cada GrupoAcademico recibe un objeto Asignatura y un objeto Docente, y guarda
referencias a los objetos Estudiante matriculados. No sustituye esos objetos por
sus nombres. Asignatura y Estudiante mantienen la relación con ProgramaAcademico.

El grupo construye internamente `Horario(dia, hora_inicio, hora_fin, salon)`. Este
horario es una parte del grupo: **un grupo tiene un horario**, por lo que se utiliza
composición. Heredar de Horario implicaría que el grupo es un horario y mezclaría
responsabilidades. Cada grupo crea su propia instancia; `cambiar_horario()` crea
un reemplazo válido antes de asignarlo. La interfaz de Horario solo ofrece consultas.

`get_estudiantes()` devuelve una copia de la lista para impedir que una modificación
de esa lista externa evite los controles de matrícula. Sus elementos siguen siendo
los mismos objetos. Los cupos se calculan a partir de la capacidad y de la lista,
sin mantener un contador separado que pueda quedar desactualizado.

## Matrícula, retiro y excepciones

La matrícula comprueba primero el código estudiantil duplicado y luego el cupo.
Solo añade el estudiante si ambas validaciones terminan correctamente. El retiro
busca el código, elimina su referencia y devuelve el estudiante retirado.

| Excepción personalizada | Método que la lanza | Causa |
| --- | --- | --- |
| `EstudianteYaMatriculadoError` | `matricular_estudiante()` | Código ya presente en el grupo |
| `CapacidadMaximaError` | `matricular_estudiante()` | Grupo sin cupos disponibles |
| `EstudianteNoMatriculadoError` | `retirar_estudiante()` | Código no matriculado en ese grupo |
| `AsignaturaNoEncontradaError` | `buscar_asignatura()` | Código ausente del catálogo |
| `ProgramaNoEncontradoError` | `buscar_programa()` | Código ausente del catálogo |

Las cinco clases heredan de `ErrorAcademico`, que hereda de `Exception`.
`main.py` captura cada error de forma específica, presenta un mensaje comprensible
y ejecuta operaciones posteriores. Los formatos y valores inválidos siguen usando
`ValueError`; la prohibición de crear Persona utiliza el `TypeError` de Python.

## Reglas y alcance

Los atributos usan dos guiones bajos y se consultan o modifican mediante métodos.
Esta convención evita accesos accidentales, aunque no es una barrera de seguridad.
Se mantienen las reglas de AC1: textos no vacíos, enteros positivos, correo no
vacío, programa como objeto y promedio entre 0 y 5 para los ejemplos.

La capacidad es un entero positivo. Los horarios usan días en español, incluidos
`Miércoles` y `Sábado` con tilde, y horas `HH:MM` entre 00:00 y 23:59; el final debe
ser posterior al inicio dentro del mismo día. El salón no puede quedar vacío.
Un cambio de horario inválido conserva el horario anterior.

Los códigos se comparan exactamente, tras retirar espacios externos. El duplicado
se controla dentro de cada grupo. No se imponen restricciones entre grupos,
programas o facultades que el documento no solicita. Los códigos de los objetos
se mantienen estables durante la demostración; esta versión no implementa un
registro global de identificadores ni detecta cruces de horarios.

Todos los registros son ficticios. El sistema trabaja en memoria y recrea los
datos al ejecutarse. No incluye persistencia, autenticación ni interfaz gráfica.

## Asistencia y fuentes

Se utilizó ChatGPT de OpenAI para analizar los requisitos, implementar y probar
la evolución, y elaborar la documentación, además de la asistencia declarada en
AC1. El alcance está registrado en el Documento de Decisiones de Diseño. La
revisión y sustentación personal corresponden al estudiante.

- Documento del curso: *Actividad colaborativa N°2. Evolución del Sistema de Gestión Académica*.
- [Python: clases base abstractas](https://docs.python.org/es/3.12/library/abc.html).
- [Python: errores y excepciones](https://docs.python.org/es/3.12/tutorial/errors.html).
- [Python: clases y referencias a objetos](https://docs.python.org/es/3.12/tutorial/classes.html).
