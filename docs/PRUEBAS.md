# Verificación del sistema y del aporte

La versión con el aporte se verificó el 18 de octubre de 2026 con Python 3.12.14.
La ejecución de `main.py` terminó sin errores no controlados y las 16 pruebas
automatizadas finalizaron con resultado **OK**.

## Pruebas mínimas solicitadas

| Requisito | Evidencia observada |
| --- | --- |
| Crear programas y asignaturas | Dos programas y tres asignaturas asociados por referencias a objetos |
| Crear al menos seis personas | Dos estudiantes, dos docentes y dos administrativos |
| Consultar la información | Catálogo y reporte con los datos de los objetos |
| Modificar datos encapsulados | Correo actualizado, semestres de 8 a 9 y créditos de 3 a 4 |
| Intentar tres valores inválidos | Correo vacío, cero semestres y créditos negativos |
| Conservar datos válidos | Se mantienen el correo actualizado, los 9 semestres y los 4 créditos |
| Presentar cada tipo de persona | Cada rol muestra datos generales y sus cuatro campos particulares |
| Recorrer polimórficamente | Un ciclo llama los dos métodos para las seis personas |
| Actualizar el avance académico | Semestre y promedio cambian juntos a 3 y 4.6 |
| Rechazar una actualización conjunta inválida | El intento de semestre 4 y promedio 5.5 conserva ambos valores anteriores |

En `salida_demostracion.txt` se conserva la salida real del programa. En
`resultado_pruebas.txt` se conserva el resultado real de la suite. Son evidencias
de esta versión con el aporte; deben regenerarse si cambia el comportamiento del programa.

## Alcance de las pruebas automatizadas

1. Asociación de asignaturas y estudiantes con programas y propagación de un
   cambio de nombre a través de la referencia compartida.
2. Composición de la lista con dos personas de cada rol y herencia de Persona.
3. Inicialización y consulta de los campos de los constructores.
4. Modificación válida de correo, semestres y créditos.
5. Rechazo de correos inválidos sin perder el valor anterior.
6. Rechazo de semestres inválidos sin perder el valor anterior.
7. Rechazo de créditos inválidos sin perder el valor anterior.
8. Rechazo de datos inválidos durante la construcción.
9. Rechazo de un nombre de programa cuando se requiere el objeto asociado.
10. Reglas adicionales de promedio, semestre, horas y textos.
11. Datos particulares y actividades diferentes de los tres roles.
12. Admisión de una subclase nueva por el reporte sin modificarlo.
13. Ejecución integrada: cuatro rechazos controlados, avance académico conservado
    y seis actividades finales.
14. Actualización conjunta válida, incluidos los límites 0 y 5 del promedio.
15. Rechazo de un semestre inválido sin modificar ninguno de los dos datos.
16. Rechazo de un promedio inválido sin modificar ninguno de los dos datos,
    incluidos valores fuera de rango, tipos incorrectos y números no finitos.

Además se inspeccionó la estructura del código: los datos de instancia están
encapsulados, las tres subclases redefinen ambos métodos y el reporte contiene
un único ciclo sin condiciones que seleccionen por tipo.

## Comandos para repetir la verificación

Desde la carpeta que contiene `main.py`:

```powershell
py main.py
py -m unittest discover -s pruebas -v
```

En macOS o Linux, utilizar `python3` en lugar de `py` cuando corresponda.
El proyecto solo requiere Python y su biblioteca estándar.

## Condiciones que no acredita esta verificación

Estas pruebas comprueban el funcionamiento del código y de la mejora asistida.
No acreditan la comprensión o sustentación personal del estudiante, el acceso
del docente ni la creación de una etiqueta. El commit del aporte está enlazado
en el README. Las condiciones de cierre se revisan en `ENTREGA_GITHUB.md`.
