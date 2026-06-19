# Máquina de estados del chatbot

El chatbot utiliza una lógica de estados para controlar el avance del proceso. Esto permite saber qué dato debe ingresar el usuario en cada momento y evita que una respuesta sea interpretada de forma incorrecta.

## Estados principales

| Estado                  | Descripción                                                                                             |
| ----------------------- | ------------------------------------------------------------------------------------------------------- |
| ESPERANDO_DNI           | El bot espera que el usuario ingrese su DNI.                                                            |
| ESPERANDO_CANTIDAD_DIAS | El empleado fue identificado y el bot espera la cantidad de días solicitados.                           |
| SOLICITUD_APROBADA      | La solicitud fue aprobada porque el saldo era suficiente.                                               |
| SOLICITUD_RECHAZADA     | La solicitud fue rechazada porque la cantidad solicitada superaba el saldo disponible.                  |
| FINALIZADO              | El proceso terminó sin generar una solicitud, por ejemplo cuando el empleado no tiene días disponibles. |

## Caminos de error contemplados

- DNI vacío.
- DNI con caracteres no numéricos.
- DNI inexistente.
- Empleado sin días disponibles.
- Cantidad ingresada como texto.
- Cantidad menor o igual a cero.
- Cantidad mayor al saldo disponible.

## Importancia de la lógica de estados

La máquina de estados permite que el chatbot mantenga un flujo ordenado. Si el sistema está esperando un DNI, interpreta la entrada del usuario como documento. Si ya identificó al empleado, interpreta la siguiente entrada como cantidad de días solicitados.

De esta forma, el proceso se mantiene controlado y se evitan avances incorrectos con datos inválidos o incompletos.
