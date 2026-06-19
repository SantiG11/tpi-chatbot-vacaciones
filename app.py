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
    # Recibe la cantidad de días solicitados por el empleado
    empleado = st.session_state.empleado

    agregar_mensaje(
        "assistant",
        (
            f"Recibí tu solicitud para {empleado['nombre']} {empleado['apellido']}. "
            f"Cantidad ingresada: {texto_usuario}. "
            "En el próximo paso voy a validar si la cantidad es correcta y si hay saldo disponible."
        )
    )

def procesar_entrada(texto_usuario):
    # Decide qué hacer según el estado actual del bot
    agregar_mensaje("user", texto_usuario)

    if st.session_state.estado == "ESPERANDO_DNI":
        procesar_dni(texto_usuario)

    elif st.session_state.estado == "ESPERANDO_CANTIDAD_DIAS":
        procesar_cantidad_dias(texto_usuario)

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

    texto_usuario = st.chat_input("Escribí tu mensaje...")

    if texto_usuario:
        procesar_entrada(texto_usuario)
        st.rerun()


if __name__ == "__main__":
    main()