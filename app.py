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
        agregar_mensaje("user", texto_usuario)

        agregar_mensaje(
            "assistant",
            "Recibí tu mensaje. En el próximo paso voy a validar el DNI ingresado."
        )

        st.rerun()


if __name__ == "__main__":
    main()