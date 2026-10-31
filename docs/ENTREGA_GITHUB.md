# Entrega individual de la actividad 2

**Estudiante:** Hernan Felipe Astudillo Peña (`feliastu`).

El enlace para colocar en la plataforma del curso es:

**https://github.com/feliastu/programacion-i-gestion-academica**

Es el mismo repositorio público de AC1. La versión de esta actividad se identifica
con la etiqueta obligatoria [Entrega_AC2](https://github.com/feliastu/programacion-i-gestion-academica/tree/Entrega_AC2).
El cierre indicado en la actividad es el **1 de noviembre de 2026 a las 23:55**.

## Contenido para evaluar

El README presenta la ejecución, la organización y las decisiones principales.
`main.py` demuestra el sistema completo. `pruebas/` contiene las 42 pruebas y
`docs/` contiene sus resultados y el Documento de Decisiones de Diseño en
[PDF](Decisiones_Diseno_AC2.pdf), [Word](Decisiones_Diseno_AC2.docx) y
[Markdown](DECISIONES_DISENO_AC2.md).

El documento incluye portada, introducción, descripción general, abstracción,
relaciones, composición, excepciones, polimorfismo, conclusiones y declaración de
asistencia de IA. Los materiales originales del curso y la grabación no se publican.

## Conservación de la primera entrega

El commit `aa1f190c328a5e4f4155d7db08570d21fbec4142` conserva la versión anterior.
La etiqueta [Entrega_AC1](https://github.com/feliastu/programacion-i-gestion-academica/tree/Entrega_AC1)
se añade sobre ese commit histórico para identificarlo; no cambia su contenido ni
pretende representar una etiqueta creada en la fecha original. La evolución de
AC2 utiliza commits posteriores en la misma rama y el mismo proyecto.

Una etiqueta es una referencia a un commit, no un bloqueo técnico contra futuros
cambios. Conservar ambas etiquetas sin moverlas ni borrarlas, y continuar cualquier
mejora con nuevos commits.

## Descargar la versión entregada

En GitHub, abrir la etiqueta Entrega_AC2 y elegir **Code > Download ZIP**.
También puede utilizarse Git:

```bash
git clone --branch Entrega_AC2 https://github.com/feliastu/programacion-i-gestion-academica.git
cd programacion-i-gestion-academica
```

La consulta y descarga públicas no requieren iniciar sesión. Ejecutar en Windows:

```powershell
py main.py
py -m unittest discover -s pruebas -v
```

## Revisión personal antes de enviar

Ejecutar ambos comandos en el computador del estudiante y revisar el documento.
Preparar la explicación de por qué Persona es abstracta, dónde se crea Horario,
qué objeto conserva cada relación y cómo una excepción evita una modificación
inválida. La [guía de estudio](GUIA_PASO_A_PASO.md) recorre esos puntos.

El historial y [el aporte individual](APORTE_INDIVIDUAL.md) describen la
implementación asistida. No sustituyen la comprensión personal. Finalmente,
pegar el enlace del repositorio en la plataforma y confirmar el envío allí.
