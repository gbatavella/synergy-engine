import streamlit as st
import time

# 1. Page Config - Anglo Market Wide Layout
st.set_page_config(page_title="Synergy AI | Autonomous Sales Engine", page_icon="🚀", layout="wide")

# 2. Premium Visual Architecture (Anglo Edition V2.4 + LIVE DEMO)
st.markdown("""
    <style>
    .stApp { background-color: #f0f4f8 !important; }
    h1, h2, h3, p, span, div { color: #0f172a; font-family: 'Inter', sans-serif; }
    
    .metric-box {
        background-color: #ffffff; padding: 30px; border-radius: 30px; 
        text-align: center; border: none; box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08);
        transition: transform 0.3s ease;
    }
    .metric-box:hover { transform: translateY(-8px); }
    
    .metric-title { 
        font-size: 52px; font-weight: 900; 
        background: linear-gradient(90deg, #ff007a 0%, #6366f1 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: -5px;
    }
    .metric-text { color: #475569 !important; font-size: 17px; font-weight: 700; }
    
    div[data-testid="stLinkButton"] > a {
        background: linear-gradient(90deg, #ff007a 0%, #ff007a 65%, #ff6a00 100%) !important;
        color: #ffffff !important; border-radius: 60px !important; border: none !important;
        font-size: 24px !important; font-weight: 900 !important; padding: 18px 0px !important;
        text-transform: uppercase; letter-spacing: 1px; box-shadow: 0 12px 30px rgba(255, 0, 122, 0.35) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important; text-decoration: none !important;
    }
    div[data-testid="stLinkButton"] > a:hover { transform: scale(1.04) !important; box-shadow: 0 18px 40px rgba(255, 0, 122, 0.5) !important; }

    .pricing-card {
        background-color: #ffffff; padding: 40px; border-radius: 35px; height: 100%;
        box-shadow: 0 25px 35px -10px rgba(0, 0, 0, 0.07); border: 1px solid #f1f5f9;
    }
    
    /* Live Demo Terminal Style */
    .terminal-box {
        background-color: #0b0f19; color: #00ff00; font-family: 'Courier New', monospace;
        padding: 20px; border-radius: 15px; border: 1px solid #1e293b; font-size: 14px;
    }
    .terminal-email { color: #a0aec0; }
    </style>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
st.write("")
st.markdown("<h1 style='text-align: center; font-size: 60px; margin-top: 15px;'>Your AI Sales Clone Working 24/7.</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #475569; font-weight: 400; margin-bottom: 45px;'>Automate lead extraction, psychological profiling, and deal closing on the open web. Zero code required.</h3>", unsafe_allow_html=True)

col_h1, col_h2, col_h3 = st.columns([1, 2, 1])
with col_h2:
    st.link_button("🔥 DEPLOY MY SWARM NOW", "https://batavella.gumroad.com/l/lccwzw", use_container_width=True)
    st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 15px; margin-top: 12px;'>Instant access after payment. 3-minute deployment setup.</p>", unsafe_allow_html=True)

st.write("")

# --- METRICS SECTION ---
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.markdown("<div class='metric-box'><div class='metric-title'>2.6x</div><div class='metric-text'>Better Conversion than Cold Email</div></div>", unsafe_allow_html=True)
with col_m2:
    st.markdown("<div class='metric-box'><div class='metric-title'>+10k</div><div class='metric-text'>Analyzed Prospects per Hour</div></div>", unsafe_allow_html=True)
with col_m3:
    st.markdown("<div class='metric-box'><div class='metric-title'>100%</div><div class='metric-text'>Operational Autonomy</div></div>", unsafe_allow_html=True)

st.divider()

# --- 🔴 LIVE DEMO (EL POLÍGONO DE TIRO) ---
st.markdown("<h2 style='text-align: center; font-size: 45px; color: #ff007a;'>🔴 LIVE DEMO: Test The Engine</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px; color: #475569; margin-bottom: 30px;'>Input a niche and watch Synergy extract, profile, and write a hyper-personalized email in seconds.</p>", unsafe_allow_html=True)

demo_col1, demo_col2, demo_col3 = st.columns([1, 2, 1])
with demo_col2:
    target_niche = st.text_input("", placeholder="e.g., 'Dentists in Texas' or 'SaaS Founders in London'")
    run_demo = st.button("▶️ RUN LIVE EXTRACTION", use_container_width=True)

if run_demo and target_niche:
    with st.container():
        st.write("")
        # Simulación de Progreso
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text("Initiating Swarm Infiltration...")
        time.sleep(1)
        progress_bar.progress(30)
        
        status_text.text(f"Bypassing geo-restrictions. Scraping targets for '{target_niche}'...")
        time.sleep(1.5)
        progress_bar.progress(60)
        
        status_text.text("Targets acquired. Executing Psychological Profiler...")
        time.sleep(1.5)
        progress_bar.progress(100)
        status_text.text("Operation Complete. Displaying Sample Output.")
        time.sleep(0.5)
        
        # Resultados de la Demo
        col_res1, col_res2 = st.columns(2)
        with col_res1:
            st.markdown("#### 🎯 Extracted & Profiled Leads")
            st.markdown(f"""
            <div class='terminal-box'>
            > Target 1: Dr. Sarah Jenkins<br>
            > Clinic: {target_niche.split(' ')[0]} Associates<br>
            > Est. Revenue: $1.2M - $2M<br>
            > Pain Point: Scaling patient acquisition cost.<br>
            > <strong>Status: High Liquidity. Ready for Outreach.</strong><br><br>
            
            > Target 2: Elite Care Clinic<br>
            > Location: Central District<br>
            > Pain Point: Outdated digital presence.<br>
            > <strong>Status: Medium Liquidity. Ready for Outreach.</strong>
            </div>
            """, unsafe_allow_html=True)
            
        with col_res2:
            st.markdown("#### ✉️ Autonomous AI Output (Ready to Send)")
            st.markdown(f"""
            <div class='terminal-box'>
            <span class='terminal-email'>
            <strong>Subject:</strong> Patient acquisition costs at {target_niche.split(' ')[0]} Associates<br><br>
            Hi Dr. Jenkins,<br><br>
            I noticed you're scaling operations in the area, but based on your current ad footprint, your patient acquisition cost might be higher than the local average.<br><br>
            We've built an autonomous system that drops targeted leads directly into clinics like yours without the overhead of ad spend.<br><br>
            Open to a quick 5-min demo this Thursday?<br><br>
            Best,<br>
            Your AI Sales Agent
            </span>
            </div>
            """, unsafe_allow_html=True)
            
        st.write("")
        st.error("⚠️ **DEMO LIMIT REACHED.** To extract 10,000+ leads without restrictions and operate completely autonomously, deploy your own Elite Swarm below.")

st.divider()

# --- ANGLO PRICING ---
st.markdown("<h2 style='text-align: center; font-size: 45px;'>Select Your Power Level</h2>", unsafe_allow_html=True)
st.write("")

col_p1, col_p2 = st.columns(2)

with col_p1:
    st.markdown("<div class='pricing-card' style='border-top: 10px solid #ff007a;'>", unsafe_allow_html=True)
    st.markdown("### 📦 SYNERGY PRO ENGINE")
    st.markdown("<h2 style='color: #0f172a; font-size: 42px;'>$497 USD</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #475569;'>The autonomous base engine for agencies and entrepreneurs demanding immediate scale.</p>", unsafe_allow_html=True)
    st.write("✔️ Swarm Extraction Engine")
    st.write("✔️ Base Psychological Profiler")
    st.write("✔️ Deployment & Evasion Manuals")
    st.write("✔️ VIP Engineering Support (12h)")
    st.write("")
    st.link_button("🚀 GET STANDARD LICENSE", "https://batavella.gumroad.com/l/lccwzw", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_p2:
    st.markdown("<div class='pricing-card' style='border-top: 10px solid #6366f1;'>", unsafe_allow_html=True)
    st.markdown("### 💎 SYNERGY ELITE SWARM")
    st.markdown("<h2 style='color: #0f172a; font-size: 42px;'>$997 USD</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #475569;'>Full infrastructure with remote Telegram control for high-volume operations.</p>", unsafe_allow_html=True)
    st.write("✔️ Full Remote Telegram Command")
    st.write("✔️ Advanced Multi-Agent Library")
    st.write("✔️ Custom Server Calibration")
    st.write("✔️ Strategic 1-on-1 Consultation")
    st.write("")
    st.link_button("⚡ UNLOCK ELITE SWARM", "https://batavella.gumroad.com/l/gwesub", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
st.divider()
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 14px;'>Synergy Humans & Agents AI | 2026 | Sovereign Digital Operations</p>", unsafe_allow_html=True)
