# Relación entre BPMN TO-BE y código

El proceso TO-BE modelado en BPMN se corresponde con la lógica implementada en el chatbot. Cada decisión principal del diagrama está representada en el código mediante validaciones, condiciones y cambios de estado.

| Elemento del BPMN TO-BE          | Implementación en el código                                         |
| -------------------------------- | ------------------------------------------------------------------- |
| Solicitud de DNI                 | Mensaje inicial del chatbot y estado ESPERANDO_DNI                  |
| Validación del DNI               | Función validar_dni()                                               |
| Consulta del empleado            | Función buscar_empleado() y lectura de empleados.csv                |
| Empleado no encontrado           | Condición que informa el error y permite ingresar nuevamente el DNI |
| Consulta de días disponibles     | Lectura del campo dias_disponibles del empleado                     |
| Empleado sin días disponibles    | Finalización del proceso sin registrar solicitud                    |
| Solicitud de cantidad de días    | Estado ESPERANDO_CANTIDAD_DIAS                                      |
| Validación de cantidad           | Control de número entero mayor a cero                               |
| Verificación de saldo suficiente | Comparación entre dias_solicitados y dias_disponibles               |
| Solicitud aprobada               | Registro en solicitudes.csv y actualización de empleados.csv        |
| Solicitud rechazada              | Registro en solicitudes.csv con motivo de rechazo                   |
| Nueva solicitud                  | Reinicio del estado del chatbot                                     |

Esta relación permite comprobar que el diagrama no es solo una representación teórica, sino que refleja el funcionamiento real de la solución desarrollada.
