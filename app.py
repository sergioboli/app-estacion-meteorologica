import requests
import streamlit as st

# Configuración de la página (modo móvil amigable)
st.set_page_config(
    page_title="Estación Meteorológica Escolar", page_icon="⛅", layout="centered"
)

# Estilos personalizados (fondo casi negro, tarjetas con transparencia y hover)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #050505;
        color: #ffffff;
    }
    .weather-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
        margin-bottom: 15px;
    }
    .weather-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 20px rgba(0, 255, 128, 0.2);
        border-color: #00ff80;
    }
    .weather-card h3 {
        margin: 0;
        font-size: 1rem;
        color: #a0a0a0;
    }
    .weather-card h2 {
        margin: 10px 0 0 0;
        font-size: 1.8rem;
        color: #ffffff;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.title("⛅ Estación IOLIVA129")
st.markdown("---")

# URL OFICIAL DE TU SERVIDOR EN RENDER
URL_API = "https://estacion-meteorologica-profe.onrender.com/api/estado"


def obtener_datos():
  try:
    response = requests.get(URL_API, timeout=5)
    if response.status_code == 200:
      return response.json()
  except:
    pass
  return None


datos = obtener_datos()

if datos:
  st.caption(f"📅 Última actualización: {datos.get('fecha', 'N/D')}")

  # Estructura en tarjetas (2 columnas)
  col1, col2 = st.columns(2)

  with col1:
    st.markdown(
        f"""
        <div class="weather-card">
            <h3>🌡️ Temperatura</h3>
            <h2>{datos.get('temperatura_C', '--')} °C</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div class="weather-card">
            <h3>💨 Viento</h3>
            <h2>{datos.get('viento_kmh', '--')} km/h</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

  with col2:
    st.markdown(
        f"""
        <div class="weather-card">
            <h3>💧 Humedad</h3>
            <h2>{datos.get('humedad_pct', '--')} %</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div class="weather-card">
            <h3>🌧️ Lluvia</h3>
            <h2>{datos.get('lluvia_acumulada_mm', '--')} mm</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

  # ZONA DE MODIFICACIÓN PARA CLASE
  temp = datos.get("temperatura_C", 0)
  if temp and temp > 25:
    st.warning("⚠️ ¡Aviso: Temperatura superior a 25 °C!")

else:
  st.error("⚠️ No se pudo conectar con el servidor central de Render.")
