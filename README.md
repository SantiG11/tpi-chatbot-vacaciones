# Chatbot de Gestión de Vacaciones

Trabajo Práctico Integrador de la materia Organización Empresarial.

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un chatbot web funcional para gestionar solicitudes de vacaciones dentro de una organización ficticia.

El sistema permite que un empleado ingrese su DNI, consulte sus días disponibles, solicite una cantidad de días de vacaciones y reciba una respuesta automática según las reglas definidas del proceso.

## Organización seleccionada

La organización ficticia seleccionada es TecnoGestión S.A., una empresa de servicios tecnológicos que cuenta con distintas áreas internas, entre ellas Recursos Humanos, Sistemas, Administración, Ventas y Soporte Técnico.

## Proceso administrativo elegido

El proceso elegido es la gestión de solicitudes de vacaciones de empleados.

Actualmente, este tipo de trámite suele realizarse mediante mensajes, correos o consultas directas al área de Recursos Humanos, lo que puede generar demoras, errores de registro y falta de trazabilidad.

## Solución propuesta

Se propone automatizar el proceso mediante un chatbot web desarrollado en Python con Streamlit.

El bot permite:

- Identificar al empleado mediante DNI.
- Consultar sus días disponibles.
- Solicitar una cantidad de días de vacaciones.
- Aprobar la solicitud si existe saldo suficiente.
- Rechazar la solicitud si no existe saldo suficiente.
- Registrar cada solicitud en un archivo CSV.
- Manejar errores de entrada del usuario.

## Tecnologías utilizadas

- Python
- Streamlit
- Pandas
- CSV como base de datos simulada
- Git y GitHub

## Estructura del proyecto

```text
tpi-chatbot-vacaciones/
│
├── app.py
├── empleados.csv
├── solicitudes.csv
├── README.md
├── requirements.txt
├── .gitignore
│
├── documentacion/
│   ├── analisis_sistemico.md
│   ├── flujo_bpmn_codigo.md
│   ├── maquina_estados.md
│   └── capturas/
│
└── prompts_ia/
    └── prompts_usados.md
```
