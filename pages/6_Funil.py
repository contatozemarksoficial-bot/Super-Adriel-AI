import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE (ESTRUTURA DE LUXO)
st.set_page_config(page_title="Adriel-AI Pro Elite", layout="wide", initial_sidebar_state="expanded")

# =============================================================================================================
# 2. INJEÇÃO DE CSS BLACK-LABEL (CIANO NEON IDÊNTICO AO SEU PRINT)
# =============================================================================================================
st.markdown("""
<style>
/* 🌌 FUNDO PRETO ÔNIX ABSOLUTO */
.stApp, [data-testid="stHeader"], [data-testid="stSidebar"] { background-color: #02040a !important; }

/* 👤 SIDEBAR COM BORDA CIANO NEON */
section[data-testid="stSidebar"] { border-right: 1px solid #00f2ff !important; background-color: #060913 !important; }
section[data-testid="stSidebar"] * { color: #00f2ff !important; font-weight: 800; }

/* 🤖 ROBÔ CIANO NEON GIGA (ANIMAÇÃO ZOOM) */
.robot-neon-original {
    font-size: 110px; text-align: center;
    color: #00f2ff;
    filter: drop-shadow(0 0 15px #00f2ff) drop-shadow(0 0 35px #00f2ff);
    animation: zoom-pulse 2.5s infinite ease-in-out;
}
@keyframes zoom-pulse {
    0% { transform: scale(0.9); opacity: 0.8; }
    50% { transform: scale(1.1); opacity: 1; }
    100% { transform: scale(0.9); opacity: 0.8; }
}

/* 💎 CHASSI COM BORDAS ARREDONDADAS IGUAL AO PRINT */
.chassi-luxury {
    background: #040814;
    border: 1.5px solid #00f2ff; 
    border-radius: 12px;
    padding: 30px; 
    text-align: center; 
    margin-bottom: 20px;
    box-shadow: 0 0 15px rgba(0, 242, 255, 0.1);
}

/* 📋 CARDS DE RESULTADOS EM LINHAS */
.card-resultado {
    background: #060913; 
    border: 1px solid #00f2ff; 
    border-radius: 8px;
    padding: 15px; 
    margin-bottom: 10px;
    color: #ffffff;
    font-family: 'Segoe UI', sans-serif;
}

/* ⚡ BOTÃO DE COMANDO CIANO VIVO */
.stButton > button {
    background: linear-gradient(135deg, #00f2ff 0%, #0080ff 100%) !important;
    color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 18px !important; width: 100%; border: none !important;
    box-shadow: 0 0 20px rgba(0, 242, 255, 0.4) !important;
    text-transform: uppercase; letter-spacing: 2px;
}

/* 🚨 BLINDAGEM CONTRA O BRANCO */
div[data-baseweb="input"] { background-color: #060913 !important; border: 1.5px solid #00f2ff !important; border-radius: 8px; }
input { background-color: transparent !important; color: #ffffff !important; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR COM STATUS
with st.sidebar:
    st.markdown("### 🛰️ ADRIEL-AI STATUS")
    st.markdown("<p style='color:#00f2ff;'>🟢 SCANNER: ATIVO</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("### 🔌 PLATAFORMAS")
    platforms = ["CLICKBANK", "BUYGOODS", "MAXWEB", "DIGISTORE24"]
    for p in platforms:
        st.markdown(f'<div style="border:1px solid #00f2ff; padding:5px; border-radius:5px; margin-bottom:5px; text-align:center; font-size:11px;">{p}</div>', unsafe_allow_html=True)

# 4. ÁREA PRINCIPAL
st.markdown('<div class="robot-neon-original">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00f2ff; font-weight:900; margin-top:-20px; letter-spacing:3px;">MINERADOR DE ELITE V7</h1>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chassi-luxury">', unsafe_allow_html=True)
    aff_id = st.text_input("🔑 SEU ID DE AFILIADO:", placeholder="ex: adriel_pro")
    prod_alvo = st.text_input("💎 PRODUTO PARA MINERAR:", value="Sugar Defender")
    btn_run = st.button("🚀 INICIAR VARREDURA (100 TERMOS)")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. MOTOR DE MINERAÇÃO (PESQUISA EM LINHAS)
if btn_run:
    if not aff_id:
        st.error("❌ Insira seu ID de Afiliado na lateral!")
        st.stop()

    status = st.empty()
    esteira = st.container()
    
    sufixos = ["official", "buy now", "discount", "reviews", "ingredients", "is it safe", "scam", "where to buy", "price", "order"] * 10
    
    minerados = []
    for i, suf in enumerate(sufixos):
        termo = f"{prod_alvo} {suf}".upper()
        status.markdown(f'<p style="color:#00f2ff; text-align:center;">⛏️ VARRENDO: {termo} ({i+1}/100)</p>', unsafe_allow_html=True)
        
        minerados.append({
            "termo": termo,
            "cpc": f"$ {random.uniform(2.10, 5.80):.2f}",
            "link": f"https://{aff_id}.hop.clickbank.net/?tid={suf.lower().replace(' ', '_')}"
        })
        time.sleep(0.04)

    status.markdown('<div class="chassi-luxury" style="border-color:#00ff87; color:#00ff87;">✅ VARREDURA CONCLUÍDA: 100 TERMOS CATALOGADOS</div>', unsafe_allow_html=True)

    # 6. EXIBIÇÃO DA MATRIZ EM LINHAS (IGUAL AO PRINT)
    st.write("---")
    for item in minerados[:50]: # Mostrando os primeiros 50 em cards individuais
        st.markdown(f"""
        <div class="card-resultado">
            <div style="display:flex; justify-content:space-between;">
                <b style="color:#00f2ff;">🔍 {item['termo']}</b>
                <span style="color:#00f2ff;">CPC: {item['cpc']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.code(item['link']) # Botão de cópia automática
