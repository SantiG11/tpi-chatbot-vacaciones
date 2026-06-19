# Chatbot de Solicitud de Vacaciones

Trabajo Práctico Integrador de Organización Empresarial.

Este proyecto consiste en el análisis, modelado y automatización del proceso de solicitud de vacaciones dentro del área de Recursos Humanos de una organización ficticia llamada TecnoGestión S.A.

La solución desarrollada es un chatbot web que permite a un empleado ingresar su DNI, consultar sus días disponibles, solicitar una cantidad de días de vacaciones y recibir una respuesta automática según el saldo disponible.

## Objetivo del proyecto

El objetivo es transformar un proceso administrativo manual en una solución simple, funcional y trazable. Para esto se modeló el proceso actual AS-IS, se propuso un proceso optimizado TO-BE y se desarrolló un chatbot que representa el funcionamiento del proceso automatizado.

## Tecnologías utilizadas

- Python
- Streamlit
- Pandas
- Archivos CSV
- Git y GitHub
- BPMN 2.0

## Funcionamiento general

El chatbot guía al usuario a través del proceso de solicitud de vacaciones. Primero solicita el DNI del empleado y valida que el dato ingresado sea correcto. Luego consulta el archivo empleados.csv para verificar si el empleado existe y cuántos días de vacaciones tiene disponibles.

Si el empleado cuenta con días disponibles, el sistema solicita la cantidad de días que desea pedir. Luego valida la cantidad ingresada y compara el valor solicitado con el saldo disponible.

Si el saldo es suficiente, la solicitud se aprueba, se registra en solicitudes.csv y se actualizan los días disponibles en empleados.csv. Si el saldo no alcanza, la solicitud se rechaza y también se registra el motivo.

## Archivos principales

- app.py: archivo principal de la aplicación.
- empleados.csv: contiene los empleados registrados y sus días disponibles.
- solicitudes.csv: registra las solicitudes realizadas y su resultado.
- README.md: documentación principal del proyecto.
- documentacion/: carpeta con documentación complementaria, diagramas BPMN y capturas.
- prompts_ia/: carpeta con el registro del uso de inteligencia artificial durante el desarrollo.

## Instalación y ejecución

Para ejecutar el proyecto de forma local, primero se deben instalar las librerías necesarias:

```bash
pip install streamlit pandas
```

Luego, desde la carpeta principal del proyecto, se ejecuta la aplicación con el siguiente comando:

```bash
python -m streamlit run app.py
```

La aplicación se abrirá en el navegador y permitirá interactuar con el chatbot.

## Diagramas BPMN

Los diagramas del proceso se encuentran dentro de la carpeta documentacion/:

- bpmn_as_is.png: representa el proceso actual manual.
- bpmn_to_be.png: representa el proceso optimizado mediante el chatbot.

## Pruebas realizadas

Se realizaron pruebas sobre el flujo principal y sobre distintos caminos de error:

- Solicitud aprobada con saldo suficiente.
- Solicitud rechazada por saldo insuficiente.
- DNI inválido.
- DNI inexistente.
- Empleado sin días disponibles.
- Cantidad inválida.
- Actualización de días disponibles.
- Registro de solicitudes en el archivo CSV.

## Uso de inteligencia artificial

El uso de inteligencia artificial durante el desarrollo se encuentra documentado en la carpeta prompts_ia/. Allí se registran ejemplos representativos de prompts utilizados para organizar el trabajo, seleccionar herramientas, estructurar el código, resolver dudas técnicas y revisar la coherencia entre BPMN y chatbot.

## Estado del proyecto

El proyecto se encuentra funcional y cumple con el flujo principal definido para la solicitud de vacaciones. La aplicación permite consultar empleados, validar datos, registrar solicitudes y actualizar la información correspondiente.
