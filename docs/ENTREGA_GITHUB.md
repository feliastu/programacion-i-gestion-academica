# Trabajo individual y entrega en GitHub

El entregable solicitado por el curso es el enlace al repositorio:
[feliastu/programacion-i-gestion-academica](https://github.com/feliastu/programacion-i-gestion-academica).
Esta entrega se realizará de manera individual por **Hernan Felipe Astudillo Peña**
(`feliastu`). Se conserva el nombre oficial del curso: *Actividad colaborativa 1*.

La base funcional y su documentación ya están publicadas para revisión. Antes de
entregar faltan la revisión personal, el registro de aportes verificables, el
acceso del docente y la etiqueta final.

## Organizar el trabajo individual

El estudiante responsable revisará y comprenderá la totalidad del sistema:

1. Estudiar Persona, ProgramaAcademico, Asignatura y las validaciones comunes.
2. Seguir la herencia y la sobreescritura en Estudiante, Docente y Administrativo.
3. Ejecutar `main.py`, revisar las pruebas y explicar el ciclo polimórfico.
4. Identificar una mejora o corrección justificada, implementarla y documentar
   su resultado. Agregar o ajustar pruebas cuando el cambio de comportamiento
   lo requiera.
5. Registrar su aporte real con un commit y actualizar su referencia en el README.

Esta lista organiza el trabajo pendiente; no representa aportes ya realizados.
El historial debe reflejar el trabajo efectivo con la identidad del estudiante.
Un cambio cosmético o añadir un nombre no equivale a un aporte de desarrollo.

## Acceder al repositorio

El repositorio pertenece a `feliastu` y es privado. Antes de la entrega, comprobar
que el docente tenga acceso para evaluarlo. El documento de la actividad no exige
que el repositorio sea público.

`main.py`, `README.md`, `modelos`, `pruebas` y `docs` se encuentran en la raíz.
Las grabaciones de clase y el documento original no están incluidos.

## Obtener una copia para trabajar

Se necesita Git instalado y autenticación con la cuenta `feliastu`.
Desde una terminal en la carpeta donde se quiera guardar el proyecto:

```bash
git clone https://github.com/feliastu/programacion-i-gestion-academica.git
cd programacion-i-gestion-academica
```

Si GitHub solicita autenticación, utilizar el flujo de inicio de sesión de Git
o del administrador de credenciales instalado. No guardar contraseñas ni tokens
en el repositorio.

Configurar la identidad local. Reemplazar el correo de ejemplo por uno asociado
a la cuenta de GitHub, incluido el correo privado de GitHub si se prefiere:

```bash
git config user.name "Hernan Felipe Astudillo Peña"
git config user.email "CORREO ASOCIADO A SU CUENTA DE GITHUB"
```

En Windows, comprobar la ejecución:

```powershell
py main.py
py -m unittest discover -s pruebas -v
```

La carga inicial con asistencia de IA no acredita por sí sola el desarrollo
personal. La declaración de IA debe permanecer y los aportes posteriores deben
ser reales.

## Registrar una mejora propia

Crear una rama para el cambio, editar los archivos, ejecutar el programa y las
pruebas, y registrar un commit con un mensaje que describa el aporte.

Ejemplo para un cambio real de validación, después de clonar el repositorio:

```bash
git switch -c mejora-validacion
```

Luego de editar y verificar:

```bash
git add modelos/validaciones.py pruebas/test_sistema.py
git commit -m "Corrige validación del caso identificado y agrega su prueba"
git push -u origin mejora-validacion
```

Los archivos y el mensaje deben coincidir con lo que efectivamente se cambió.
Revisar e integrar la rama mediante una solicitud de cambios en GitHub, o mediante
el flujo de Git elegido, conservando la autoría real.

## Cerrar la versión de la actividad

Completar la contribución y el commit verificable del estudiante en el README,
comprobar que el docente puede acceder, ejecutar las pruebas y revisar el historial:

```bash
git log --format="%h | %an | %s"
```

Cuando los cambios estén integrados y antes de la fecha límite, crear una etiqueta
que identifique exactamente la versión entregada:

```bash
git switch main
git pull --ff-only
git tag -a actividad-1-v1.0 -m "Entrega individual de la actividad colaborativa 1"
git push origin actividad-1-v1.0
```

El nombre es una propuesta. Una etiqueta marca un commit, pero no impide por sí
misma que alguien la mueva o elimine. Conservarla sin cambios: no reemplazarla,
borrarla ni reescribir el historial de la versión entregada.

También puede crearse una versión desde la sección **Releases** de GitHub y
seleccionar la etiqueta del commit final. Para la siguiente actividad, continuar
con nuevos commits posteriores, manteniendo intacta la etiqueta de esta entrega.

## Verificación final individual

- [ ] El repositorio contiene un solo sistema y un único `main.py` de ejecución.
- [ ] Se ejecuta desde una copia recién descargada sin instalar paquetes externos.
- [ ] Demuestra seis personas, tres rechazos y el ciclo polimórfico.
- [ ] El README identifica a Hernan Felipe Astudillo Peña como único estudiante responsable.
- [ ] El enlace del repositorio y el aporte verificable están completos en el README.
- [ ] El estudiante tiene al menos un commit de desarrollo verificable.
- [ ] El README declara de manera fiel el uso de inteligencia artificial.
- [ ] El estudiante puede explicar todo el código y sus decisiones.
- [ ] Las pruebas pasan después de integrar los cambios.
- [ ] La etiqueta identifica el commit final y el docente tiene acceso.

Consultar las instrucciones oficiales de
[creación de repositorios](https://docs.github.com/es/repositories/creating-and-managing-repositories/creating-a-new-repository)
y de [versiones y etiquetas](https://docs.github.com/es/repositories/releasing-projects-on-github/managing-releases-in-a-repository).
