# Organización del equipo y entrega en GitHub

El entregable solicitado por el curso es el enlace al repositorio:
[feliastu/programacion-i-gestion-academica](https://github.com/feliastu/programacion-i-gestion-academica).
La base funcional y su documentación ya están publicadas para revisión. Antes de
entregar faltan los aportes individuales, el acceso del docente y la etiqueta final.

## Acordar las contribuciones

El equipo está conformado por Camilo Arias Arias y Hernan Felipe Astudillo Peña.
El usuario de GitHub de Hernan es `feliastu`; el de Camilo está pendiente de
confirmación. La siguiente distribución es una propuesta para organizar el
trabajo; no representa aportes ya realizados.

| Integrante | Responsabilidad propuesta | Aporte de desarrollo verificable |
| --- | --- | --- |
| Camilo Arias Arias | Persona, ProgramaAcademico, Asignatura y validaciones comunes | Identificar e implementar una mejora justificada del modelo o de la validación, con su prueba correspondiente |
| Hernan Felipe Astudillo Peña | Estudiante, Docente, Administrativo, integración en main.py y documentación | Implementar una mejora justificada de un comportamiento o de la demostración integrada, con su prueba y explicación |

Ambos deben revisar las pruebas, comprobar el reporte polimórfico y comprender
la totalidad del proyecto. Pueden ajustar esta distribución de común acuerdo.
Cada uno debe efectuar su aporte desde su propia identidad de Git.
No registrar commits con nombres ajenos,
no crear commits vacíos y no dividir artificialmente un trabajo para simular
participación. Un cambio cosmético o añadir un nombre no equivale a desarrollar.

## Acceder al repositorio

El repositorio pertenece a `feliastu` y es privado. Hernan debe invitar al usuario
confirmado de Camilo desde **Settings > Collaborators** para que pueda trabajar.
Antes de la entrega, también debe asegurarse de que el docente tenga acceso.
El documento de la actividad no exige que el repositorio sea público.

`main.py`, `README.md`, `modelos`, `pruebas` y `docs` se encuentran en la raíz.
Las grabaciones de clase y el documento original no están incluidos.

## Obtener una copia para trabajar

Cada integrante necesita Git instalado y autenticación con su propia cuenta.
Desde una terminal en la carpeta donde quiera guardar el proyecto:

```bash
git clone https://github.com/feliastu/programacion-i-gestion-academica.git
cd programacion-i-gestion-academica
```

Si GitHub solicita autenticación, utilizar el flujo de inicio de sesión de Git
o del administrador de credenciales instalado. No compartir contraseñas o tokens
en el repositorio ni entre integrantes.

Configurar la identidad local con los datos del estudiante que realmente hará el
commit. Reemplazar los textos de ejemplo por sus datos:

```bash
git config user.name "NOMBRE REAL DEL AUTOR"
git config user.email "CORREO ASOCIADO A SU CUENTA DE GITHUB"
```

En Windows, comprobar la ejecución:

```powershell
py main.py
py -m unittest discover -s pruebas -v
```

La carga inicial con asistencia de IA no acredita por sí sola el desarrollo
individual de los dos integrantes. La declaración de IA debe permanecer y los
aportes posteriores deben ser reales.

## Trabajar sobre la misma versión

Cada integrante obtiene una copia del repositorio, crea una rama para su tarea,
realiza el cambio, ejecuta el programa y las pruebas, y registra un commit con
un mensaje que describa el aporte. Integrar las ramas conservando la autoría de
los commits individuales.

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
Revisar e integrar el aporte mediante una solicitud de cambios o el flujo que
acuerde el equipo. No cambiar la autoría para repartir créditos.

## Cerrar la versión de la actividad

Completar integrantes y contribuciones en el README, comprobar que el docente
puede acceder, ejecutar las pruebas y revisar el historial:

```bash
git log --format="%h | %an | %s"
```

Cuando todos los aportes estén integrados y antes de la fecha límite, crear una
etiqueta que identifique exactamente la versión entregada:

```bash
git switch main
git pull --ff-only
git tag -a actividad-1-v1.0 -m "Entrega de la actividad colaborativa 1"
git push origin actividad-1-v1.0
```

El nombre es una propuesta. Una etiqueta marca un commit, pero no impide por sí
misma que alguien la mueva o elimine. Conservarla sin cambios: no reemplazarla,
borrarla ni reescribir el historial de la versión entregada.

También puede crearse una versión desde la sección **Releases** de GitHub y
seleccionar la etiqueta del commit final. Para la siguiente actividad, continuar
con nuevos commits posteriores, manteniendo intacta la etiqueta de esta entrega.

## Verificación final del equipo

- [ ] El repositorio contiene un solo sistema y un único `main.py` de ejecución.
- [ ] Se ejecuta desde una copia recién descargada sin instalar paquetes externos.
- [ ] Demuestra seis personas, tres rechazos y el ciclo polimórfico.
- [ ] Los integrantes y el enlace del repositorio están completos en el README.
- [ ] Cada estudiante tiene al menos un commit de desarrollo verificable.
- [ ] El README declara de manera fiel el uso de inteligencia artificial.
- [ ] Todos pueden explicar el código y sus decisiones.
- [ ] Las pruebas pasan después de integrar los aportes.
- [ ] La etiqueta identifica el commit final y el docente tiene acceso.

Consultar las instrucciones oficiales de
[creación de repositorios](https://docs.github.com/es/repositories/creating-and-managing-repositories/creating-a-new-repository)
y de [versiones y etiquetas](https://docs.github.com/es/repositories/releasing-projects-on-github/managing-releases-in-a-repository).
