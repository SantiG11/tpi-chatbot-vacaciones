# Máquina de estados del chatbot

El chatbot utiliza una lógica de estados para saber en qué etapa del proceso se encuentra el usuario.

## Estados definidos

| Estado                  | Descripción                                                                         |
| ----------------------- | ----------------------------------------------------------------------------------- |
| INICIO                  | El bot inicia la conversación y presenta el proceso                                 |
| ESPERANDO_DNI           | El bot espera que el usuario ingrese su DNI                                         |
| VALIDANDO_DNI           | El sistema valida el formato del DNI                                                |
| EMPLEADO_VALIDADO       | El sistema encontró al empleado en la base de datos                                 |
| ESPERANDO_CANTIDAD_DIAS | El bot espera que el usuario indique cuántos días desea solicitar                   |
| VALIDANDO_SOLICITUD     | El sistema valida si la cantidad ingresada es correcta y si existe saldo suficiente |
| SOLICITUD_APROBADA      | La solicitud fue aprobada y registrada                                              |
| SOLICITUD_RECHAZADA     | La solicitud fue rechazada y registrada                                             |
| FINALIZADO              | El proceso finaliza o queda disponible para una nueva solicitud                     |

## Caminos infelices contemplados

- DNI vacío.
- DNI con letras o símbolos.
- DNI inexistente.
- Cantidad vacía.
- Cantidad no numérica.
- Cantidad menor o igual a cero.
- Cantidad mayor a los días disponibles.
- Empleado sin días disponibles.

## Importancia de la máquina de estados

La máquina de estados permite que el chatbot conserve el contexto de la conversación y responda de manera coherente según el paso en el que se encuentra el usuario.
