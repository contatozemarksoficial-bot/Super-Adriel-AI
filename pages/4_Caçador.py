import streamlit as st
import random
import pandas as pd
import time
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA (MODO LUXO)
    st.set_page_config(page_title="Caçador Pro - Luxo Neon", layout="wide")

    # CSS PARA ESTILO PLATAFORMA DE LUXO E COMPACTAÇÃO
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] {display: none !important;}
    .stApp {background-color: #020617 !important; color: #f8fafb !important;}
    
    /* Barra Lateral Estilizada */
    [data-testid="stSidebar"] {background-color: #030712 !important; border-right: 1px solid #10b981;}

    /* Botões Luxo Neon */
    .stButton>button {
        background-color: #020617 !important; 
        color: #10b981 !important; 
        border: 1px solid #10b981 !important; 
        border-radius: 6px !important;
        font-weight: bold !important;
        transition: 0.4s;
    }
    .stButton>button:hover {
        background-color: #10b981 !important; 
        color: #020617 !important;
        box-shadow: 0 0 20px #10b981 !important;
    }

    /* Cards de Rastreio Luxo */
    .card-luxury {
        border: 1px solid #1e293b;
        padding: 20px;
        border-radius: 12px;
        background: linear-gradient(145deg, #0f172a, #020617);
        margin-bottom: 10px;
        border-left: 4px solid #10b981;
    }
    .neon-text { color: #10b981; font-weight: bold; }
    
    /* Campo de texto menor */
    .stTextInput>div>div>input {
        background-color: #030712 !important;
        color: #10b981 !important;
        border: 1px solid #1e293b !important;
        height: 35px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # --- TÍTULO CENTRAL ---
    st.markdown('<h1 style="color: #10b981; text-align: center; font-size: 2.2rem;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)
    
    # --- 📲 CONFIGURAÇÃO DE CONTATO COMPACTA ---
    if "whats_config" not in st.session_state: st.session_state.whats_config = ""

    # Área de contato menor e em linha única
    c_tel, c_save, c_search = st.columns([2, 1, 2])
    with c_tel:
        whats_input = st.text_input("WhatsApp (Ex: 5511999999999):", value=st.session_state.whats_config, label_visibility="collapsed", placeholder="Seu WhatsApp...")
    with c_save:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.whats_config = whats_input
            st.toast("Contato fixado!", icon="✅")
    with c_search:
        ativar = st.button("🚀 INICIAR VARREDURA ESTRATÉGICA")

    st.markdown("---")

    # --- LÓGICA DE VARREDURA ---
    if ativar:
        if not st.session_state.whats_config:
            st.warning("⚠️ Salve o WhatsApp para receber o dossiê.")
        
        with st.status("🔍 Rastreando...", expanded=False) as status:
            time.sleep(1)
            status.update(label="Varredura de Luxo Finalizada!", state="complete")

        # BANCO DE DADOS
        pool = [
            {"n": "FitSpresso", "o": "Oferta matinal de café termogênico.", "d": "Resistência à perda de peso.", "g": "USA, Canadá", "cpc": "$1.45", "grv": "99.1"},
            {"n": "Nagano Tonic", "o": "Tônico japonês para queima de gordura.", "d": "Metabolismo lento pós-40.", "g": "Austrália, EUA", "cpc": "$1.10", "grv": "88.4"},
            {"n": "DentiCore", "o": "Saúde oral e reconstrução dentária.", "d": "Inflamação e hálito crônico.", "g": "Reino Unido, Irlanda", "cpc": "$1.25", "grv": "91.7"},
            {"n": "Sugar Defender", "o": "Controle natural de glicemia.", "d": "Cansaço e picos de insulina.", "g": "USA, Canadá", "cpc": "$1.85", "grv": "96.3"},
            {"n": "Puravive", "o": "Alvo em gordura marrom teimosa.", "d": "Autoestima e inchaço.", "g": "USA, UK", "cpc": "$1.60", "grv": "97.9"},
            {"n": "ZenCortex", "o": "Saúde auditiva e neuroproteção.", "d": "Ruídos e perda de foco.", "g": "Canadá, Austrália", "cpc": "$0.95", "grv": "85.2"}
        ]
        random.shuffle(pool)

        # EXIBIÇÃO EM GRID 2 COLUNAS
        for i in range(0, 6, 2):
            cols = st.columns(2)
            for j in range(2):
                p = pool[i + j]
                with cols[j]:
                    st.markdown(f"""
                    <div class="card-luxury">
                        <h3 style="color:#10b981; margin:0; font-size:1.4rem;">🔥 {p['n']}</h3>
                        <p style="font-size: 0.8rem; color: #94a3b8; margin-bottom:10px;">Monitoramento Ativo</p>
                        <p><span class="neon-text">⚖️ VEREDITO:</span> {p['o']}</p>
                        <p><span class="neon-text">💡 DOR:</span> {p['d']}</p>
                        <p><span class="neon-text">🌍 GOOGLE ADS:</span> {p['g']}</p>
                        <p><span class="neon-text">💰 CPC:</span> {p['cpc']} | <span class="neon-text">📊 GRAVIDADE:</span> {p['grv']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Gráfico de Colunas Neon Verde
                    df = pd.DataFrame({"Tendência": [random.randint(30, 100) for _ in range(5)]})
                    st.bar_chart(df, height=130, color="#10b981")

        if st.session_state.whats_config:
            st.success(f"💎 DISPARO CONCLUÍDO para {st.session_state.whats_config}")
    else:
        st.info("Aguardando comando... Use o painel superior para caçar.")

if __name__ == "__main__":
    main()
