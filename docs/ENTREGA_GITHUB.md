# Trabajo individual y entrega en GitHub

El entregable solicitado por el curso es el enlace al repositorio:
[feliastu/programacion-i-gestion-academica](https://github.com/feliastu/programacion-i-gestion-academica).
Esta entrega se realizará de manera individual por **Hernan Felipe Astudillo Peña**
(`feliastu`). Se conserva el nombre oficial del curso: *Actividad colaborativa 1*.

El sistema incluye el aporte de actualización conjunta de semestre y promedio,
su demostración y 16 pruebas correctas. La implementación con asistencia de IA
está registrada en el commit enlazado en el README y explicada en
[APORTE_INDIVIDUAL.md](APORTE_INDIVIDUAL.md). Antes de entregar quedan la revisión
y sustentación personal, el acceso del docente y la etiqueta final.

## Organizar el trabajo individual

El estudiante responsable revisará y comprenderá la totalidad del sistema:

1. Estudiar Persona, ProgramaAcademico, Asignatura y las validaciones comunes.
2. Seguir la herencia y la sobreescritura en Estudiante, Docente y Administrativo.
3. Ejecutar `main.py`, revisar las pruebas y explicar el ciclo polimórfico.
4. Seguir el método `actualizar_avance_academico()` y explicar cómo conserva los
   dos datos cuando una validación falla.
5. Repetir la demostración y las pruebas en su computador. Si realiza nuevos
   cambios, registrarlos con su explicación y actualizar la documentación.

La implementación y sus pruebas están registradas. Esta lista orienta la revisión
personal pendiente y no certifica que ya se haya realizado.

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

La declaración de IA describe la asistencia utilizada tanto en la versión inicial
como en la mejora. Actualizarla si cambia el alcance de la ayuda recibida.

## Registrar cambios posteriores

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

Comprobar que la descripción del aporte y su commit en el README correspondan a
la versión entregada, que el docente pueda acceder y que las pruebas pasen.
Revisar el historial:

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

- [x] El repositorio contiene un solo sistema y un único `main.py` de ejecución.
- [ ] Se ejecuta desde una copia recién descargada sin instalar paquetes externos.
- [x] Demuestra seis personas, cuatro rechazos y el ciclo polimórfico.
- [x] El README identifica a Hernan Felipe Astudillo Peña como único estudiante responsable.
- [x] El enlace del repositorio y el aporte técnico verificable están completos en el README.
- [x] La mejora está registrada en un commit con la asistencia de IA declarada.
- [x] El README declara el alcance de la asistencia de inteligencia artificial.
- [ ] El estudiante puede explicar todo el código y sus decisiones.
- [x] Las 16 pruebas pasan después de integrar los cambios.
- [ ] La etiqueta identifica el commit final y el docente tiene acceso.

Consultar las instrucciones oficiales de
[creación de repositorios](https://docs.github.com/es/repositories/creating-and-managing-repositories/creating-a-new-repository)
y de [versiones y etiquetas](https://docs.github.com/es/repositories/releasing-projects-on-github/managing-releases-in-a-repository).
