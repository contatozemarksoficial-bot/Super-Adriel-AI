import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE
st.set_page_config(page_title="Adriel-AI Elite v7", layout="wide", initial_sidebar_state="collapsed")

# 2. ESTADO DA SESSÃO (Isso faz o login funcionar e "entrar" no robô)
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

# =============================================================================================================
# 3. DESIGN BLACK-LABEL (NEON & ONYX)
# =============================================================================================================
st.markdown("""
<style>
    .stApp { background-color: #02040a !important; color: #f8fafc !important; }
    [data-testid="stHeader"] { display: none !important; }
    
    /* Chassi de Login e Minerador */
    .chassi-elite {
        background: linear-gradient(145deg, #0f172a, #02040a);
        border: 2px solid #00ff87; border-radius: 20px;
        padding: 40px; text-align: center; max-width: 500px; margin: 0 auto;
        box-shadow: 0 0 30px rgba(0, 255, 135, 0.2);
    }

    /* Robô Neon Giga */
    .robot-neon {
        font-size: 100px; text-align: center; filter: drop-shadow(0 0 20px #00ff87);
        animation: pulse 2s infinite alternate;
    }
    @keyframes pulse { from { transform: scale(1); } to { transform: scale(1.05); } }

    /* Inputs e Botões Neon */
    div[data-baseweb="input"] { background-color: #060913 !important; border: 1.5px solid #00ff87 !important; border-radius: 50px !important; }
    input { color: #ffffff !important; background-color: transparent !important; }
    .stButton > button {
        background: linear-gradient(135deg, #00ff87 0%, #00ffcc 100%) !important;
        color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
        padding: 15px !important; width: 100%; border: none !important; box-shadow: 0 0 20px #00ff8766;
    }
    .card-sugestao { background: #0f172a; border-left: 4px solid #00ff87; padding: 15px; border-radius: 8px; margin-bottom: 12px; }
</style>
""", unsafe_allow_html=True)

# =============================================================================================================
# 4. TELA DE LOGIN (CONEXÃO PARTICULAR)
# =============================================================================================================
if not st.session_state.autenticado:
    st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True)
    st.markdown('<div class="robot-neon">🤖</div>', unsafe_allow_html=True)
    st.markdown('<h1 style="text-align:center; color:#00ff87;">CONEXÃO PARTICULAR</h1>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="chassi-elite">', unsafe_allow_html=True)
        user_email = st.text_input("E-mail do Operador:", placeholder="admin@elite.com")
        user_password = st.text_input("Senha Criptografada:", type="password", placeholder="******")
        
        if st.button("🔓 ENTRAR NO TERMINAL"):
            if user_email == "admin@elite.com" and user_password == "123456":
                st.session_state.autenticado = True
                st.success("ACESSO LIBERADO!")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Credenciais Inválidas.")
        st.markdown('</div>', unsafe_allow_html=True)

# =============================================================================================================
# 5. TELA DO MINERADOR (SÓ APARECE APÓS LOGIN)
# =============================================================================================================
else:
    st.markdown('<div class="robot-neon">🤖</div>', unsafe_allow_html=True)
    st.markdown('<h1 style="text-align:center; color:#00ff87;">MINERADOR CIBERNÉTICO ELITE</h1>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="chassi-elite" style="max-width: 800px;">', unsafe_allow_html=True)
        prod_alvo = st.text_input("💎 Ativo para Mineração:", value="Sugar Defender")
        if st.button("🚀 DISPARAR SCANNER SÍNCRONO"):
            status = st.empty()
            esteira = st.empty()
            
            termos = ["Official Website", "Buy Now", "Discount", "Reviews", "Ingredients"]
            results = []
            
            for t in termos:
                status.info(f"⛏️ [LINKANDO]: {prod_alvo} {t}")
                results.append({"Termo": f"{prod_alvo} {t}", "CPC": f"$ {random.uniform(2.5, 5.0):.2f}"})
                esteira.dataframe(pd.DataFrame(results), use_container_width=True)
                time.sleep(0.5)
            
            status.success("✅ Varredura Completa!")
            
            st.write("---")
            cols = st.columns(2)
            for i, res in enumerate(results):
                with cols[i % 2]:
                    st.markdown(f'<div class="card-sugestao"><b>{res["Termo"]}</b><br>Lance: {res["CPC"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    if st.sidebar.button("🔴 SAIR"):
        st.session_state.autenticado = False
        st.rerun()
