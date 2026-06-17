# Relación entre BPMN y código

Este documento describe la relación entre el flujo modelado en BPMN y la lógica implementada en el chatbot.

| Elemento del proceso             | Representación en el código                           |
| -------------------------------- | ----------------------------------------------------- |
| Inicio del proceso               | Inicio de la aplicación en Streamlit                  |
| Usuario ingresa DNI              | Entrada mediante chat                                 |
| Validación de DNI                | Control de campo vacío y formato numérico             |
| Consulta de empleado             | Búsqueda en `empleados.csv`                           |
| Gateway: ¿empleado existe?       | Condicional que verifica si el DNI está registrado    |
| Bot informa días disponibles     | Mensaje generado con datos del empleado               |
| Usuario ingresa días solicitados | Entrada mediante chat                                 |
| Gateway: ¿cantidad válida?       | Validación de número entero mayor a cero              |
| Gateway: ¿saldo suficiente?      | Comparación entre días solicitados y días disponibles |
| Solicitud aprobada               | Registro con estado “Aprobada” en `solicitudes.csv`   |
| Solicitud rechazada              | Registro con estado “Rechazada” en `solicitudes.csv`  |
| Fin del proceso                  | Mensaje final y opción de nueva solicitud             |
