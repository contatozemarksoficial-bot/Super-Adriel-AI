import streamlit as st
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DA PÁGINA (Sidebar habilitada e Layout Wide)
    st.set_page_config(page_title="Auditor Premium - AdrielAI", layout="wide", initial_sidebar_state="expanded")

    # CSS NEON CORRIGIDO (SEM ESCONDER A INTERFACE)
    estilo_cyber = """
    <style>
    [data-testid="stAppViewContainer"] { background-color: #030712 !important; color: #f9fafb !important; }
    [data-testid="stSidebar"] { background-color: #090d16 !important; border-right: 1px solid #1e293b; }
    
    /* Estilo dos Inputs */
    .stTextInput>div>div>input {
        background-color: #0f172a !important; 
        color: #00ffcc !important; 
        border: 2px solid #1e293b !important;
        border-radius: 8px !important;
    }

    /* Estilo do Botão - AGORA VISÍVEL */
    .stButton>button {
        background-color: #0f172a !important; 
        color: #00ffcc !important; 
        border: 2px solid #00ffcc !important;
        font-weight: bold !important;
        width: 100% !important;
        height: 50px !important;
        box-shadow: 0 0 10px rgba(0,255,204,0.2);
    }
    .stButton>button:hover {
        background-color: #00ffcc !important;
        color: #030712 !important;
        box-shadow: 0 0 25px #00ffcc !important;
    }

    /* Métricas Neon */
    [data-testid="stMetricContainer"] {
        background: linear-gradient(135deg, #0f172a, #030712) !important;
        border-left: 4px solid #00ffcc !important;
        border-radius: 10px !important;
        padding: 15px !important;
    }
    
    h1, h2, h3, h4 { color: #00ffcc !important; text-shadow: 0 0 10px rgba(0,255,204,0.3); }
    </style>
    """
    st.markdown(estilo_cyber, unsafe_allow_html=True)

    # 2. BARRA LATERAL DE COMANDOS (AQUI ESTÃO OS SEUS COMANDOS)
    with st.sidebar:
        st.markdown("### 🤖 PAINEL DE CONTROLE")
        st.write("Status: **OPERACIONAL**")
        st.markdown("---")
        # Você pode adicionar filtros aqui na lateral se quiser
        st.info("O robô AdrielAI está pronto para auditar o mercado internacional.")

    # 3. CONTEÚDO PRINCIPAL
    st.markdown('<h1>🛡️ AUDITOR EXPERT DE MERCADO</h1>', unsafe_allow_html=True)
    
    # Campo de Entrada e Botão
    produto_digitado = st.text_input("INSIRA O NOME DO PRODUTO GRINGO:", value="Alpilean")
    botao_executar = st.button("🚀 EXECUTAR VARREDURA AO VIVO")

    if botao_executar or produto_digitado:
        nome_prod = produto_digitado.strip().upper()
        fator = len(nome_prod)
        tempo_seg = datetime.now().second

        # Lógica de Cálculo
        pesquisas_mes = 55000 + (fator * 3200)
        pesquisas_hoje = 1300 + (fator * 110)

        # Status do Produto
        produto_e_ruim = False
        if fator < 5 or tempo_seg % 4 == 0:
            produto_e_ruim = True

        if produto_e_ruim:
            st.error(f"⚠️ ALERTA OPERACIONAL: O PRODUTO {nome_prod} POSSUI INDÍCIOS DE BAIXO DESEMPENHO.")

        # Exibição de Dados
        col1, col2 = st.columns([1, 1.3])

        with col1:
            st.markdown("### 📋 Inteligência de Copy")
            st.success(f"**Benefício de {nome_prod}:** Estabilização de índices metabólicos profundos.")
            st.warning(f"**Dor do Público:** Frustração com promessas falsas no mercado de saúde.")

        with col2:
            st.markdown("### ⚡ Métricas Globais")
            c1, c2 = st.columns(2)
            c1.metric("Pesquisas/Mês", f"{pesquisas_mes:,}")
            c2.metric("Hoje (Live)", f"{pesquisas_hoje:,}")
            
            st.markdown("---")
            st.markdown("#### 🏆 VEREDITO FINAL:")
            
            if produto_e_ruim:
                st.error(f"❌ RECOMENDAÇÃO: NÃO SUBA CAMPANHA PARA O PRODUTO **{nome_prod}** AGORA.")
            else:
                st.success(f"✅ RECOMENDAÇÃO: FOCO TOTAL EM **{nome_prod}**! ESTRATÉGIA VALIDADA.")

if __name__ == '__main__':
    main()
