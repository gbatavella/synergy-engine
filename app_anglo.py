import streamlit as st
import pandas as pd

# Configuración de Élite
st.set_page_config(page_title="Synergy AI | RaaS Elite Sales Engine", page_icon="🚀", layout="wide")

# Estilo Swarm Dark
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button {
        background: linear-gradient(45deg, #ff4b1f, #ff9068);
        color: white; border-radius: 20px; border: none;
        padding: 15px 30px; font-weight: bold; width: 100%;
    }
    .highlight { color: #ff4b1f; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER RaaS ---
st.title("Your AI Sales Clone Works 24/7")
st.header("The First <span class='highlight'>RaaS</span> (Robots as a Service) for High-Ticket Sales", unsafe_allow_html=True)

st.markdown("""
### Stop buying static tools that break. 
Subscribe to the **Swarm Evolution Protocol (SEP)**. Our agents adapt weekly to the changing web, 
ensuring your sales machine never stops, regardless of platform updates or anti-bot defenses.
""")

st.button("🔥 DEPLOY MY SWARM NOW")
st.caption("Instant access after payment. 3-minute deployment setup.")

# --- FEATURES ---
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("2.6x")
    st.write("Better Conversion than Cold Email")
with col2:
    st.subheader("+10k")
    st.write("Analyzed Prospects per Hour")
with col3:
    st.subheader("100%")
    st.write("Operational Autonomy")

st.divider()

# --- THE 90-DAY EDGE ---
st.subheader("🛡️ The 90-Day Evolution Guarantee")
st.info("""
**Zero Friction. Zero Downtime.** Your subscription includes **90 days of full Evolution Support**. 
If the web changes, our 'Sentinel' agents deploy a patch to your system within 24 hours. 
Your business stays operational while the world adapts.
""")

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
    st.write("### PRO SWARM")
    st.write("## $497")
    st.write("- 5 Autonomous Extraction Agents")
    st.write("- Swarm Evolution Protocol (90 days)")
    st.write("- Standard Lead Profiling")
with p2:
    st.write("### ELITE SWARM")
    st.write("## $997")
    st.write("- 20 Autonomous Agents + Manager")
    st.write("- **Lifetime Evolution Protocol Access**")
    st.write("- Advanced Psychological Profiling")
    st.write("- Direct WhatsApp/Telegram Integration")
