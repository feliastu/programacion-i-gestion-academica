# Aporte: actualización del avance académico

**Estudiante responsable:** Hernan Felipe Astudillo Peña  
**Modalidad:** individual  
**Commit de implementación:** [0f2c576](https://github.com/feliastu/programacion-i-gestion-academica/commit/0f2c5765fe07b454053a7a858b5e7a558adfe195)

## Qué se agregó y para qué sirve

Se agregó el método `actualizar_avance_academico(semestre, promedio)` a la clase
`Estudiante`. Permite actualizar los dos datos juntos y evita dejar una
actualización incompleta cuando uno de ellos es inválido.

Los setters individuales siguen disponibles. Si se llaman por separado, cada
uno valida su propio dato: un cambio de semestre puede completarse aunque una
llamada posterior para cambiar el promedio falle. El nuevo método cubre el caso
en que los dos datos deben aceptarse o rechazarse como una sola operación.

## Cómo funciona

1. Valida el semestre con `validar_entero_positivo()`.
2. Valida el promedio con `validar_promedio()`.
3. Guarda los resultados en los atributos privados solo cuando las dos
   validaciones han terminado correctamente.
4. Si alguna validación lanza `ValueError`, el método termina antes de modificar
   los atributos y el programa principal muestra el error.

Se reutilizan las reglas existentes: semestre entero mayor que cero y promedio
entre 0 y 5. La escala del promedio es una decisión del ejemplo. La mejora no
establece una política institucional sobre promoción de semestre.

## Ejemplo de la demostración

| Operación | Semestre resultante | Promedio resultante |
| --- | --- | --- |
| Estado inicial del primer estudiante | 2 | 4.2 |
| Actualizar con semestre 3 y promedio 4.6 | 3 | 4.6 |
| Intentar semestre 4 y promedio 5.5 | 3 | 4.6 |

El último intento se rechaza porque 5.5 está fuera del rango permitido. El
semestre 4 es válido por separado, pero tampoco se guarda: falló la operación
conjunta.

## Archivos modificados

- `modelos/estudiante.py`: método de actualización conjunta.
- `main.py`: ejemplo válido, intento inválido y consulta de los datos conservados.
- `pruebas/test_sistema.py`: tres pruebas nuevas y ampliación de la prueba de
  ejecución completa.
- `docs/salida_demostracion.txt` y `docs/resultado_pruebas.txt`: evidencia de la
  ejecución de esta versión.

La mejora pertenece al mismo sistema. El reporte conserva su lista heterogénea
y su único ciclo, que llama a los dos métodos sobrescritos sin separar por tipo.

## Resultado de la verificación

El 18 de octubre de 2026 se ejecutaron el programa y las pruebas con Python
3.12.14. La ejecución terminó correctamente y las **16 pruebas pasaron**.

Las tres pruebas nuevas comprueban la actualización válida, el rechazo de un
semestre inválido y el rechazo de un promedio inválido. Las pruebas de rechazo
verifican que se conserven **los dos datos**, no solo que se produzca un error.

Para repetir la verificación en Windows:

```powershell
py main.py
py -m unittest discover -s pruebas -v
```

## Preparación para la sustentación

Revisar el método y explicar con palabras propias:

- Por qué las validaciones aparecen antes de las asignaciones.
- Qué diferencia hay entre dos llamadas independientes a setters y este método.
- Por qué un promedio inválido impide también cambiar el semestre.
- Cómo el reporte final muestra el estado actualizado del mismo objeto.

## Asistencia utilizada

La mejora fue propuesta, implementada, probada y documentada con ChatGPT a
solicitud del estudiante. Su revisión y sustentación personal quedan pendientes;
este registro no las presenta como realizadas.
