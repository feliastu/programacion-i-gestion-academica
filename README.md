# Sistema de Gestión Académica

Actividad colaborativa 1 de Programación I, Universidad de Manizales.

Primera versión funcional de un único sistema en Python que representa personas,
programas académicos y asignaturas. Las cinco fases se integran en las mismas
clases y en un solo punto de entrada, `main.py`.

**Modalidad de entrega:** individual.

**Estado:** versión funcional con una mejora para actualizar el avance académico
y 16 pruebas automatizadas correctas. Antes de entregar quedan la revisión y
sustentación personal, la comprobación del acceso del docente y la etiqueta final.

## Estudiante responsable

| Nombre | Usuario de GitHub | Contribución y commit verificable |
| --- | --- | --- |
| Hernan Felipe Astudillo Peña | feliastu | Actualización conjunta de semestre y promedio, demostración y pruebas, con asistencia de IA. [Commit 0f2c576](https://github.com/feliastu/programacion-i-gestion-academica/commit/0f2c5765fe07b454053a7a858b5e7a558adfe195) |

Hernan Felipe Astudillo Peña es el único estudiante responsable de esta entrega.
El aporte técnico está explicado en [Aporte individual](docs/APORTE_INDIVIDUAL.md).
La guía de trabajo y cierre de la entrega se encuentra en
[Entrega en GitHub](docs/ENTREGA_GITHUB.md).

Repositorio: [feliastu/programacion-i-gestion-academica](https://github.com/feliastu/programacion-i-gestion-academica).

El repositorio es privado durante la revisión. Antes de entregar, el estudiante
debe comprobar que el docente tenga acceso para evaluarlo.

Etiqueta de entrega propuesta: `actividad-1-v1.0`. Se creará cuando el estudiante
termine la revisión y sus aportes; el documento no establece un nombre obligatorio.

## Ejecución

Se requiere Python 3.10 o superior. Se utiliza únicamente la biblioteca estándar,
por lo que no es necesario instalar paquetes con `pip`.

1. Descargar y descomprimir el proyecto desde **Code > Download ZIP**, o clonarlo
   con Git siguiendo `docs/ENTREGA_GITHUB.md`.
2. Abrir en Visual Studio Code la carpeta que contiene `main.py`.
3. Abrir una terminal en esa carpeta, donde se encuentra `main.py`.
4. En Windows, ejecutar:

```powershell
py main.py
```

También puede utilizarse `python main.py` si ese es el comando configurado. En
macOS o Linux, normalmente se utiliza `python3 main.py`.

La demostración es automática: crea dos programas, tres asignaturas y seis
personas; consulta sus datos; realiza tres modificaciones válidas; rechaza tres
modificaciones inválidas; demuestra la actualización conjunta de semestre y
promedio, con un cuarto rechazo; y termina con el reporte polimórfico. No solicita
datos por teclado y no requiere conexión a internet.

Para ejecutar las pruebas en Windows:

```powershell
py -m unittest discover -s pruebas -v
```

Resultado de referencia: **16 pruebas, OK**. En otros sistemas, reemplazar `py`
por el comando de Python instalado.

## Archivos del proyecto

| Archivo o carpeta | Responsabilidad |
| --- | --- |
| `main.py` | Crea los datos, muestra cambios válidos e inválidos y genera el reporte |
| `modelos/persona.py` | Clase base con identificación, nombre y correo |
| `modelos/programa_academico.py` | Código, nombre, facultad y número de semestres |
| `modelos/asignatura.py` | Código, nombre, créditos y asociación con un programa |
| `modelos/estudiante.py` | Especialización de Persona para estudiantes |
| `modelos/docente.py` | Especialización de Persona para docentes |
| `modelos/administrativo.py` | Especialización de Persona para administrativos |
| `modelos/validaciones.py` | Reglas comunes de validación |
| `modelos/__init__.py` | Identifica el paquete de modelos |
| `pruebas/test_sistema.py` | Pruebas automatizadas que reutilizan el sistema |
| `pruebas/__init__.py` | Identifica el paquete de pruebas |
| `docs/GUIA_PASO_A_PASO.md` | Explicación del diseño y preparación para sustentarlo |
| `docs/APORTE_INDIVIDUAL.md` | Mejora del avance académico, evidencia y explicación |
| `docs/ENTREGA_GITHUB.md` | Organización del trabajo, publicación y etiqueta |
| `docs/PRUEBAS.md` | Matriz de aceptación y resultado de la verificación |
| `docs/salida_demostracion.txt` | Salida real de la ejecución de referencia |
| `docs/resultado_pruebas.txt` | Resultado real de las pruebas automatizadas |
| `.gitignore` | Excluye archivos temporales y cachés |

## Aplicación de los conceptos de POO

**Clases y objetos.** Las seis clases modelan las entidades solicitadas. Cada
instancia posee sus propios valores. Una asignatura y un estudiante conservan
una referencia a un objeto `ProgramaAcademico`.

**Constructores.** Cada clase utiliza `__init__` para inicializar todos sus
atributos. Los constructores llaman a los setters para aplicar las mismas reglas
durante la creación y las modificaciones posteriores.

**Encapsulamiento.** Los atributos utilizan dos guiones bajos, por ejemplo
`__correo`. Los métodos `get_...` consultan y los métodos `set_...` actualizan.
Python transforma internamente esos nombres; esto ayuda a evitar accesos
accidentales, pero no constituye una barrera de seguridad absoluta. El código
cliente debe respetar la interfaz pública de métodos.

**Herencia.** `Estudiante`, `Docente` y `Administrativo` heredan de `Persona`.
Usan `super().__init__(identificacion, nombre, correo)` para inicializar la
información común, sin volver a declarar esos atributos en cada subclase.

**Sobreescritura.** Las tres subclases redefinen `mostrar_informacion()` y
`realizar_actividad_principal()`. La primera amplía la información general
mediante `super().mostrar_informacion()`; la segunda expresa la actividad de cada
rol. Los métodos devuelven texto y `main.py` lo imprime.

**Polimorfismo.** `mostrar_reporte()` recibe la única lista heterogénea y ejecuta
las mismas llamadas en un solo ciclo:

```python
for persona in personas:
    print(persona.mostrar_informacion())
    print("Actividad principal:", persona.realizar_actividad_principal())
    print()
```

Python selecciona el método del objeto real. Este ciclo no utiliza `if`,
`isinstance()` ni `type()` para distinguir los roles. Los controles de tipos de
las validaciones y las comprobaciones de la suite de pruebas tienen otra función;
no seleccionan comportamientos en el reporte.

## Mejora: actualización del avance académico

`Estudiante.actualizar_avance_academico(semestre, promedio)` permite actualizar
los dos datos en una sola operación. Primero valida ambos valores y después
modifica los atributos privados. Si un valor es inválido, conserva los dos datos
anteriores. Utiliza las mismas reglas de los setters individuales.

Por ejemplo, después de guardar semestre 3 y promedio 4.6, un intento de cambiar
a semestre 4 y promedio 5.5 se rechaza por el promedio. El semestre permanece en 3.
Esta operación se demuestra en `main.py` y tiene tres pruebas específicas.

## Cumplimiento de las cinco fases

| Fase | Implementación en este mismo proyecto |
| --- | --- |
| 1 Modelado inicial | Persona, ProgramaAcademico, Asignatura y sus constructores |
| 2 Protección de información | Atributos encapsulados, getters, setters y ValueError |
| 3 Diferenciación de personas | Estudiante, Docente y Administrativo heredan de Persona |
| 4 Comportamientos particulares | Dos métodos sobrescritos en cada subclase |
| 5 Procesamiento conjunto | Lista de seis personas y un único ciclo polimórfico |

Los archivos de pruebas importan estas mismas clases. No hay una implementación
separada para cada fase.

## Validaciones y decisiones del diseño

Las reglas obligatorias impiden dejar vacío el correo y exigen que los números
de semestres y créditos sean mayores que cero. Un setter primero valida y luego
asigna; si lanza `ValueError`, el valor anterior permanece intacto. `main.py`
captura ese error y lo muestra sin interrumpir el resto de la demostración.

Como decisiones adicionales de esta propuesta:

- Los textos deben tener contenido; una cadena con espacios se considera vacía.
- Identificaciones y códigos son cadenas para conservar letras y ceros iniciales.
- Semestres, créditos, semestre del estudiante y horas semanales son enteros
  positivos. No se aceptan booleanos como números.
- El promedio utiliza la escala de 0 a 5, adoptada para los ejemplos. El documento
  no fija una escala; el estudiante debe ajustar esta regla si el docente indica otra.
- El programa de un estudiante o asignatura debe ser un objeto `ProgramaAcademico`.
- No se valida el formato completo de un correo: la regla solicitada exige que
  no sea vacío. Tampoco se implementan reglas institucionales no suministradas,
  como límites de matrícula, unicidad de códigos o validaciones entre semestres.

Todos los registros de la demostración son ficticios. Los nombres de programas
y sus duraciones son ejemplos y no certifican planes de estudio oficiales.
Los datos permanecen en memoria: cada ejecución vuelve a crearlos. No se incluyen
base de datos, archivos de persistencia, interfaz gráfica ni menú interactivo,
porque no son requisitos de esta primera actividad.

## Declaración de uso de inteligencia artificial

Se utilizó **ChatGPT de OpenAI** para analizar los requisitos, proponer el diseño
y generar la implementación inicial completa, las pruebas y la documentación.
También se utilizó para proponer e implementar la actualización conjunta de
semestre y promedio, probarla y documentarla a solicitud del estudiante.

La revisión, comprensión y sustentación del código corresponden al estudiante.
El registro del cambio acredita la implementación asistida; no certifica que la
revisión personal ya se haya realizado.

## Fuentes de referencia

- Documento de la actividad suministrado por el curso: *Construcción de un Sistema
  de Gestión Académica utilizando Programación Orientada a Objetos*.
- [Documentación oficial de Python sobre clases, herencia y nombres privados](https://docs.python.org/es/3.12/tutorial/classes.html).
- [GitHub Docs sobre creación de repositorios](https://docs.github.com/es/repositories/creating-and-managing-repositories/creating-a-new-repository).
- [GitHub Docs sobre versiones y etiquetas](https://docs.github.com/es/repositories/releasing-projects-on-github/managing-releases-in-a-repository).

Se revisó completo el documento de la actividad. De los cuatro videos se
inspeccionaron pantallas de muestra como apoyo visual; no se realizó una revisión
íntegra ni una transcripción de las grabaciones. No se atribuyen a los videos
instrucciones que no hayan sido verificadas.
