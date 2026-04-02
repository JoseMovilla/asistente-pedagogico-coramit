import streamlit as st
import google.generativeai as genai

# Configuración básica
st.set_page_config(page_title="Asistente CORAMIT", page_icon="🧸")

st.title("🧸 Asistente de Planeación 2026")

# Entrada de la llave
api_key = st.sidebar.text_input("Pega tu API Key:", type="password")
mes = st.sidebar.selectbox("Mes", ["Marzo", "Abril", "Mayo", "Junio"])
semana = st.sidebar.selectbox("Semana", ["Semana 1", "Semana 2", "Semana 3", "Semana 4"])

if st.sidebar.button("🚀 GENERAR"):
    if not api_key:
        st.error("Escribe la API Key")
    else:
        try:
            # 1. Configurar la llave
            genai.configure(api_key=api_key)
            
            # 2. PROBAR CON EL MODELO MÁS BÁSICO POSIBLE
            # Si 'gemini-1.5-flash' falla, el sistema nos dirá por qué
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"Genera una tabla de planeación pedagógica para la {semana} de {mes} sobre literatura infantil para niños de 1 a 4 años. Usa formato de tabla de 6 filas."
            
            with st.spinner('Generando...'):
                response = model.generate_content(prompt)
                st.success("¡Conexión exitosa!")
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"Error técnico: {e}")
            st.info("Si el error es 404, intenta cambiar en el código 'gemini-1.5-flash' por 'models/gemini-1.5-flash'")
