import requests
import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN DEL SISTEMA Y METADATOS
# ==========================================
st.set_page_config(
    page_title="NEO-METEO // IOLIVA129", page_icon="⚡", layout="centered"
)

# ==========================================
# 2. ESTILOS CSS AVANZADOS (ESTÉTICA FUTURISTA)
# ==========================================
# Inyectamos CSS personalizado para lograr un aspecto de interfaz cibernética:
# - Fondo negro profundo (#030305)
# - Tarjetas con efectos de cristal translúcido y bordes de neón
# - Animaciones de desplazamiento y destellos al pasar el ratón (hover)
st.markdown(
    """
    <style>
    /* Configuración general de la pantalla */
    .stApp {
        background-color: #030305;
        color: #00ffcc;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Contenedor del título principal con efecto de brillo */
    .hero-title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 800;
        color: #ffffff;
        text-shadow: 0 0 10px rgba(0, 255, 204, 0.5), 0 0 20px rgba(0, 255, 204, 0.2);
        letter-spacing: 2px;
        margin-bottom: 0px;
    }
    
    .hero-subtitle {
        text-align: center;
        font-size: 0.85rem;
        color: #00ffcc;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-bottom: 25px;
    }

    /* Tarjeta futurista (Glassmorphism + Neón) */
    .cyber-card {
        background: rgba(0, 255, 204, 0.02);
        border: 1px solid rgba(0, 255, 204, 0.15);
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.8);
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        margin-bottom: 15px;
        position: relative;
        overflow: hidden;
    }

    /* Efecto interactivo al pasar el ratón (Hover Pro) */
    .cyber-card:hover {
        transform: translateY(-8px) scale(1.02);
        background: rgba(0, 255, 128, 0.05);
        border-color: #00ff80;
        box-shadow: 0 0 25px rgba(0, 255, 128, 0.4), inset 0 0 10px rgba(0, 255, 128, 0.2);
    }

    /* Iconografía grande */
    .cyber-icon {
        font-size: 2.8rem;
        margin-bottom: 5px;
        filter: drop-shadow(0 0 8px rgba(255, 255, 255, 0.3));
    }

    /* Títulos de las métricas */
    .cyber-card h3 {
        margin: 0;
        font-size: 0.8rem;
        color: #8c9ba5;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }

    /* Valores numéricos principales */
    .cyber-card h2 {
        margin: 8px 0 0 0;
        font-size: 1.7rem;
        color: #ffffff;
        font-weight: 700;
        text-shadow: 0 0 8px rgba(255, 255, 255, 0.4);
    }

    /* Indicador de estado en línea (Pulse animation) */
    .status-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        background: rgba(0, 255, 128, 0.1);
        border: 1px solid #00ff80;
        color: #00ff80;
        font-size: 0.75rem;
        letter-spacing: 1px;
        margin-bottom: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ==========================================
# 3. ENCABEZADO VISUAL
# ==========================================
st.markdown('<div class="hero-title">⚡ NEO-METEO ⚡</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-subtitle">Estación Táctica Central // IOLIVA129</div>',
    unsafe_allow_html=True,
)

# ==========================================
# 4. CONEXIÓN CON EL BACKEND (API RENDER)
# ==========================================
URL_API = "https://estacion-meteorologica-profe.onrender.com/api/estado"


@st.cache_data(ttl=30)  # Caché inteligente de 30 segundos para optimizar peticiones
def sincronizar_telemetria():
  """Realiza una petición HTTP GET segura al servidor central Flask en Render.

  Devuelve un diccionario con los datos o None si falla la conexión.
  """
  try:
    response = requests.get(URL_API, timeout=5)
    if response.status_code == 200:
      return response.json()
  except Exception as err:
    print(f"Error de enlace con la red: {err}")
  return None


# Ejecución de la sincronización
telemetria = sincronizar_telemetria()

# ==========================================
# 5. RENDERIZADO DE LA INTERFAZ DE DATOS
# ==========================================
if telemetria:
  # Estado de conexión en tiempo real
  col_estado, _ = st.columns([1, 1])
  with col_estado:
    st.markdown(
        f'<div class="status-badge">🟢 SISTEMA ONLINE — SYNC:'
        f" {telemetria.get('fecha', 'N/D')}</div>",
        unsafe_allow_html=True,
    )

  # Distribución de alta densidad en 3 columnas simétricas
  c1, c2, c3 = st.columns(3)

  with c1:
    st.markdown(
        f"""
        <div class="cyber-card">
            <div class="cyber-icon">🌡️</div>
            <h3>Temperatura</h3>
            <h2>{telemetria.get('temperatura_C', '--')} °C</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div class="cyber-card">
            <div class="cyber-icon">💨</div>
            <h3>Viento</h3>
            <h2>{telemetria.get('viento_kmh', '--')} km/h</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

  with c2:
    st.markdown(
        f"""
        <div class="cyber-card">
            <div class="cyber-icon">💧</div>
            <h3>Humedad</h3>
            <h2>{telemetria.get('humedad_pct', '--')} %</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div class="cyber-card">
            <div class="cyber-icon">🌪️</div>
            <h3>Ráfaga Máx</h3>
            <h2>{telemetria.get('rafaga_kmh', '--')} km/h</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

  with c3:
    st.markdown(
        f"""
        <div class="cyber-card">
            <div class="cyber-icon">🌧️</div>
            <h3>Precipitación</h3>
            <h2>{telemetria.get('lluvia_acumulada_mm', '--')} mm</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div class="cyber-card">
            <div class="cyber-icon">☀️</div>
            <h3>Índice UV</h3>
            <h2>{telemetria.get('indice_uv', '--')}</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

  # Fila secundaria inferior para parámetros avanzados de radiación y vector de viento
  col_sub1, col_sub2 = st.columns(2)
  with col_sub1:
    st.markdown(
        f"""
        <div class="cyber-card">
            <div class="cyber-icon">🔆</div>
            <h3>Radiación Solar</h3>
            <h2>{telemetria.get('radiacion_solar_W_m2', '--')} W/m²</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )
  with col_sub2:
    st.markdown(
        f"""
        <div class="cyber-card">
            <div class="cyber-icon">🧭</div>
            <h3>Vector Dirección</h3>
            <h2>{telemetria.get('direccion_viento_grados', '--')} °</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

  # ==========================================
  # 6. MOTOR DE ALERTAS Y LÓGICA TÁCTICA
  # ==========================================
  temp_val = telemetria.get("temperatura_C", 0)
  if temp_val and temp_val > 28:
    st.markdown(
        "🚨 **ALERTA TÁCTICA:** Umbral térmico superado (> 28°C). Protocolo de"
        " refrigeración activo."
    )
  elif temp_val and temp_val < 10:
    st.markdown(
        "❄️ **AVISO CLIMÁTICO:** Alerta de bajas temperaturas (< 10°C)."
    )

else:
  # Manejo de errores de enlace crítico
  st.error(
      "⚠️ **FALLO CRÍTICO DE ENLACE:** No se pudo establecer comunicación con"
      " la API central en Render."
  )
