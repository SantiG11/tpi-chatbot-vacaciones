from pathlib import Path

import pandas as pd
import streamlit as st


# Carpeta principal del proyecto
BASE_DIR = Path(__file__).resolve().parent

# Rutas de los archivos CSV
EMPLEADOS_CSV = BASE_DIR / "empleados.csv"
SOLICITUDES_CSV = BASE_DIR / "solicitudes.csv"


def cargar_empleados():
    # Carga los empleados desde el archivo CSV
    empleados = pd.read_csv(EMPLEADOS_CSV, dtype={"dni": str})

    return empleados

def guardar_empleados(empleados):
    # Guarda los cambios en el archivo de empleados
    empleados.to_csv(EMPLEADOS_CSV, index=False)

def cargar_solicitudes():
    # Carga las solicitudes registradas desde el archivo CSV
    solicitudes = pd.read_csv(SOLICITUDES_CSV, dtype={"dni": str})

    return solicitudes

def obtener_id_solicitud():
    # Genera el número de la próxima solicitud
    solicitudes = cargar_solicitudes()

    if solicitudes.empty:
        return 1

    return len(solicitudes) + 1

def registrar_solicitud(empleado, dias_solicitados, estado, motivo):
    # Guarda una nueva solicitud en el archivo CSV
    solicitudes = cargar_solicitudes()

    nueva_solicitud = {
        "id_solicitud": obtener_id_solicitud(),
        "dni": empleado["dni"],
        "nombre_completo": f"{empleado['nombre']} {empleado['apellido']}",
        "sector": empleado["sector"],
        "dias_solicitados": dias_solicitados,
        "estado": estado,
        "motivo": motivo,
    }

    solicitudes.loc[len(solicitudes)] = nueva_solicitud

    solicitudes.to_csv(SOLICITUDES_CSV, index=False)

def actualizar_dias_disponibles(dni, dias_solicitados):
    # Descuenta los días aprobados del empleados
    empleados = cargar_empleados()

    empleados.loc[
        empleados["dni"] == dni,
        "dias_disponibles"
    ] = empleados.loc[
        empleados["dni"] == dni,
        "dias_disponibles"
    ].astype(int) - dias_solicitados

    guardar_empleados(empleados)

def buscar_empleado(dni):
    # Busca un empleado según el DNI ingresado
    empleados = cargar_empleados()

    empleado = empleados[empleados["dni"] == dni]

    if empleado.empty:
        return None

    return empleado.iloc[0]

def validar_dni(dni):
    # Valida que el DNI no esté vacío y tenga solo números
    dni = dni.strip()

    if dni == "":
        return False, "El DNI no puede estar vacío."

    if not dni.isdigit():
        return False, "El DNI debe contener solo números."

    return True, ""

def procesar_dni(texto_usuario):
    # Procesa el DNI ingresado por el usuario
    dni = texto_usuario.strip()

    dni_valido, mensaje_error = validar_dni(dni)

    if not dni_valido:
        agregar_mensaje("assistant", mensaje_error)
        return

    empleado = buscar_empleado(dni)

    if empleado is None:
        agregar_mensaje(
            "assistant",
            "No se encontró un empleado registrado con ese DNI. Verificá el dato e intentá nuevamente."
        )
        return
    
    st.session_state.empleado = empleado
    st.session_state.estado = "ESPERANDO_CANTIDAD_DIAS"

    agregar_mensaje(
        "assistant",
        (
            f"Empleado encontrado: {empleado['nombre']} {empleado['apellido']}. "
            f"Sector: {empleado['sector']}. "
            f"Días disponibles: {empleado['dias_disponibles']}."
            "¿Cuántos días de vacaciones querés solicitar?"
        )
    )

def procesar_cantidad_dias(texto_usuario):
     # Valida la cantidad de días solicitados
    cantidad = texto_usuario.strip()

    if cantidad == "":
        agregar_mensaje(
            "assistant",
            "La cantidad de días no puede estar vacía. Ingresá un número entero mayor a 0."
        )
        return

    try:
        dias_solicitados = int(cantidad)
    except ValueError:
        agregar_mensaje(
            "assistant",
            "La cantidad debe ser un número entero. Por favor, intentá nuevamente."
        )
        return

    if dias_solicitados <= 0:
        agregar_mensaje(
            "assistant",
            "La cantidad solicitada debe ser mayor a 0. Por favor, intentá nuevamente."
        )
        return

    empleado = st.session_state.empleado
    dias_disponibles = int(empleado["dias_disponibles"])

    if dias_solicitados > dias_disponibles:
        registrar_solicitud(
            empleado,
            dias_solicitados,
            "Rechazada",
            "Saldo insuficiente"
        )

        st.session_state.estado = "SOLICITUD_RECHAZADA"

        agregar_mensaje(
            "assistant",
            (
                "Solicitud rechazada. "
                f"Pediste {dias_solicitados} días, pero solo tenés "
                f"{dias_disponibles} días disponibles."
                "La solicitud fue registrada con estado Rechazada"
            )
        )
        return
    
    registrar_solicitud(
        empleado,
        dias_solicitados,
        "Aprobada",
        "Saldo suficiente"
    )

    actualizar_dias_disponibles(empleado["dni"], dias_solicitados)

    nuevo_saldo = dias_disponibles - dias_solicitados

    st.session_state.estado = "SOLICITUD_APROBADA"

    agregar_mensaje(
        "assistant",
        (
            "Solicitud aprobada. "
            f"Tenés saldo suficiente para solicitar {dias_solicitados} días de vacaciones." 
            f"Tu nuevo saldo disponible es de {nuevo_saldo} días."
        )
    )

def procesar_entrada(texto_usuario):
    # Decide qué hacer según el estado actual del bot
    agregar_mensaje("user", texto_usuario)

    if st.session_state.estado == "ESPERANDO_DNI":
        procesar_dni(texto_usuario)

    elif st.session_state.estado == "ESPERANDO_CANTIDAD_DIAS":
        procesar_cantidad_dias(texto_usuario)

    else:
        agregar_mensaje(
            "assistant",
            "El proceso actual ya finalizó. Para hacer otra solicitud, usá el botón de nueva solicitud."
        )

def iniciar_chat():
    # Crea el historial inicial del chat si todavía no existe
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = [
            {
                "role": "assistant",
                "content": (
                    "Hola, soy el asistente virtual de Recursos Humanos. "
                    "Para comenzar, ingresá tu DNI."
                ),
            }
        ]

    # Guarda en qué parte del proceso está el usuario
    if "estado" not in st.session_state:
        st.session_state.estado = "ESPERANDO_DNI"

    # Guarda los datos del empleado cuando el DNI sea válido
    if "empleado" not in st.session_state:
        st.session_state.empleado = None


def mostrar_mensajes():
    # Muestra todos los mensajes guardados en el chat
    for mensaje in st.session_state.mensajes:
        with st.chat_message(mensaje["role"]):
            st.write(mensaje["content"])


def agregar_mensaje(rol, contenido):
    # Agrega un nuevo mensaje al historial del chat
    st.session_state.mensajes.append(
        {
            "role": rol,
            "content": contenido,
        }
    )

def reiniciar_solicitud():
    # Reinicia el chat para cargar una nueva solicitud
    st.session_state.estado = "ESPERANDO_DNI"
    st.session_state.empleado = None
    
    st.session_state.mensajes = [
        {
            "role": "assistant",
            "content": (
                "Nueva solicitud iniciada."
                "Por favor, ingresá tu DNI"
            )
        }
    ]

def mostrar_controles():
    # Muestra opciones cuando el proceso ya terminó
    if st.session_state.estado in ["SOLICITUD_APROBADA", "SOLICITUD_RECHAZADA"]:
        if st.button("Iniciar nueva solicitud"):
            reiniciar_solicitud()
            st.rerun()

def main():
    # Configura la página principal
    st.set_page_config(
        page_title="Chatbot de Vacaciones",
        page_icon="💬"
    )

    st.title("Chatbot de Gestión de Vacaciones")

    st.write(
        "Asistente virtual para gestionar solicitudes de vacaciones "
        "del área de Recursos Humanos."
    )

    # Carga los empleados para verificar que la base esté disponible
    empleados = cargar_empleados()

    with st.expander("Ver empleados registrados"):
        st.dataframe(empleados)

    iniciar_chat()
    mostrar_mensajes()
    mostrar_controles()

    texto_usuario = st.chat_input("Escribí tu mensaje...")

    if texto_usuario:
        procesar_entrada(texto_usuario)
        st.rerun()


if __name__ == "__main__":
    main()