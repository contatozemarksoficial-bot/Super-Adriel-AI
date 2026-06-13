import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. CONFIGURAÇÃO DA INTERFACE
st.set_page_config(page_title="Adriel-AI Pro", layout="wide", initial_sidebar_state="collapsed")

# 2. INJEÇÃO DE CSS BLACK-LABEL (Otimizado para o seu estilo)
st.markdown("""
<style>
    .stApp { background-color: #060913 !important; color: #f8fafc !important; }
    [data-testid="stHeader"] { display: none !important; }
    .block-container { padding-top: 2rem !important; max-width: 100% !important; }
    
    /* Botões Neon */
    div.stLinkButton > a, .stButton > button {
        background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important; color: #030712 !important;
        font-weight: 900 !important; border-radius: 30px !important; border: none !important; width: 100% !important;
    }
    
    /* Métricas Premium */
    [data-testid="stMetricContainer"] {
        background: #0f172a !important; border: 1px solid #1e293b !important;
        border-bottom: 3px solid #00ffcc !important; border-radius: 12px !important; padding: 20px !important;
    }
    
    .terminal-hacker { 
        background-color: #040814 !important; border: 1px solid #00ffcc !important; 
        padding: 15px; border-radius: 10px; font-family: monospace; color: #00ffcc; font-size: 12px;
    }
</style>
""", unsafe_allow_html=True)

# Inicialização de sessão
if "plano_usuario" not in st.session_state: 
    st.session_state.plano_usuario = None

# 3. LÓGICA DE ACESSO (TELA DE BLOQUEIO)
if st.session_state.plano_usuario is None:
    st.markdown('<h2 style="text-align:center;">🤖 ADRIEL-AI <span style="background:#ff0055; padding:5px; border-radius:5px;">LOCK</span></h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.info("Insira seu token para liberar as funções robóticas.")
        chave = st.text_input("Token de Licença:", type="password", placeholder="Ex: PRO-97")
        if st.button("🔓 ACESSAR SOFTWARE"):
            if chave in ["START-47", "PRO-97", "ELITE-197"]:
                st.session_state.plano_usuario = chave.split("-")[0]
                st.success(f"Acesso liberado: Nível {st.session_state.plano_usuario}")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Token Inválido!")
    st.stop()

# 4. DASHBOARD PÓS-LOGIN (O QUE ACONTECE DEPOIS QUE FUNCIONA)
plano = st.session_state.plano_usuario

# Cabeçalho de Status
c1, c2 = st.columns([3, 1])
with c1:
    st.title(f"🚀 Dashboard {plano}")
with c2:
    if st.button("🔴 SAIR"):
        st.session_state.plano_usuario = None
        st.rerun()

# Espaço de Ferramentas Baseado no Plano
st.write("---")
col_m1, col_m2, col_m3, col_m4 = st.columns(4)

with col_m1: st.metric("Afiliados Ativos", "1,284", "+12%")
with col_m2: st.metric("ROI Médio", "4.8x", "+0.3")
with col_m3: st.metric("Vendas Hoje", "R$ 12.450", "+8%")
with col_m4: st.metric("Bots Operando", "24/24", "Online")

# Restrição de Funcionalidades
st.subheader("🛠️ Ferramentas Disponíveis")

if plano == "START":
    st.warning("Seu plano START permite apenas Extração Básica. Faça upgrade para o PRO para Automação.")
    st.button("Extrair Leads Atuais")
    
elif plano == "PRO":
    col_pro1, col_pro2 = st.columns(2)
    with col_pro1:
        st.markdown('<div class="terminal-hacker"><b>Buscando novos funis...</b><br>> API Conectada<br>> Status: Operacional</div>', unsafe_allow_html=True)
    with col_pro2:
        st.button("Disparar Campanhas Automáticas")

elif plano == "ELITE":
    st.markdown('<h3 style="color:#00ffcc;">👑 COMANDOS DE ELITE LIBERADOS</h3>', unsafe_allow_html=True)
    tabs = st.tabs(["IA Generativa", "Escala Global", "Relatórios Black"])
    with tabs[0]:
        st.write("Criação de anúncios com IA habilitada.")
    with tabs[1]:
        st.write("Integração com 50+ plataformas liberada.")
