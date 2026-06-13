import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE
st.set_page_config(page_title="Terminal Adriel-AI Elite", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. CSS BLACK-LABEL (TRAVANDO O VERDE NEON E FIM DO BRANCO)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ABSOLUTO */
.stApp, [data-testid="stHeader"], [data-testid="stSidebar"] { background-color: #02040a !important; }
section[data-testid="stSidebar"] { border-right: 2px solid #00ff87 !important; background-color: #060913 !important; }

/* 🤖 ROBÔ VERDE NEON EM ZOOM */
.robot-neon {
    font-size: 100px; text-align: center;
    filter: drop-shadow(0 0 25px #00ff87);
    animation: zoom-pulse 2.5s infinite ease-in-out;
}
@keyframes zoom-pulse { 0% { transform: scale(0.95); } 50% { transform: scale(1.1); } 100% { transform: scale(0.95); } }

/* 💎 CHASSI COM BORDA NEON */
.chassi-luxury {
    background: linear-gradient(145deg, #0f172a, #02040a);
    border: 2px solid #00ff87; border-radius: 20px;
    padding: 35px; text-align: center; margin-bottom: 25px;
}

/* ⚡ BOTÃO DE COMANDO NEON */
.stButton > button {
    background: linear-gradient(135deg, #00ff87 0%, #00ffcc 100%) !important;
    color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 20px !important; width: 100%; border: none !important;
    box-shadow: 0 0 25px rgba(0, 255, 135, 0.4) !important;
}

/* 📋 CARD DE ENTRADA DIRETA */
.card-acesso { 
    background: #0f172a; border: 1.5px solid #1e293b; border-left: 6px solid #00ff87;
    padding: 25px; border-radius: 12px; margin-bottom: 15px; text-align: center;
}

.btn-entrar {
    display: inline-block; background: #00ff87; color: #000 !important;
    text-decoration: none !important; padding: 12px 30px; border-radius: 30px;
    font-weight: 900; margin-top: 15px; transition: 0.3s;
    box-shadow: 0 0 15px rgba(0, 255, 135, 0.4);
}
.btn-entrar:hover { transform: scale(1.05); box-shadow: 0 0 25px #00ff87; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR: CREDENCIAIS
with st.sidebar:
    st.markdown("### 🔑 CREDENCIAIS")
    aff_id = st.text_input("Seu ID de Afiliado:", placeholder="ex: adriel123")
    plataforma = st.selectbox("Escolha a Rede:", ["CLICKBANK", "BUYGOODS", "DIGISTORE24", "MAXWEB"])
    st.write("---")
    if aff_id:
        st.markdown(f"### 📡 STATUS: <span style='color:#00ff87;'>CONECTADO</span>", unsafe_allow_html=True)
    else:
        st.markdown(f"### 📡 STATUS: <span style='color:#ff4b4b;'>AGUARDANDO ID</span>", unsafe_allow_html=True)

# 4. ÁREA PRINCIPAL
st.markdown('<div class="robot-neon">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ff87; font-weight:900; margin-top:-10px;">TERMINAL DE ENTRADA DIRETA</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chassi-luxury">', unsafe_allow_html=True)
    prod_alvo = st.text_input("💎 Nome do Ativo (ex: Sugar Defender):", value="Sugar Defender")
    btn_start = st.button(f"🚀 LIBERAR ACESSO DIRETO PARA {plataforma}")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. GERADOR DE LINKS DE ENTRADA
if btn_start:
    if not aff_id:
        st.error("❌ ERRO CRÍTICO: Preencha seu ID de Afiliado na barra lateral!")
        st.stop()

    status = st.empty()
    lista_links = []
    
    opcoes = [
        {"nome": "PÁGINA DE VENDAS", "track": "vendas_robo"},
        {"nome": "CHECKOUT DIRETO", "track": "checkout_robo"},
        {"nome": "PÁGINA DE DESCONTO", "track": "promo_robo"}
    ]
    
    for op in opcoes:
        status.markdown(f'<div style="color:#00ff87; padding:10px;">⛏️ [LINKANDO]: {op["nome"]}...</div>', unsafe_allow_html=True)
        
        # Lógica de Linkagem Real
        if plataforma == "CLICKBANK":
            url = f"https://{aff_id}.hop.clickbank.net/?tid={op['track']}"
        elif plataforma == "BUYGOODS":
            url = f"https://buygoods.com{aff_id}&prod={prod_alvo.lower()}&track={op['track']}"
        elif plataforma == "DIGISTORE24":
            url = f"https://digistore24.com{prod_alvo.lower()}/{aff_id}/{op['track']}"
        else:
            url = f"https://maxweb.com{prod_alvo.lower()}/{aff_id}?tid={op['track']}"
            
        lista_links.append({"nome": op["nome"], "url": url})
        time.sleep(0.4)

    status.empty()

    # 6. EXIBIÇÃO DOS CARDS COM BOTÃO DE ENTRADA REAL
    st.write("---")
    cols = st.columns(3)
    for idx, item in enumerate(lista_links):
        with cols[idx]:
            st.markdown(f"""
            <div class="card-acesso">
                <b style="color:#00ff87; font-size:16px;">{item['nome']}</b><br>
                <a href="{item['url']}" target="_blank" class="btn-entrar">ENTRAR AGORA →</a>
            </div>
            """, unsafe_allow_html=True)

    st.success("✅ Protocolo de Entrada Liberado. Clique nos botões acima para abrir as páginas.")
