# Sistema de Gestión Académica

Actividad colaborativa 1 de Programación I, Universidad de Manizales.

Primera versión funcional de un único sistema en Python que representa personas,
programas académicos y asignaturas. Las cinco fases se integran en las mismas
clases y en un solo punto de entrada, `main.py`.

**Estado:** primera versión funcional publicada para revisión y desarrollo del
equipo. Antes de entregar deben completarse el usuario de GitHub de Camilo, las
contribuciones individuales verificables y la etiqueta definitiva. La carga
inicial con asistencia de IA no acredita por sí sola la participación de ambos.

## Integrantes

| Nombre | Usuario de GitHub | Contribución y commit verificable |
| --- | --- | --- |
| Camilo Arias Arias | Por confirmar | Por registrar después de su aporte real |
| Hernan Felipe Astudillo Peña | feliastu | Por registrar después de su aporte real |

El equipo está conformado por estos dos estudiantes. Cada integrante debe
realizar al menos un commit con una contribución sustantiva al desarrollo;
añadir únicamente su nombre no cumple esa condición. La propuesta de distribución
de tareas para ambos se encuentra en `docs/ENTREGA_GITHUB.md`.

Repositorio: [feliastu/programacion-i-gestion-academica](https://github.com/feliastu/programacion-i-gestion-academica).

El repositorio es privado durante la revisión. Camilo y el docente necesitarán
acceso antes de colaborar y evaluar, respectivamente.

Etiqueta de entrega propuesta: `actividad-1-v1.0`. Se creará cuando el equipo
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
modificaciones inválidas; y termina con el reporte polimórfico. No solicita datos
por teclado y no requiere conexión a internet.

Para ejecutar las pruebas en Windows:

```powershell
py -m unittest discover -s pruebas -v
```

Resultado de referencia: **13 pruebas, OK**. En otros sistemas, reemplazar `py`
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
  no fija una escala; el equipo debe ajustar esta regla si el docente indica otra.
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

Esta versión inicial se elaboró con apoyo de **ChatGPT de OpenAI** para analizar
los requisitos, proponer el diseño, generar el código Python y las pruebas,
redactar la documentación y revisar la ejecución. La asistencia incluyó la
generación de la estructura y de la implementación inicial completa; no se limitó
a correcciones de redacción.

El equipo debe revisar, comprender, explicar y justificar la totalidad del código
antes de entregarlo. La participación individual debe quedar respaldada por
contribuciones reales y commits de cada estudiante. Esta declaración no acredita
que esa revisión o participación ya se haya realizado. Actualizarla con el uso
efectivo de otras herramientas y con las modificaciones hechas por el equipo.

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
