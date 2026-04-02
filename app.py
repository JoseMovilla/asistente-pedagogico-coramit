import streamlit as st
import google.generativeai as genai
import google.ai.generativelanguage as glm

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Asistente Pedagógico CORAMIT", page_icon="🧸", layout="wide")

st.sidebar.title("Configuración")
api_key = st.sidebar.text_input("Pega tu API Key de Google aquí:", type="password")
mes = st.sidebar.selectbox("Mes de trabajo", ["Marzo", "Abril", "Mayo", "Junio", "Julio"])
semana = st.sidebar.selectbox("Semana del mes", ["Semana 1", "Semana 2", "Semana 3", "Semana 4"])
tema = st.sidebar.text_input("Tema del Proyecto", value="Explorando el mundo del Juego y la Literatura")

st.title("🗂️ Asistente de Planeación Pedagógica 2026")

if st.sidebar.button("🚀 GENERAR PLANEACIÓN"):
    if not api_key:
        st.error("Por favor, pega tu API Key.")
    else:
        try:
            # Forzamos la configuración para evitar el error NotFound
            genai.configure(api_key=api_key)
            
            # Usamos el modelo Flash que es el más compatible
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"""
            Genera la planeación pedagógica de la {semana} de {mes}.
            Tema: {tema}. Grupo: 1 a 4 años.
            REGLAS ESTRICTAS: 
            1. Tabla de 6 filas (Materiales, Espacio, Inicio, Desarrollo, Cierre, Documentación).
            2. Desarrollo con nombres de cuentos y canciones reales.
            3. Resumen CORAMIT NARRATIVO: No empieces con infinitivos. Usa "Se busca que...", "La finalidad es...".
            """
            
            with st.spinner('Conectando con el servidor de Google...'):
                # Esta es la llamada que a veces falla, la envolvemos en un chequeo
                response = model.generate_content(prompt)
                st.success("¡Logramos la conexión!")
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"Hubo un problema con la llave API o el modelo: {e}")
            st.info("💡 Consejo: Asegúrate de que tu API Key sea de 'Google AI Studio' y no de 'Google Cloud Console'.")
