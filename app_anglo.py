import streamlit as st

# Configuración
st.set_page_config(page_title="Synergy AI | Autonomous Sales Engine", page_icon="🚀", layout="wide")

# CSS Original Restaurado
st.markdown("""
<style>
/* Botón Principal */
.stButton>button {
    background: linear-gradient(90deg, #FF007F 0%, #FF5E00 100%) !important;
    color: white !important;
    border-radius: 30px !important;
    border: none !important;
    padding: 15px 30px !important;
    font-weight: bold !important;
    width: 100% !important;
    transition: 0.3s !important;
}
.stButton>button:hover {
    transform: scale(1.02) !important;
    box-shadow: 0px 5px 15px rgba(255, 94, 0, 0.4) !important;
}

/* Tarjetas de Métricas Redondeadas */
.metric-card {
    background-color: white;
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}
.metric-value {
    font-size: 2.5rem;
    font-weight: bold;
    background: -webkit-linear-gradient(45deg, #FF007F, #8A2BE2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 5px;
}
.metric-label {
    font-size: 0.9rem;
    color: #555;
    font-weight: 600;
}

/* Tarjetas de Precio */
.pricing-card-pro {
    background-color: white;
    border-radius: 15px;
    padding: 30px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    border-top: 8px solid #FF007F;
}
.pricing-card-elite {
    background-color: white;
    border-radius: 15px;
    padding: 30px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    border-top: 8px solid #6495ED;
}
h1, h2, h3 { text-align: center; color: #222; }
.sub-header { text-align: center; color: #666; font-size: 1.1rem; margin-bottom: 30px; }
</style>
""", unsafe_allow_html=True)

# --- CABECERA ---
st.markdown("<h1>Your AI Sales Clone Working 24/7.</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>The First <b>RaaS (Robots as a Service)</b> for High-Ticket Sales.<br>Stop buying static tools that break. Subscribe to the <b>Swarm Evolution Protocol (SEP)</b>.</p>", unsafe_allow_html=True)

st.button("🔥 DEPLOY MY SWARM NOW")
st.markdown("<p style='text-align:center; color:#888; font-size:12px;'>Instant access after payment. 3-minute deployment setup.</p>", unsafe_allow_html=True)

st.write("---")

# --- MÉTRICAS ---
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='metric-card'><div class='metric-value'>2.6x</div><div class='metric-label'>Better Conversion than Cold Email</div></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='metric-card'><div class='metric-value'>+10k</div><div class='metric-label'>Analyzed Prospects per Hour</div></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='metric-card'><div class='metric-value'>100%</div><div class='metric-label'>Operational Autonomy</div></div>", unsafe_allow_html=True)

# --- GARANTÍA ---
st.markdown("<h2>The 90-Day Evolution Guarantee</h2>", unsafe_allow_html=True)
st.info("**Zero Friction. Zero Downtime.** Your subscription includes 90 days of full Evolution Support. If the web changes, our 'Sentinel' agents deploy a patch to your system within 24 hours.")

st.write("---")

# --- DEMO ---
st.markdown("<h2>🔴 LIVE DEMO: Test The Engine</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#666;'>Input a niche and watch Synergy extract, profile, and write a hyper-personalized email in seconds.</p>", unsafe_allow_html=True)

niche = st.text_input("", placeholder="e.g., 'Dentists in Austin' or 'SaaS Founders in London'")
if st.button("▶️ RUN LIVE EXTRACTION"):
    if niche:
        with st.spinner(f"Swarm deployed to {niche}... Extracting intelligence..."):
            import time
            time.sleep(2)
            st.success(f"Target Acquired: 15 High-Value Leads found in {niche}.")
    else:
        st.warning("Please enter a target niche.")

st.write("---")

# --- PRECIOS ---
st.markdown("<h2>Select Your Power Level</h2>", unsafe_allow_html=True)
p1, p2 = st.columns(2)

with p1:
    st.markdown("""
    <div class='pricing-card-pro'>
        <h3 style='text-align:left; color:#FF007F;'>📦 SYNERGY PRO ENGINE</h3>
        <h1 style='text-align:left; margin-top:0;'>$497 USD</h1>
        <p style='color:#666; font-size:14px;'>The autonomous base engine for agencies.</p>
        <p>✔️ <b>5 Autonomous Extraction Agents</b></p>
        <p>✔️ Engine Evolution Protocol (90 days)</p>
        <p>✔️ Standard Lead Profiling</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("🚀 GET STANDARD LICENSE", key="pro")

with p2:
    st.markdown("""
    <div class='pricing-card-elite'>
        <h3 style='text-align:left; color:#6495ED;'>💎 SYNERGY ELITE SWARM</h3>
        <h1 style='text-align:left; margin-top:0;'>$997 USD</h1>
        <p style='color:#666; font-size:14px;'>Full infrastructure for high-volume operations.</p>
        <p>✔️ <b>20 Autonomous Agents + Manager</b></p>
        <p>✔️ <b>Lifetime Evolution Protocol Access</b></p>
        <p>✔️ Advanced Psychological Profiling</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("⚡ UNLOCK ELITE SWARM", key="elite")
