# Verificación de la segunda entrega

El 31 de octubre de 2026 se ejecutaron `main.py` y la suite completa con Python
3.12.14. La demostración terminó correctamente y **las 42 pruebas pasaron**:
16 pruebas del sistema anterior, adaptadas a Persona abstracta, y 26 de AC2.

## Correspondencia con las pruebas mínimas

| Caso solicitado | Evidencia en la demostración |
| --- | --- |
| Prohibir la creación directa de Persona | Se captura TypeError en la sección 6 |
| Crear objetos relacionados | Se reutilizan las asignaturas, docentes y estudiantes de AC1 |
| Crear al menos dos grupos | PROG1-A y PROG1-B, con docentes y horarios propios |
| Matricular correctamente | EST001 en PROG1-A y EST002 en PROG1-B |
| Rechazar duplicados | EST001 intenta matricularse nuevamente en PROG1-A |
| Rechazar capacidad excedida | EST002 intenta ingresar a PROG1-A, cuya capacidad es 1 |
| Retirar correctamente | Se retira EST001 de PROG1-A y se libera un cupo |
| Rechazar retiro inexistente | EST999 no pertenece a PROG1-A |
| Buscar asignatura inexistente | ASIG999 produce AsignaturaNoEncontradaError |
| Buscar programa inexistente | PROG999 produce ProgramaNoEncontradoError |
| Continuar después de las excepciones | Mensajes CONTINÚA, búsquedas válidas y estado final de ambos grupos |

Al terminar, PROG1-A tiene a EST002 y cero cupos libres; PROG1-B tiene al mismo
objeto EST002 y un cupo libre. La regla de duplicados se aplica por grupo; no se
ha establecido una restricción de matrícula entre grupos.

## Qué comprueban las pruebas

La suite conserva la validación de datos, herencia, sobreescritura, referencias
compartidas, avance académico y el reporte polimórfico de AC1. Las nuevas pruebas
comprueban el contrato abstracto, los tres roles concretos, asociaciones reales,
horarios independientes y válidos, reemplazo seguro del horario, matrículas por
código, capacidad, retiro, consulta, búsquedas y continuidad de la demostración.

Los rechazos se comprueban tanto por su excepción como por el estado posterior:
una matrícula fallida no altera la lista ni los cupos y un horario inválido no
reemplaza el anterior. La copia de la lista de estudiantes protege la colección
interna. Un cambio en la asignatura compartida se observa desde ambos grupos.

`test_sistema.py` contiene 16 métodos de prueba y `test_ac2.py` contiene 26.
Varios métodos incluyen subcasos para límites, tipos incorrectos y datos vacíos.

## Reproducir el resultado

Desde la carpeta de `main.py`, en Windows:

```powershell
py main.py
py -m unittest discover -s pruebas -v
```

En Linux o macOS usar `python3` cuando corresponda. No hay paquetes externos.

- [Salida real de la demostración](salida_demostracion.txt).
- [Salida real de las 42 pruebas](resultado_pruebas.txt).

Las pruebas verifican el comportamiento del sistema; la revisión y explicación
personal del estudiante se preparan con [la guía](GUIA_PASO_A_PASO.md).
