import streamlit as st
import pandas as pd

# Configuración de Élite (Mantiene la página ancha y profesional)
st.set_page_config(page_title="Synergy AI | RaaS Elite Sales Engine", page_icon="🚀", layout="wide")

# CSS Minimalista: Solo tocamos el botón y el brillo de la marca
st.markdown("""
    <style>
    /* Botón High-Ticket: Elegante y moderno */
    div.stButton > button {
        background: linear-gradient(135deg, #FF416C 0%, #FF4B2B 100%);
        color: white;
        border-radius: 8px;
        border: none;
        box-shadow: 0 4px 14px 0 rgba(255, 75, 43, 0.39);
        padding: 0.75rem 2rem;
        font-weight: 600;
        letter-spacing: 1px;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px 0 rgba(255, 75, 43, 0.6);
    }
    /* Texto brillante para RaaS */
    .elite-text {
        color: #FF4B2B;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("Your AI Sales Clone Works 24/7")
st.markdown("### The First <span class='elite-text'>RaaS (Robots as a Service)</span> for High-Ticket Sales", unsafe_allow_html=True)

st.write("---")

st.markdown("""
**Stop buying static tools that break.** Subscribe to the **Swarm Evolution Protocol (SEP)**. Our agents adapt weekly to the changing web, ensuring your sales machine never stops, regardless of platform updates or anti-bot defenses.
""")

st.button("🔥 DEPLOY MY SWARM NOW")
st.caption("Instant access after payment. 3-minute deployment setup.")

st.write("---")

# --- FEATURES (Usando st.metric para un look de Dashboard Profesional) ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Conversion vs Cold Email", value="2.6x")
with col2:
    st.metric(label="Analyzed Prospects per Hour", value="+10k")
with col3:
    st.metric(label="Operational Autonomy", value="100%")

st.write("---")

# --- THE 90-DAY EDGE ---
st.subheader("🛡️ The 90-Day Evolution Guarantee")
st.info("**Zero Friction. Zero Downtime.** Your subscription includes **90 days of full Evolution Support**. If the web changes, our 'Sentinel' agents deploy a patch to your system within 24 hours. Your business stays operational while the world adapts.")

st.write("---")

# --- LIVE DEMO ---
st.subheader("🔴 LIVE DEMO: Test The Engine")
st.write("Input a niche and watch Synergy extract, profile, and write a hyper-personalized email in seconds.")

niche = st.text_input("Target Niche:", placeholder="e.g., 'Dentists in Austin' or 'SaaS Founders in London'")

if st.button("▶️ RUN LIVE EXTRACTION"):
    if niche:
        with st.spinner(f"Swarm deployed to {niche}... Extracting intelligence..."):
            import time
            time.sleep(2)
            st.success(f"Target Acquired: 15 High-Value Leads found in {niche}.")
            st.code(f"Analyzing psychological profile for {niche} owners...\nGenerating Swarm Evolution pitch...")
    else:
        st.warning("Please enter a target niche.")

st.write("---")

# --- PRICING ---
st.subheader("Choose Your Battle Fleet")
p1, p2 = st.columns(2)

with p1:
    st.markdown("### PRO ENGINE")
    st.markdown("## $497")
    st.markdown("""
    * **5 Autonomous Extraction Agents**
    * Engine Evolution Protocol (90 days)
    * Standard Lead Profiling
    """)

with p2:
    st.markdown("### ELITE SWARM")
    st.markdown("## $997")
    st.markdown("""
    * **20 Autonomous Agents + Manager**
    * **Lifetime Evolution Protocol Access**
    * Advanced Psychological Profiling
    * Direct WhatsApp/Telegram Integration
    """)
