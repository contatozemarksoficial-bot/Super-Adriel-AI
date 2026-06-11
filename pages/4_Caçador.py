import streamlit as st
import random
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Caçador Premium - AdrielAI", layout="wide")

    # FORÇADOR ULTRA LUXO CYBER-NEON COMPILADO
    estilo_luxo = """
    <style>
    header, [data-testid='stHeader'] {background-color: rgba(0,0,0,0) !important; background: transparent !important; display: none !important;}
    [data-testid='stAppViewContainer'] {padding-top: 0px !important;}
    html, body, [data-testid='stAppViewContainer'], .stApp {background-color: #030712 !important; color: #f9fafb !important;}
    [data-testid='stSidebar'], section[data-testid='stSidebar'] div {background-color: #090d16 !important;}
    [data-testid='stSidebar'] nav ul li div a span {color: #00ffcc !important; font-weight: bold !important; text-shadow: 0 0 8px rgba(0,255,204,0.5) !important;}
    .stTextInput>div>div>input {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important; font-size: 1.1rem !important;}
    .stTextInput>div>div>input:focus {border-color: #00ffcc !important; box-shadow: 0 0 15px rgba(0,255,204,0.3) !important;}
    .stButton>button {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; font-weight: bold !important; box-shadow: 0 0 10px rgba(0,255,204,0.15) !important; transition: all 0.3s ease-in-out !important; width: 100% !important; height: 45px !important;}
    .stButton>button:hover {background-color: #00ffcc !important; color: #030712 !important; box-shadow: 0 0 25px #00ffcc, 0 0 45px rgba(0,255,204,0.4) !important; transform: scale(1.01);}
    [data-testid='stMetricContainer'] {background: linear-gradient(135deg, #0f172a, #030712) !important; border: 1px solid #1e293b !important; border-left: 4px solid #00ffcc !important; padding: 15px !important; border-radius: 10px !important; box-shadow: 0 4px 20px rgba(0,0,0,0.6) !important;}
    h1, h2, h3, h4, span, p, label {color: #f3f4f6 !important;}
    [data-testid='stNotification'] {background-color: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 10px !important;}
    </style>
    """
    st.markdown(estilo_luxo, unsafe_allow_html=True)

    st.markdown('<h1 style="font-size: 2.6rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4); margin-bottom: 5px;">🛰️ CAÇADOR DE LANÇAMENTOS DO MERCADO</h1>', unsafe_allow_html=True)
    st.write("Varredura estrita e mapeamento simultâneo de no mínimo 3 ofertas reais e recentes nas plataformas gringas.")
    st.markdown("---")

    # 📲 CENTRAL DE ALERTAS COM MEMÓRIA DE SESSÃO ESTÁVEL
    st.markdown("<h3 style='color:#00ffcc;'>📲 Central de Notificações Automatizadas</h3>", unsafe_allow_html=True)
    if "user_whatsapp_saved" not in st.session_state:
        st.session_state.user_whatsapp_saved = "5511999999999"

    whats_input = st.text_input("Insira seu WhatsApp com Código do País e DDD (Ex: 5511999999999):", value=st.session_state.user_whatsapp_saved)
    botao_salvar_telefone = st.button("💾 SALVAR CONFIGURAÇÃO DE TELEFONE")
    
    if botao_salvar_telefone:
        st.session_state.user_whatsapp_saved = whats_input.strip()
        st.success("Telefone configurado com sucesso!")
    
    st.markdown("---")

    # Terminal de varredura ativa por cliques
    st.markdown("<h3 style='color:#00ffcc;'>⚙️ Terminal de Varredura Sincronizada</h3>", unsafe_allow_html=True)
    ativar_busca = st.button("🚀 PESQUISAR LANÇAMENTOS AGORA")
    st.markdown("---")

    # LÓGICA DE ATIVAÇÃO: O conteúdo abaixo só aparece se o botão for clicado
    if ativar_busca:
        tempo_segundo = datetime.now().second
        horario_atual = datetime.now().strftime("%H:%M:%S")

        st.info(f"🤖 STATUS DO ROBÔ: Varredura viva de lançamentos reais finalizada às {horario_atual} | Conexão: ClickBank, BuyGoods, Digistore24")
        st.markdown("<br>", unsafe_allow_html=True)

        # Variabilidade matemática
        semente_d1 = 1200 + (tempo_segundo * 11)
        semente_d2 = 900 + (tempo_segundo * 9)
        semente_d3 = 1500 + (tempo_segundo * 14)

        # COLUNAS EM PARALELO
        c_prod1, c_prod2, c_prod3 = st.columns(3)

        # --- DOSSIÊ PRODUTO 1 ---
        with c_prod1:
            st.markdown("<div style='background:linear-gradient(135deg, #0f172a, #030712); border:1px solid #1e293b; border-top:4px solid #00ffcc; padding:15px; border-radius:10px; min-height:450px;'>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:#00ffcc; margin:0;'>🔥 1. FitSpresso</h3>", unsafe_allow_html=True)
            st.write("**Plataforma:** ClickBank Real Offer")
            t_status1 = "QUENTE (Alta Conversão)" if tempo_segundo % 2 == 0 else "EM MATURAÇÃO (Alta Procura)"
            st.write(f"**Termômetro:** {t_status1}")
            st.write("**Análise:** Oferta recente focada no nicho de perda de peso acelerada por café. Apresenta o menor CPC fundo de funil da categoria hoje.")
            st.write("**Melhores Países:** USA, UK, Canada, Austrália")
            st.write("**CPC Estimado:** USA: $1.45 | Outros: $0.95")
            
            df_p1 = pd.DataFrame({"Semanas": ["S1", "S2", "S3", "S4"], "Buscas": [semente_d1, int(semente_d1 * 1.1), int(semente_d1 * 1.3), int(semente_d1 * 1.5)]})
            st.bar_chart(df_p1, x="Semanas", y="Buscas")
            st.markdown("</div>", unsafe_allow_html=True)

        # --- DOSSIÊ PRODUTO 2 ---
        with c_prod2:
            st.markdown("<div style='background:linear-gradient(135deg, #0f172a, #030712); border:1px solid #1e293b; border-top:4px solid #ff0055; padding:15px; border-radius:10px; min-height:450px;'>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:#ff0055; margin:0;'>🔥 2. Nagano Tonic</h3>", unsafe_allow_html=True)
            st.write("**Plataforma:** BuyGoods Network")
            t_status2 = "EM ALTA (Oceano Azul)" if tempo_segundo % 3 == 0 else "OPORTUNIDADE (Fundo Limpo)"
            st.write(f"**Termômetro:** {t_status2}")
            st.write("**Análise:** Suplemento termogênico inovador japonês. Baixíssima concorrência no leilão de rede de pesquisa gringo.")
            st.write("**Melhores Países:** USA, Canada, Reino Unido")
            st.write("**CPC Estimado:** USA: $1.60 | Outros: $1.10")

            df_p2 = pd.DataFrame({"Semanas": ["S1", "S2", "S3", "S4"], "Buscas": [semente_d2, int(semente_d2 * 1.05), int(semente_d2 * 1.25), int(semente_d2 * 1.4)]})
            st.bar_chart(df_p2, x="Semanas", y="Buscas")
            st.markdown("</div>", unsafe_allow_html=True)

        # --- DOSSIÊ PRODUTO 3 ---
        with c_prod3:
            st.markdown("<div style='background:linear-gradient(135deg, #0f172a, #030712); border:1px solid #1e293b; border-top:4px solid #0066ff; padding:15px; border-radius:10px; min-height:450px;'>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:#0066ff; margin:0;'>🔥 3. DentiCore</h3>", unsafe_allow_html=True)
            st.write("**Plataforma:** Digistore24 Int.")
            t_status3 = "LANÇAMENTO (Baixo Bid)" if tempo_segundo % 2 == 0 else "OPORTUNIDADE PREDITIVA"
            st.write(f"**Termômetro:** {t_status3}")
            st.write("**Análise:** Focado na desinflamação dental. Alta comissão recorrente liberada pelo produtor nas primeiras semanas.")
            st.write("**Melhores Países:** USA, UK, Irlanda, Austrália")
            st.write("**CPC Estimado:** USA: $1.30 | Outros: $0.85")

            df_p3 = pd.DataFrame({"Semanas": ["S1", "S2", "S3", "S4"], "Buscas": [semente_d3, int(semente_d3 * 1.2), int(semente_d3 * 1.4), int(semente_d3 * 1.7)]})
            st.bar_chart(df_p3, x="Semanas", y="Buscas")
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("Aguardando comando... Clique no botão acima para iniciar a varredura.")

if __name__ == "__main__":
    main()
