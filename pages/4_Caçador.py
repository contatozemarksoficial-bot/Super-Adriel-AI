import streamlit as st
import random
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURAÇÃO DE PÁGINA LUXO
    st.set_page_config(page_title="Radar Premium - AdrielAI", layout="wide")

    # CSS PARA TEMA DARK TOTAL E REMOÇÃO DE FAIXAS BRANCAS
    st.markdown("""
    <style>
    /* Fundo total e lateral */
    [data-testid="stSidebar"], .stApp, [data-testid="stAppViewContainer"] {
        background-color: #030712 !important;
        color: #f9fafb !important;
    }
    /* Estilo dos botões do menu lateral */
    .stSidebar .stButton>button {
        background: transparent !important;
        color: #94a3b8 !important;
        border: none !important;
        text-align: left !important;
        font-size: 1rem !important;
    }
    .stSidebar .stButton>button:hover {
        color: #00ffcc !important;
        background: rgba(0, 255, 204, 0.05) !important;
    }
    /* Estilo dos Botões de Seleção de Produto (Painel Estatístico) */
    .btn-produto > button {
        background: #030712 !important;
        color: #f3f4f6 !important;
        border: 1px solid #00ffcc !important;
        border-radius: 8px !important;
        margin-bottom: 10px !important;
        width: 100% !important;
        height: 50px !important;
        font-size: 0.9rem !important;
    }
    .btn-produto > button:hover {
        background: rgba(0, 255, 204, 0.1) !important;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.3) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # --- BARRA LATERAL (MENU DE MÓDULOS) ---
    with st.sidebar:
        st.markdown("<br><br>", unsafe_allow_html=True)
        modulos = ["app", "Radar", "Auditor", "Gerador", "Caçador", "Presell", "Funil", "Assinantes"]
        for mod in modulos:
            st.button(mod)

    # --- CONTEÚDO PRINCIPAL ---
    st.markdown('<h1 style="color: #f9fafb; font-size: 2.2rem;">💎 RADAR DE PRODUTOS PERPÉTUOS</h1>', unsafe_allow_html=True)
    st.write("Varredura automatizada e mapeamento operacional de ofertas de alta tração nas plataformas gringas.")
    horario_agora = datetime.now().strftime("%H:%M:%S")
    st.write(f"Sistemas operando em Modo de Guerra. Varredura ativa às {horario_agora}")
    
    st.markdown("---")

    # Layout de Duas Colunas Principal
    col_lista, col_detalhes = st.columns([1, 1.2])

    with col_lista:
        st.markdown("<h3 style='color:#f9fafb;'>🎯 Painel Estatístico Global</h3>", unsafe_allow_html=True)
        st.write("Selecione o produto abaixo para ativar os sinais:")
        
        # Lista de produtos com status
        produtos = [
            {"n": "Alpilean", "s": "🔥 ALTA - 📉 DESCENDO", "c": "#00ffcc"},
            {"n": "Puravive", "s": "🔥 ALTA - 📈 SUBINDO", "c": "#00ffcc"},
            {"n": "Java Burn", "s": "🔥 ALTA - 📉 DESCENDO", "c": "#00ffcc"},
            {"n": "GlucoTrust", "s": "🔥 ALTA - 📈 SUBINDO", "c": "#00ffcc"},
            {"n": "ProDentim", "s": "🔥 ALTA - 📉 DESCENDO", "c": "#00ffcc"},
            {"n": "Liv Pure", "s": "🔥 ALTA - 📈 SUBINDO", "c": "#00ffcc"}
        ]

        # Criar os botões de seleção (painel da esquerda)
        selecionado = produtos[0] # Padrão
        for p in produtos:
            if st.button(f"{p['n']} [ {p['s']} ]", key=p['n'], help=f"Ver detalhes de {p['n']}", use_container_width=True):
                selecionado = p

    with col_detalhes:
        # Título do Produto Selecionado
        st.markdown(f"<h1 style='color:#f9fafb; margin-bottom:0;'>⚡ {selecionado['n']}</h1>", unsafe_allow_html=True)
        st.write(f"Classificação: {selecionado['s'].split('-')[0]} - MONITORAMENTO ATIVO")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Gráfico de Tendência (Volume)
        st.markdown("📈 **Volume de pesquisas nos últimos dias:**")
        volume_fake = random.randint(45000, 65000)
        st.markdown(f"<h2 style='color:#00ffcc;'>{volume_fake:,}</h2>", unsafe_allow_html=True)
        
        df = pd.DataFrame({"Buscas": [random.randint(30, 100) for _ in range(5)]})
        st.bar_chart(df, height=200)

        # Veredito Psicológico
        st.markdown("<h3 style='color:#00ffcc;'>❤️ Veredito Psicológico Gringo:</h3>", unsafe_allow_html=True)
        st.write("Frustração emocional profunda e busca por soluções biológicas associadas ao bem-estar imediato.")
        
        st.markdown("---")
        
        # Área de WhatsApp
        st.markdown("**Notificação de Oportunidade:**")
        zap = st.text_input("WhatsApp para alertas:", placeholder="Ex: 5511999999999")
        if st.button("🚀 ENVIAR ANÁLISE COMPLETA"):
            if zap:
                st.success(f"Dossiê de {selecionado['n']} enviado para {zap}!")
            else:
                st.warning("Insira o número do WhatsApp.")

if __name__ == "__main__":
    main()
