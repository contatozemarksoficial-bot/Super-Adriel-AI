import streamlit as st
import random
import time

# 1. CONFIGURAÇÃO DE ELITE (Design Cinema Dark)
st.set_page_config(page_title="Adriel-AI Pro", layout="wide", initial_sidebar_state="expanded")

# --- SUA CHAVE MESTRE (LINK HOSTINGER) ---
CHAVE_MESTRE = "https://hostinger.com"

# 2. CSS MASTER LUXO V20 - PROTOCOLO "NÚCLEO ADRIEL"
st.markdown("""
<style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp, [data-testid="stSidebar"], [data-testid="stSidebarNav"] {
        background-color: #010409 !important;
    }
    [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
    
    .stButton>button {
        background-color: #0d1117 !important; color: #ffffff !important;
        border: 1px solid #1e293b !important; border-radius: 10px !important;
        height: 45px !important; width: 100% !important;
        font-weight: 700 !important; text-align: left !important;
        padding-left: 20px !important; text-transform: uppercase !important;
        font-size: 0.75rem !important; transition: 0.3s !important;
    }
    .stButton>button:hover {
        border-color: #00ffcc !important;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.3) !important;
        color: #00ffcc !important;
    }

    /* A CARA DO ROBÔ ADRIEL-AI PRO */
    .robot-canvas {
        display: flex; justify-content: center; align-items: center;
        padding: 50px 0; perspective: 1000px;
    }
    .robot-head {
        width: 200px; height: 180px;
        background: linear-gradient(145deg, #0d1117, #010409);
        border: 3px solid #00ffcc;
        border-radius: 60px 60px 30px 30px;
        position: relative;
        box-shadow: 0 0 80px rgba(0, 255, 204, 0.2), inset 0 0 30px rgba(0, 255, 204, 0.1);
        animation: floating 4s infinite ease-in-out;
    }
    .antenna {
        position: absolute; top: -30px; width: 4px; height: 35px;
        background: #00ffcc; box-shadow: 0 0 15px #00ffcc;
    }
    .antenna.left { left: 50px; transform: rotate(-15deg); }
    .antenna.right { right: 50px; transform: rotate(15deg); }
    
    .eye {
        width: 45px; height: 45px;
        background: radial-gradient(circle, #00ffcc 30%, #0088ff 100%);
        border-radius: 50%;
        position: absolute; top: 50px;
        box-shadow: 0 0 25px #00ffcc;
        animation: eyeBlink 5s infinite;
    }
    .eye.left { left: 40px; }
    .eye.right { right: 40px; }

    .processing-bar {
        position: absolute; bottom: 35px; left: 50%; transform: translateX(-50%);
        width: 80px; height: 4px; background: #1e293b; border-radius: 2px; overflow: hidden;
    }
    .processing-fill {
        width: 100%; height: 100%; background: #00ffcc;
        box-shadow: 0 0 10px #00ffcc; animation: sync 2s infinite linear;
    }

    @keyframes floating { 0%, 100% { transform: translateY(0) rotateX(5deg); } 50% { transform: translateY(-15px) rotateX(10deg); } }
    @keyframes eyeBlink { 0%, 92%, 100% { transform: scaleY(1); } 96% { transform: scaleY(0.1); } }
    @keyframes sync { 0% { transform: translateX(-100%); } 100% { transform: translateX(100%); } }

    .brand-title { 
        color: white; font-size: 3.5rem; font-weight: 900; 
        text-align: center; letter-spacing: -2px; margin-top: 20px;
    }
    
    /* BADGE CHAVE MESTRE */
    .master-key {
        background: rgba(0, 255, 204, 0.1);
        border: 1px solid #00ffcc;
        color: #00ffcc !important;
        padding: 10px 20px;
        border-radius: 8px;
        font-weight: 800;
        text-decoration: none !important;
        font-size: 0.8rem;
        transition: 0.4s;
    }
    .master-key:hover { background: #00ffcc; color: #010409 !important; box-shadow: 0 0 30px #00ffcc; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: NAVEGAÇÃO ---
with st.sidebar:
    st.markdown('<div style="color:white; font-size:1.6rem; font-weight:900; padding:15px;">🤖 Adriel-AI <span style="color:#00ffcc;">Pro</span></div>', unsafe_allow_html=True)
    
    # Navegação com nomes síncronos
    if st.button("🏠 DASHBOARD"): st.switch_page("app.py")
    if st.button("📡 1. RADAR ELITE"): st.switch_page("pages/1_Radar.py")
    if st.button("🕵️ 2. AUDITOR IA"): st.switch_page("pages/2_Auditor.py")
    if st.button("✍️ 3. GERADOR RSA"): st.switch_page("pages/3_Gerador.py")
    if st.button("🎯 4. CAÇADOR V10"): st.switch_page("pages/4_Cacador.py")
    if st.button("📐 6. ARQUITETO FUNIL"): st.switch_page("pages/6_Funil.py")
    if st.button("💎 5. ASSINANTES"): st.switch_page("pages/5_Assinantes.py")

# --- CONTEÚDO PRINCIPAL ---

# Dock de Plataformas com a CHAVE MESTRE
st.markdown(f"""
    <div style="display: flex; gap: 10px; margin-bottom: 30px;">
        <div style="flex:1; background:#0d1117; border:1px solid #1e293b; padding:12px; border-radius:8px; color:white; font-size:0.6rem; font-weight:800; text-align:center;">● CLICKBANK</div>
        <div style="flex:1; background:#0d1117; border:1px solid #1e293b; padding:12px; border-radius:8px; color:white; font-size:0.6rem; font-weight:800; text-align:center;">● BUYGOODS</div>
        <a href="{CHAVE_MESTRE}" target="_blank" style="flex:1; background:#0d1117; border:2px solid #00ffcc; padding:12px; border-radius:8px; color:#00ffcc; font-size:0.6rem; font-weight:800; text-align:center; text-decoration:none;">🔌 CONECTAR HOSTINGER (MESTRE)</a>
    </div>
""", unsafe_allow_html=True)

# A CARA DO ROBÔ ADRIEL-AI PRO
st.markdown("""
    <div class="robot-canvas">
        <div class="robot-head">
            <div class="antenna left"></div>
            <div class="antenna right"></div>
            <div class="eye left"></div>
            <div class="eye right"></div>
            <div class="processing-bar"><div class="processing-fill"></div></div>
        </div>
    </div>
    <div class="brand-title">Adriel-AI <span style="color:#00ffcc;">Pro</span></div>
    <p style="color:#94a3b8; font-size:1.3rem; font-weight:600; text-align:center; letter-spacing:1px; margin-top:-10px;">
        Sincronização de Inteligência Preditiva em Tempo Real
    </p>
""", unsafe_allow_html=True)

# RODAPÉ COM ACESSO RÁPIDO À CHAVE MESTRE
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
    <div style="text-align:center;">
        <a href="{CHAVE_MESTRE}" target="_blank" class="master-key">🛡️ ATIVAR INFRAESTRUTURA VIA HOSTINGER VPS</a>
    </div>
""", unsafe_allow_html=True)

# MÉTRICAS
st.markdown("<br><br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
c1.metric("MOTOR IA", "Ativo", "v20.2")
c2.metric("RASTREIOS", f"{random.randint(4500, 5200)}", "LIVE")
c3.metric("CHAVE MESTRE", "Vinculada", "PROTEGIDO")
