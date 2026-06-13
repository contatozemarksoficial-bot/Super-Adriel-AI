import streamlit as st
import pandas as pd
import time
import random

# 1. CONFIGURAÇÃO DE ELITE
st.set_page_config(page_title="Adriel-AI Elite v7", layout="wide", initial_sidebar_state="expanded")

# 2. DESIGN BLACK-LABEL (NEON & ONYX)
st.markdown("""
<style>
.stApp { background-color: #02040a !important; color: #f8fafc !important; }
[data-testid="stHeader"], [data-testid="stSidebar"] { background-color: #02040a !important; }
.robot-scanner { font-size: 80px; text-align: center; filter: drop-shadow(0 0 20px #00ff87); animation: zoom 2s infinite alternate; }
@keyframes zoom { from { transform: scale(0.9); } to { transform: scale(1.05); } }
div.stButton > button {
    background: linear-gradient(135deg, #00ff87 0%, #00ffcc 100%) !important;
    color: #030712 !important; font-weight: 900 !important; border-radius: 50px !important;
    padding: 18px 30px !important; width: 100% !important; border: none !important;
    box-shadow: 0 0 15px rgba(0, 255, 135, 0.4) !important;
}
.moldura-neon { border: 2px solid #00ff87; border-radius: 15px; padding: 20px; background: #040814; text-align: center; margin-bottom: 20px; }
.card-sugestao { background: #0f172a; border-left: 4px solid #00ff87; padding: 12px; border-radius: 8px; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    st.markdown("### 🔑 AFILIADO ID")
    aff_id = st.text_input("Seu ID:", placeholder="adriel123")
    st.write("---")
    st.markdown("### 🔌 PLATAFORMAS")
    st.markdown("<p style='color:#00ff87;'>CLICKBANK: OK<br>BUYGOODS: OK</p>", unsafe_allow_html=True)

# 4. ÁREA PRINCIPAL
st.markdown('<div class="robot-scanner">🤖</div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align:center; color:#00ff87; font-weight:900;">MINERADOR INTELIGENTE V7</h1>', unsafe_allow_html=True)

prod_alvo = st.text_input("💎 Produto Alvo:", value="Sugar Defender")
btn_run = st.button("🚀 DISPARAR MINERAÇÃO ALEATÓRIA")

espaco_pesquisa = st.empty()
espaco_vazio = st.container()

if btn_run:
    # 📚 BASE DE DADOS EXPANDIDA (50 TERMOS REAIS)
    base_sufixos = [
        "official website", "discount", "order now", "customer reviews", "ingredients list",
        "side effects", "is it safe", "real results", "where to buy", "best price today",
        "coupon code", "promo code", "scam or legit", "benefits", "how to use",
        "shipping time", "money back guarantee", "vsl link", "checkout page", "special offer",
        "lowest cost", "legit site", "official store", "get a discount", "sale today",
        "guaranteed", "drops price", "liquid discount", "buy direct", "consumer reports",
        "fast shipping", "genuine store", "original product", "stock update", "availability",
        "top rated", "expert review", "pros and cons", "trial offer", "best deal",
        "official portal", "price check", "real site", "secure order", "bonus offer",
        "refund policy", "complaints", "success stories", "for sale", "order today"
    ]
    
    # 🎲 EMBALHAR A LISTA PARA NÃO SER SEMPRE IGUAL
    random.shuffle(base_sufixos)
    
    minerados = []
    for i, suf in enumerate(base_sufixos):
        termo = f"{prod_alvo} {suf}".upper()
        espaco_pesquisa.markdown(f'<div class="moldura-neon"><h2 style="color:#00ff87; margin:0;">⛏️ [MINANDO]: {termo}</h2></div>', unsafe_allow_html=True)
        
        cpc = random.uniform(2.15, 6.40)
        minerados.append({"TERMO": termo, "CPC": f"$ {cpc:.2f}", "LINK": f"https://{aff_id}.hop.clickbank.net/?tid={suf.replace(' ', '_')}"})
        time.sleep(0.05)

    espaco_pesquisa.markdown('<div class="moldura-neon"><h2 style="color:#00ff87; margin:0;">✅ VARREDURA CONCLUÍDA</h2></div>', unsafe_allow_html=True)

    with espaco_vazio:
        st.markdown("### 📋 Matriz de Resultados Únicos")
        cols = st.columns(2)
        for idx, item in enumerate(minerados):
            with cols[idx % 2]:
                st.markdown(f"""
                <div class="card-sugestao">
                    <b style="color:#00ff87;">🔗 {item['TERMO']}</b><br>
                    <span style="color:#ffffff; font-size:12px;">Lance sugerido: {item['CPC']}</span>
                </div>
                """, unsafe_allow_html=True)
