import streamlit as st
import google.generativeai as genai

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Asistente Pedagógico CORAMIT", page_icon="🧸", layout="wide")

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; background-color: #2e7d32; color: white; height: 3em; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL (CONFIGURACIÓN) ---
st.sidebar.title("⚙️ Configuración")
api_key = st.sidebar.text_input("Pega tu API Key de Google aquí:", type="password")

st.sidebar.divider()
mes = st.sidebar.selectbox("Mes de trabajo", ["Marzo", "Abril", "Mayo", "Junio", "Julio"])
semana = st.sidebar.selectbox("Semana del mes", ["Semana 1", "Semana 2", "Semana 3", "Semana 4", "Semana 5"])
tema_sugerido = "Explorando el mundo del Juego y la Literatura" if mes == "Abril" else "Mi cuerpo, mi mayor tesoro"
tema_proyecto = st.sidebar.text_input("Nombre del Proyecto", value=tema_sugerido)

st.sidebar.info("Este asistente genera planeaciones multinivel (1-4 años) siguiendo el formato técnico de CORAMIT.")

# --- CUERPO PRINCIPAL ---
st.title("🧸 Asistente de Planeación Pedagógica 2026")
st.write(f"Generando contenido para el proyecto: **{tema_proyecto}**")

if st.sidebar.button("🚀 GENERAR PLANEACIÓN COMPLETA"):
    if not api_key:
        st.error("❌ Por favor, pega tu API Key en la barra lateral izquierda para continuar.")
    else:
        try:
            # Configuración del modelo Gemini 3.1 Flash Preview (visto en tu imagen)
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash-latest') # He puesto flash para asegurar compatibilidad, pero si prefieres el 3.1 cámbialo a 'gemini-3.1-flash-preview'
            
            # PROMPT MAESTRO CON TODAS TUS REGLAS
            prompt = f"""
            Actúa como Coordinador Pedagógico Senior de la Corporación Amigos de la Tierra (CORAMIT). 
            Genera la planeación pedagógica de la {semana} de {mes}.
            
            DATOS CLAVE:
            - Proyecto: {tema_proyecto}
            - Grupo: Multinivel (Niños y niñas de 1 a 4 años).
            - Enfoque: 100% Laico (sin religión), sin apartados de inclusión.
            
            ESTRUCTURA OBLIGATORIA:
            
            PARTE 1: ENCABEZADO DEL PROYECTO
            Incluye: Justificación técnica (1 párrafo), 5 Objetivos pedagógicos, Color del mes, Canción del mes (con nombre real) y Valor del mes.
            
            PARTE 2: PLANEACIÓN SEMANAL (TABLA POR DÍA)
            Para cada día (Lunes a Viernes), genera una tabla con estas 6 filas exactas:
            1. MATERIALES A UTILIZAR (Específicos).
            2. DESCRIPCIÓN DEL ESPACIO PEDAGÓGICO/AMBIENTE EDUCATIVO.
            3. ACTIVIDAD DE INICIO (Bienvenida con canción real, asamblea y agradecimiento laico).
            4. ACTIVIDAD DE DESARROLLO (Incluye nombre de cuento real, video de YouTube de apoyo y ACTIVIDAD MANUAL de dibujo/decoración/modelado).
            5. ACTIVIDAD DE CIERRE (Socialización y orden).
            6. DOCUMENTACIÓN (Registro fotográfico).
            
            PARTE 3: RESUMEN CORAMIT (PARA EL FORMATO FÍSICO)
            Redacta la "Descripción de la experiencia" de lunes a viernes con LENGUAJE NARRATIVO NATURAL.
            REGLA CRÍTICA: Prohibido empezar las frases con verbos en infinitivo (Ej: No uses 'Fomentar...', 'Promover...'). 
            Usa conectores como: 'Se busca que los niños y niñas...', 'La finalidad es...', 'Incentivar a los pequeños a...'.
            """
            
            with st.spinner('⏳ El asistente está redactando, espera un momento...'):
                response = model.generate_content(prompt)
                
                # Visualización de resultados en pestañas
                tab1, tab2 = st.tabs(["📋 Planeación Detallada", "📝 Resumen CORAMIT"])
                
                with tab1:
                    st.markdown(response.text.split("PARTE 3:")[0])
                
                with tab2:
                    if "PARTE 3:" in response.text:
                        st.markdown(response.text.split("PARTE 3:")[1])
                    else:
                        st.markdown(response.text)
                        
                st.success("✅ ¡Planeación generada con éxito! Ya puedes copiar el contenido.")
                
        except Exception as e:
            st.error(f"Se produjo un error de conexión: {e}")
            st.info("Nota: Si el error persiste, verifica que la API Key sea la correcta.")
