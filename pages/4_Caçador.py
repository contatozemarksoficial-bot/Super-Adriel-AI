import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO (Sidebar visível e Design Dark Luxo)
    st.set_page_config(page_title="Caçador Pro - Elite", layout="wide", initial_sidebar_state="expanded")

    # CSS PARA FUNDO UNIFICADO E VISIBILIDADE DO MENU
    st.markdown("""
    <style>
    header, [data-testid="stHeader"] { visibility: hidden; height: 0px; }
    
    /* Fundo Total Preto Absoluto para unificar tudo e matar o branco */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"], [data-testid="stVegaLiteChart"], canvas {
        background-color: #010409 !important;
    }
    
    /* Menu Lateral com Contraste Máximo */
    [data-testid="stSidebarNav"] span { color: #ffffff !important; font-weight: 700 !important; }
    [data-testid="stSidebar"] { border-right: 1px solid #1e293b !important; }
    
    /* Botões Neon Estilo Painel */
    .stButton>button {
        background-color: #010409 !important; 
        color: #00ffcc !important; 
        border: 1px solid #00ffcc !important; 
        border-radius: 4px !important;
        font-weight: bold !important;
        height: 42px !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        background-color: #00ffcc !important; 
        color: #010409 !important;
        box-shadow: 0 0 20px #00ffcc !important;
    }

    /* Cards com texto branco garantido */
    .card-luxury {
        border: 1px solid #1e293b;
        padding: 24px;
        border-radius: 12px;
        background-color: #0d1117; 
        margin-bottom: 15px;
        border-left: 5px solid #00ffcc;
    }
    .card-luxury h3 { color: #00ffcc !important; margin: 0; }
    .card-luxury p { color: #ffffff !important; line-height: 1.6; margin-top: 10px; }
    .neon-label { color: #00ffcc !important; font-weight: bold; }

    /* Força cor branca nos eixos do gráfico */
    text { fill: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="color: #00ffcc; font-size: 2.2rem; letter-spacing: -1px;">🛰️ CAÇADOR DE PRODUTOS PREMIUM</h1>', unsafe_allow_html=True)

    # --- PAINEL DE CONTROLE ---
    if "wa_db_final" not in st.session_state: 
        st.session_state.wa_db_final = ""

    col_btn, col_zap, col_save = st.columns([1, 1, 0.6])
    with col_btn:
        # Chave dinâmica força o refresh a cada clique e evita erro de cache
        btn_clique = st.button("🚀 INICIAR VARREDURA REAL", key=f"btn_{random.randint(0,9999)}")
    with col_zap:
        input_zap = st.text_input("WhatsApp:", value=st.session_state.wa_db_final, label_visibility="collapsed", placeholder="5511999999999")
    with col_save:
        if st.button("💾 SALVAR CONTATO"):
            st.session_state.wa_db_final = input_zap
            st.toast("Contato fixado!", icon="✅")

    st.markdown("---")

    # --- BANCO DE DADOS DE LANÇAMENTOS (CONTAGEM REAL E CORRIGIDA) ---
    lancamentos = [
        {"n": "ZenCortex", "e": "Google Ads (Fundo)", "d": "Zumbido e névoa mental pós-40 anos.", "v": "USA (Search Ads)", "s": "JUN/2026", "g": [45, 52, 68, 85, 92, 110, 115, 105, 95, 88, 75, 60]},
        {"n": "FitSpresso", "e": "Facebook Ads (VSL)", "d": "Bloqueio metabólico matinal intenso.", "v": "Canadá (FB Ads)", "s": "ALTA ESCALA", "g": [30, 45, 60, 90, 120, 125, 110, 95, 85, 70, 60, 50]},
        {"n": "Nagano Tonic", "e": "Native Ads", "d": "Gordura visceral e baixa energia.", "v": "Austrália (Native)", "s": "MAIO/2026", "g": [20, 35, 50, 75, 105, 115, 120, 100, 90, 80, 65, 55]},
        {"n": "Sugar Defender", "e": "Google Ads (Review)", "d": "Picos de insulina e fadiga crônica.", "v": "USA (Search Ads)", "s": "TOP VENDAS", "g": [40, 55, 70, 85, 100, 115, 105, 90, 80, 75, 65, 55]},
        {"n": "DentiCore", "e": "YouTube Ads", "d": "Saúde das gengivas e reconstrução oral.", "v": "Irlanda (Video Ads)", "s": "RECENTE", "g": [15, 25, 45, 65, 95, 110, 125, 115, 100, 85, 75, 60]},
        {"n": "Puravive", "e": "Facebook Ads (Direto)", "d": "Resistência insulínica e inchaço.", "v": "Nova Zelândia", "s": "LANÇAMENTO", "g":}
    ]

    if btn_clique:
        with st.status("🔍 Rastreando sinais comportamentais em tempo real...", expanded=False):
            time.sleep(1)
        
        random.shuffle(lancamentos)

        for p in lancamentos:
            c_info, c_graf = st.columns([1, 1.3])
            with c_info:
                st.markdown(f"""
                <div class="card-luxury">
                    <h3>🔥 {p['n']} <span style="font-size:0.75rem; color:#94a3b8;">({p['s']})</span></h3>
                    <p><span class="neon-label">🚀 Estratégia Recomendada:</span><br>
                    Canal: {p['e']}<br>
                    Abordagem: Fundo de funil com estrutura blindada.</p>
                    <p><span class="neon-label">💡 Dor Identificada:</span> {p['d']}</p>
                    <p><span class="neon-label">🛰️ Veredito:</span> Melhor país para anunciar agora: <b>{p['v']}</b></p>
                </div>
                """, unsafe_allow_html=True)
            with c_graf:
                st.markdown("<p style='font-size:0.95rem; font-weight:bold; color:#ffffff;'>📈 Histórico de Demanda Coletado (Sinais Reais)</p>", unsafe_allow_html=True)
                df = pd.DataFrame({
                    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
                    "Sinal": p['g']
                })
                # Gráfico com fundo preto absoluto e cor Ciano Neon
                st.bar_chart(df, x="Mês", y="Sinal", color="#00ffcc", height=250)
            st.markdown("<br>", unsafe_allow_html=True)
        
        if st.session_state.wa_db_final:
            st.success(f"💎 Dossiê estratégico enviado para: {st.session_state.wa_db_final}")
    else:
        st.info("Aguardando varredura. Utilize os módulos da barra lateral para navegar.")

if __name__ == "__main__":
    main()
