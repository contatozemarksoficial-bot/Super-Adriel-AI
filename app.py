import streamlit as st
import time

# 1. CONFIGURAÇÃO PREMIUM DA INTERFACE
st.set_page_config(page_title="Adriel-AI Pro", layout="wide", initial_sidebar_state="collapsed")

# 2. INJEÇÃO DE CSS (DESIGN DARK COM BOTÕES CIANO)
st.markdown("""
<style>
    .stApp { background-color: #060913 !important; color: #f8fafc !important; }
    [data-testid="stHeader"] { display: none !important; }
    .block-container { padding-top: 2rem !important; }
    
    /* Card de Planos */
    .card-plano {
        background-color: #080f1d !important;
        border: 1px solid #1e293b !important;
        border-radius: 14px !important;
        padding: 20px !important;
        text-align: center;
        margin-bottom: 10px;
    }
    
    /* Botão Estilo Hostinger (Ciano) */
    .stButton > button, div.stLinkButton > a {
        background: linear-gradient(135deg, #00ffcc 0%, #00FF87 100%) !important;
        color: #030712 !important;
        font-weight: 900 !important;
        border-radius: 30px !important;
        width: 100% !important;
        border: none !important;
        text-decoration: none !important;
        display: inline-block;
        padding: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Inicialização do estado de login
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

# 3. LÓGICA DE LOGIN E BLOQUEIO
if not st.session_state.autenticado:
    st.markdown('<h2 style="text-align:center; color:white;">🤖 Adriel-AI <span style="background:#ff0055; padding:2px 8px; border-radius:4px; font-size:14px;">TRANCADO</span></h2>', unsafe_allow_html=True)
    
    st.write("---")
    chave_digitada = st.text_input("Digite a sua Chave de Acesso SaaS abaixo:", placeholder="Insira o Token de Ativação...", type="password")
    
    if st.button("🔑 EFETUAR LOGIN NO SISTEMA"):
        if chave_digitada == "ADRIEL-VIP-2026":
            st.session_state.autenticado = True
            st.success("✅ Licença Validada!")
            time.sleep(0.5)
            st.rerun()
        else:
            st.error("❌ Chave de Acesso Inválida.")

    st.write("---")
    st.markdown("<h3 style='text-align:center;'>💳 CONTRATAR ASSINATURA DO ROBÔ</h3>", unsafe_allow_html=True)
    
    # Colunas de Planos com preços reais da Hostinger
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""<div class="card-plano">
            <p style="color:#94a3b8; font-size:12px;">PREMIUM</p>
            <h2 style="color:white;">$2.99<span style="font-size:14px;">/mês</span></h2>
            <p style="font-size:13px; color:#cbd5e1;">100 Websites + SSL Grátis</p>
        </div>""", unsafe_allow_html=True)
        st.link_button("ASSINAR PREMIUM", "https://hostinger.com")

    with col2:
        st.markdown("""<div class="card-plano" style="border: 1px solid #00ffcc !important;">
            <p style="color:#00ffcc; font-size:12px;">BUSINESS (RECOMENDADO)</p>
            <h2 style="color:white;">$3.99<span style="font-size:14px;">/mês</span></h2>
            <p style="font-size:13px; color:#cbd5e1;">Ferramentas de IA + CDN</p>
        </div>""", unsafe_allow_html=True)
        st.link_button("ASSINAR BUSINESS", "https://hostinger.com")

    with col3:
        st.markdown("""<div class="card-plano">
            <p style="color:#94a3b8; font-size:12px;">CLOUD STARTUP</p>
            <h2 style="color:white;">$7.99<span style="font-size:14px;">/mês</span></h2>
            <p style="font-size:13px; color:#cbd5e1;">IP Dedicado + Performance</p>
        </div>""", unsafe_allow_html=True)
        st.link_button("ASSINAR CLOUD", "https://hostinger.com")

else:
    # PAINEL DO USUÁRIO LOGADO
    st.title("🚀 Painel Adriel-AI Pro")
    st.success("Conectado com sucesso. Bem-vindo ao ecossistema de IA.")
    
    if st.button("SAIR DO SISTEMA"):
        st.session_state.autenticado = False
        st.rerun()
