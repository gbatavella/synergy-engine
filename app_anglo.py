import streamlit as st
import pandas as pd

# Configuración de Élite
st.set_page_config(page_title="Synergy AI | RaaS Elite Sales Engine", page_icon="🚀", layout="wide")

# CSS AGRESIVO - Forzando el Modo Oscuro y Estilos High-Ticket
st.markdown("""
    <style>
    /* Forzar fondo oscuro en toda la aplicación */
    .stApp {
        background-color: #0e1117 !important;
    }
    
    /* Forzar texto blanco para contrastar */
    html, body, [class*="css"], h1, h2, h3, h4, h5, h6, p, span {
        color: #ffffff !important;
    }
    
    /* Botones nucleares (Gradiente Naranja/Fuego) */
    .stButton>button {
        background: linear-gradient(45deg, #ff4b1f, #ff9068) !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 15px 30px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        width: 100% !important;
        box-shadow: 0 4px 15px rgba(255, 75, 31, 0.3) !important;
        transition: 0.3s !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(255, 75, 31, 0.6) !important;
    }
    
    /* Resaltado de palabras clave */
    .highlight {
        color: #ff4b1f !important;
        font-weight: 900 !important;
        text-shadow: 0px 0px 10px rgba(255,75,31,0.5);
    }
    
    /* Cajas de alerta estilizadas */
    div[data-testid="stInfo"] {
        background-color: rgba(255, 75, 31, 0.05) !important;
        border-left: 4px solid #ff4b1f !important;
        color: white !important;
    }
    
    /* Separadores sutiles */
    hr {
        border-color: #2b303b !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER RaaS ---
st.markdown("<br>", unsafe_allow_html=True) # Espacio inicial
st.title("Your AI Sales Clone Works 24/7")
st.markdown("## The First <span class='highlight'>RaaS</span> (Robots as a Service) for High-Ticket Sales", unsafe_allow_html=True)

st.markdown("""
### Stop buying static tools that break. 
Subscribe to the **Swarm Evolution Protocol (SEP)**. Our agents adapt weekly to the changing web, 
ensuring your sales machine never stops, regardless of platform updates or anti-bot defenses.
""")

st.markdown("<br>", unsafe_allow_html=True)
st.button("🔥 DEPLOY MY SWARM NOW")
st.caption("Instant access after payment. 3-minute deployment setup.")
st.markdown("<br>", unsafe_allow_html=True)

# --- FEATURES ---
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<h2 style='color:#ff4b1f !important;'>2.6x</h2>", unsafe_allow_html=True)
    st.write("**Better Conversion than Cold Email**")
with col2:
    st.markdown("<h2 style='color:#ff4b1f !important;'>+10k</h2>", unsafe_allow_html=True)
    st.write("**Analyzed Prospects per Hour**")
with col3:
    st.markdown("<h2 style='color:#ff4b1f !important;'>100%</h2>", unsafe_allow_html=True)
    st.write("**Operational Autonomy**")

st.divider()

# --- THE 90-DAY EDGE ---
st.subheader("🛡️ The 90-Day Evolution Guarantee")
st.info("""
**Zero Friction. Zero Downtime.** Your subscription includes **90 days of full Evolution Support**. 
If the web changes, our 'Sentinel' agents deploy a patch to your system within 24 hours. 
Your business stays operational while the world adapts.
""")

st.divider()

# --- LIVE DEMO (POLÍGONO DE TIRO) ---
st.subheader("🔴 LIVE DEMO: Test The Engine")
niche = st.text_input("Input a niche and watch Synergy extract, profile, and write a hyper-personalized email in seconds.", placeholder="e.g., 'Dentists in Austin' or 'SaaS Founders in London'")

if st.button("▶️ RUN LIVE EXTRACTION"):
    if niche:
        with st.spinner(f"Swarm deployed to {niche}... Extracting intelligence..."):
            import time
            time.sleep(2)
            st.success(f"Target Acquired: 15 High-Value Leads found in {niche}.")
            st.code(f"Analizing psychological profile for {niche} owners...\nGenerating Swarm Evolution pitch...")
    else:
        st.warning("Please enter a target niche.")

st.divider()

# --- PRICING RaaS ---
st.subheader("Choose Your Battle Fleet")
p1, p2 = st.columns(2)
with p1:
    st.write("### PRO ENGINE")
    st.markdown("<h2 class='highlight'>$497</h2>", unsafe_allow_html=True)
    st.write("- 5 Autonomous Extraction Agents")
    st.write("- Engine Evolution Protocol (90 days)")
    st.write("- Standard Lead Profiling")
with p2:
    st.write("### ELITE SWARM")
    st.markdown("<h2 class='highlight'>$997</h2>", unsafe_allow_html=True)
    st.write("- 20 Autonomous Agents + Manager")
    st.write("- **Lifetime Evolution Protocol Access**")
    st.write("- Advanced Psychological Profiling")
    st.write("- Direct WhatsApp/Telegram Integration")
