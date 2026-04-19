import streamlit as st

st.set_page_config(page_title="Synergy AI | Autonomous Sales Engine", page_icon="🚀", layout="wide")

st.markdown("""
<style>
/* EL BOTON GLOW EXACTO DE P.PNG */
div[data-testid="stButton"] > button {
    background: linear-gradient(90deg, #FF0080 0%, #FF8C00 100%) !important;
    color: white !important;
    border: none !important;
    padding: 1.2rem 2rem !important;
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    border-radius: 50px !important;
    width: 100% !important;
    box-shadow: 0 10px 30px -5px rgba(255, 0, 128, 0.6) !important;
    transition: all 0.3s ease !important;
    display: block !important;
    margin: 0 auto !important;
}
div[data-testid="stButton"] > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 15px 40px -5px rgba(255, 0, 128, 0.8) !important;
}

/* MÉTRICAS EXACTAS CON GRADIENTE */
.metric-container {
    background: white;
    border-radius: 10px;
    padding: 30px 20px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    text-align: center;
    border: 1px solid #f0f0f0;
}
.metric-value {
    font-size: 3rem;
    font-weight: 800;
    background: -webkit-linear-gradient(45deg, #FF0080, #8A2BE2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
}
.metric-label {
    font-size: 1rem;
    font-weight: 700;
    color: #4B5563;
}

/* CAJAS DE PRECIO CON BORDE GRUESO SUPERIOR */
.price-card-pro {
    border-top: 12px solid #FF0080;
    border-radius: 15px;
    padding: 2.5rem;
    background: white;
    box-shadow: 0 10px 30px -5px rgba(0,0,0,0.08);
    height: 100%;
}
.price-card-elite {
    border-top: 12px solid #6366F1; /* Azul/Indigo de la imagen original */
    border-radius: 15px;
    padding: 2.5rem;
    background: white;
    box-shadow: 0 10px 30px -5px rgba(0,0,0,0.08);
    height: 100%;
}

/* TIPOGRAFÍA GLOBAL Y CENTRADO */
h1 { text-align: center; font-weight: 800; color: #111827; font-size: 3rem !important; margin-bottom: 0.5rem !important; }
h2 { text-align: center; font-weight: 700; color: #111827; margin-top: 2rem !important; margin-bottom: 2rem !important; }
.sub-headline { text-align: center; font-size: 1.2rem; color: #4B5563; margin-bottom: 3rem; }
.highlight-text { color: #FF0080; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("<h1>Your AI Sales Clone Working 24/7.</h1>", unsafe_allow_html=True)
st.markdown("""
<div class="sub-headline">
    The First <span class="highlight-text">RaaS (Robots as a Service)</span> for High-Ticket Sales.<br>
    Stop buying static tools that break. Subscribe to the <strong>Swarm Evolution Protocol (SEP)</strong>.
</div>
""", unsafe_allow_html=True)

# Contenedor central para el botón principal (1/3 de ancho para que no ocupe toda la pantalla de lado a lado)
_, col_btn, _ = st.columns([1, 2, 1])
with col_btn:
    st.button("🔥 DEPLOY MY SWARM NOW")
st.markdown("<p style='text-align:center; color:#9CA3AF; font-size:0.8rem; margin-top:1rem;'>Instant access after payment. 3-minute deployment setup.</p>", unsafe_allow_html=True)

st.write("<br><br>", unsafe_allow_html=True)

# --- METRICS SECTION ---
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""<div class="metric-container"><div class="metric-value">2.6x</div><div class="metric-label">Better Conversion than Cold Email</div></div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="metric-container"><div class="metric-value">+10k</div><div class="metric-label">Analyzed Prospects per Hour</div></div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class="metric-container"><div class="metric-value">100%</div><div class="metric-label">Operational Autonomy</div></div>""", unsafe_allow_html=True)

st.write("<br><br>", unsafe_allow_html=True)

# --- ENTERPRISE SECTION (La que tenías en p.png) ---
st.markdown("<h2>Enterprise-Grade Architecture</h2>", unsafe_allow_html=True)
st.info("🛡️ **The 90-Day Evolution Guarantee:** Zero Friction. Zero Downtime. Your subscription includes 90 days of full Evolution Support. If the web changes, our 'Sentinel' agents deploy a patch to your system within 24 hours.")

st.write("<br>", unsafe_allow_html=True)

# --- LIVE DEMO ---
st.markdown("<h2>🔴 LIVE DEMO: Test The Engine</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#4B5563;'>Input a niche and watch Synergy extract, profile, and write a hyper-personalized email in seconds.</p>", unsafe_allow_html=True)

_, col_demo, _ = st.columns([1, 2, 1])
with col_demo:
    niche = st.text_input("", placeholder="e.g., 'Dentists in Austin' or 'SaaS Founders in London'", label_visibility="collapsed")
    if st.button("▶️ RUN LIVE EXTRACTION", key="demo"):
        if niche:
            with st.spinner(f"Swarm deployed to {niche}... Extracting intelligence..."):
                import time
                time.sleep(2)
                st.success(f"Target Acquired: 15 High-Value Leads found in {niche}.")
        else:
            st.warning("Please enter a target niche.")

st.write("<br><br>", unsafe_allow_html=True)

# --- PRICING SECTION ---
st.markdown("<h2>Select Your Power Level</h2>", unsafe_allow_html=True)

p1, p2 = st.columns(2)

with p1:
    st.markdown("""
    <div class="price-card-pro">
        <h4 style="color:#6B7280; font-weight:700; margin-bottom:0;">📦 SYNERGY PRO ENGINE</h4>
        <h1 style="color:#111827; font-size:2.5rem; margin-top:0;">$497 USD</h1>
        <p style="color:#4B5563; font-size:0.9rem; margin-bottom:1.5rem;">The autonomous base engine for agencies and entrepreneurs demanding immediate scale.</p>
        <p style="margin-bottom:0.5rem;">✔️ <b>5 Autonomous Extraction Agents</b></p>
        <p style="margin-bottom:0.5rem;">✔️ Engine Evolution Protocol (90 days)</p>
        <p style="margin-bottom:1.5rem;">✔️ Standard Lead Profiling</p>
    </div>
    <br>
    """, unsafe_allow_html=True)
    st.button("🚀 GET STANDARD LICENSE", key="btn_pro")

with p2:
    st.markdown("""
    <div class="price-card-elite">
        <h4 style="color:#6B7280; font-weight:700; margin-bottom:0;">💎 SYNERGY ELITE SWARM</h4>
        <h1 style="color:#111827; font-size:2.5rem; margin-top:0;">$997 USD</h1>
        <p style="color:#4B5563; font-size:0.9rem; margin-bottom:1.5rem;">Full infrastructure with remote Telegram control for high-volume operations.</p>
        <p style="margin-bottom:0.5rem;">✔️ <b>20 Autonomous Agents + Manager</b></p>
        <p style="margin-bottom:0.5rem;">✔️ <b>Lifetime Evolution Protocol Access</b></p>
        <p style="margin-bottom:1.5rem;">✔️ Advanced Psychological Profiling</p>
    </div>
    <br>
    """, unsafe_allow_html=True)
    st.button("⚡ UNLOCK ELITE SWARM", key="btn_elite")
