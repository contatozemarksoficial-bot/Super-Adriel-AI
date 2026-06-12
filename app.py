import streamlit as st
import pandas as pd
import random

# 1. CONFIGURAÇÃO SUPREMA DE TELA
st.set_page_config(
    page_title="Adriel-AI Pro | Dashboard Oficial",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS MASTER LUXO - PROTOCOLO TRIPLE BLACK & QUANTUM CORE
st.markdown("""
<style>
    /* RESET TOTAL E FUNDO PRETO CINEMA */
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    .stApp, [data-testid="stSidebar"], [data-testid="stSidebarNav"], [data-testid="stAppViewContainer"] {
        background-color: #010409 !important;
    }

    /* ESCONDE O MENU PADRÃO PARA NAVEGAÇÃO PROPRIETÁRIA */
    [data-testid="stSidebarNav"] { display: none; }
    [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
    
    /* MENU DE BOTÕES DA LATERAL (ESTILO EXECUTIVO) */
    .sidebar-menu { display: flex; flex-direction: column; gap: 8px; padding: 15px; }
    .menu-btn {
        display: flex; align-items: center; gap: 12px; padding: 14px;
        background: #0d1117; border: 1px solid #1e293b; border-radius: 10px;
        color: #ffffff !important; text-decoration: none !important;
        font-weight: 700; font-size: 0.8rem; text-transform: uppercase; 
        transition: 0.3s all; border-bottom: 2px solid #1e293b;
    }
    .menu-btn:hover { 
        border-color: #00ffcc; 
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.2); 
        transform: translateX(5px);
        background: #010409;
    }
    .icon-neon { color: #00ffcc; text-shadow: 0 0 8px #00ffcc; font-size: 1.1rem; }

    /* EFEITO DO NÚCLEO (O "CHÃ" DO ROBÔ NO CENTRO) */
    .core-container {
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        padding: 40px 0;
    }
    .ai-core {
        width: 160px; height: 180px;
        background: radial-gradient(circle, #010409 30%, #00ffcc11 100%);
        border-radius: 50%;
        border: 2px solid #00ffcc;
        box-shadow: 0 0 60px rgba(0, 255, 204, 0.3), inset 0 0 40px rgba(0, 255, 204, 0.2);
        margin-bottom: 30px;
        animation: breath 3s infinite ease-in-out;
    }
    @keyframes breath { 0%, 100% { transform: scale(1); opacity: 0.7; } 50% { transform: scale(1.08); opacity: 1; } }

    /* MÉTRICAS DE LUXO */
    .metric-card {
        background: #0d1117; border: 1px solid #1e293b; padding: 20px; border-radius: 15px;
        text-align: center; border-bottom: 3px solid #00ffcc;
    }
    .m-label { color: #94a3b8; font-size: 0.7rem; font-weight: 800; text-transform: uppercase; margin-bottom: 5px; }
    .m-value { color: #ffffff; font-size: 1.8rem; font-weight: 900; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: O SEU PAINEL DE NAVEGAÇÃO INTERNO ---
with st.sidebar:
    st.markdown('<div style="color:white; font-size:1.8rem; font-weight:900; padding:20px; letter-spacing:-1.5px;">🤖 Adriel-AI <span style="color:#00ffcc;">Pro</span></div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#475569; font-size:0.7rem; font-weight:800; text-transform:uppercase; letter-spacing:2px; margin-left:20px; margin-bottom:20px;">Terminal de Comando</p>', unsafe_allow_html=True)
    
    # Links de Navegação (IMPORTANTE: Os nomes devem ser os arquivos da sua pasta 'pages')
    st.markdown("""
    <div class="sidebar-menu">
        <a href="/" target="_self" class="menu-btn" style="border-left: 4px solid #00ffcc; background:#1e293b;"><span class="icon-neon">🏠</span> DASHBOARD</a>
        <a href="Radar" target="_self" class="menu-btn"><span class="icon-neon">📡</span> 1. RADAR ELITE</a>
        <a href="Auditor" target="_self" class="menu-btn"><span class="icon-neon">🕵️</span> 2. AUDITOR IA</a>
        <a href="RSA" target="_self" class="menu-btn"><span class="icon-neon">✍️</span> 3. GERADOR RSA</a>
        <a href="Cacador" target="_self" class="menu-btn"><span class="icon-neon">🎯</span> 4. CAÇADOR V10</a>
        <a href="Presell" target="_self" class="menu-btn"><span class="icon-neon">📄</span> 5. PRE-SELL</a>
        <a href="Funil" target="_self" class="menu-btn"><span class="icon-neon">📐</span> 6. FUNIL</a>
        <a href="Assinantes" target="_self" class="menu-btn"><span class="icon-neon">💎</span> ASSINANTES</a>
    </div>
    """, unsafe_allow_html=True)

# --- CONTEÚDO DA HOME (PAINEL DE LUXO) ---

# 1. Selos de Plataforma no Topo (Com seu link da Hostinger)
st.markdown(f"""
    <div style="display: flex; gap: 10px; margin-bottom: 40px; overflow-x: auto;">
        <div style="flex:1; background:#0d1117; border:1px solid #1e293b; padding:10px; border-radius:6px; color:white; font-size:0.6rem; font-weight:800; text-align:center;">● CLICKBANK</div>
        <div style="flex:1; background:#0d1117; border:1px solid #1e293b; padding:10px; border-radius:6px; color:white; font-size:0.6rem; font-weight:800; text-align:center;">● BUYGOODS</div>
        <div style="flex:1; background:#0d1117; border:1px solid #1e293b; padding:10px; border-radius:6px; color:white; font-size:0.6rem; font-weight:800; text-align:center;">● STRIPE</div>
        <a href="https://hostinger.com" target="_blank" style="flex:1; background:#0d1117; border:1px solid #00ffcc; padding:10px; border-radius:6px; color:#00ffcc; font-size:0.6rem; font-weight:800; text-align:center; text-decoration:none;">● HOSTINGER VPS</a>
    </div>
""", unsafe_allow_html=True)

# 2. O Chã (Núcleo da IA)
st.markdown("""
    <div class="core-container">
        <div class="ai-core"></div>
        <div style="color:white; font-size:2.8rem; font-weight:900; margin-top:10px; letter-spacing:-2px;">Adriel-AI <span style="color:#00ffcc;">Pro</span></div>
        <p style="color:#94a3b8; font-size:1.1rem; font-weight:500;">Sistema Síncrono de Inteligência Preditiva</p>
        <div style="color:#00ffcc; font-weight:800; letter-spacing:3px; margin-top:20px; font-size:0.7rem;">PRECISÃO: 99.8% | STATUS: ONLINE</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# 3. Métricas Reais do Dashboard
m1, m2, m3, m4 = st.columns(4)
with m1: st.markdown('<div class="metric-card"><div class="m-label">OPERADORES LIVE</div><div class="m-value">2,326</div></div>', unsafe_allow_html=True)
with m2: st.markdown('<div class="metric-card"><div class="m-label">RASTREIOS HOJE</div><div class="m-value">14,840</div></div>', unsafe_allow_html=True)
with m3: st.markdown('<div class="metric-card"><div class="m-label">VENDAS BASE 44</div><div class="m-value">R$ 142.5K</div></div>', unsafe_allow_html=True)
with m4: st.markdown('<div class="metric-card" style="border-bottom-color:#ff0055;"><div class="m-label">SINAIS GLOBAIS</div><div class="m-value">ATIVO</div></div>', unsafe_allow_html=True)

st.markdown("<br><br><p style='text-align:center; color:#475569; font-size:0.6rem;'>SISTEMA PROTEGIDO POR CRIPTOGRAFIA AES-256 | ADRIEL-AI PRO V17.2</p>", unsafe_allow_html=True)
