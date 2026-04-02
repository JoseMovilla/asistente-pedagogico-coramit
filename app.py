import streamlit as st
import google.generativeai as genai

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Asistente Pedagógico CORAMIT", page_icon="🧸", layout="wide")

# --- INTERFAZ VISUAL ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3471/3471161.png", width=100)
st.sidebar.title("Configuración")

api_key = st.sidebar.text_input("Pega tu API Key de Google aquí:", type="password")
mes = st.sidebar.selectbox("Mes de trabajo", ["Marzo", "Abril", "Mayo", "Junio", "Julio"])
semana = st.sidebar.selectbox("Semana del mes", ["Semana 1", "Semana 2", "Semana 3", "Semana 4"])
tema_sugerido = "Explorando el mundo del Juego y la Literatura" if mes == "Abril" else "Mi cuerpo, mi mayor tesoro"
tema = st.sidebar.text_input("Tema del Proyecto", value=tema_sugerido)

st.title("🗂️ Asistente de Planeación Pedagógica 2026")
st.write("Genera planeaciones profesionales para CDI y HCB bajo lineamientos de CORAMIT e ICBF.")

if st.sidebar.button("🚀 GENERAR PLANEACIÓN"):
    if not api_key:
        st.error("Por favor, pega tu API Key en la barra lateral.")
    else:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        # EL PROMPT MAESTRO QUE PERFECCIONAMOS
        prompt = f"""
        Actúa como Coordinador Pedagógico de CORAMIT. Genera la planeación de la {semana} de {mes}.
        Tema: {tema}. Grupo: 1 a 4 años.
        REGLAS: 
        1. Tabla de 6 filas exactas (Materiales, Espacio, Inicio, Desarrollo, Cierre, Documentación).
        2. Desarrollo con nombres de cuentos y canciones reales.
        3. Actividad manual obligatoria cada día.
        4. Resumen CORAMIT NARRATIVO: No empieces con infinitivos. Usa "Se busca que...", "La finalidad es...".
        5. Enfoque 100% laico.
        """
        
        with st.spinner('Redactando planeación técnica...'):
            response = model.generate_content(prompt)
            st.success("¡Planeación Generada!")
            st.markdown(response.text)

