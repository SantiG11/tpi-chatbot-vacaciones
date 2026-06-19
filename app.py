# Trabajo Práctico Integrador - Organización Empresarial
# Chatbot web para gestión de solicitudes de vacaciones
# Tecnologías: Python, Streamlit y CSV

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

def main():
    #Configura la página principal
    st.set_page_config(
        page_title="Chatbot de Vacaciones",
        page_icon="💬"
    )

    st.title("Chatbot de Gestión de Vacaciones")

    st.write(
        "Asistente virtual para gestionar solicitudes de vacaciones del área de Recursos Humanos."
    )

    # Carga la base de empleados para verificar que el archivo funciona
    empleados = cargar_empleados()

    st.subheader("Verificación inicial")
    st.write("Base de empleados cargada correctamente.")

    with st.expander("Ver empleados registrados"):
        st.dataframe(empleados)






if __name__ == "__main__":
    main()