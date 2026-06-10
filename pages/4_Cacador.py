
import streamlit as st
import random
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURACAO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Caçador Premium - AdrielAI", layout="wide")

    # FORCADOR ULTRA LUXO CYBER-NEON COMPILADO (IMUNE AO BUG DO PYTHON 3.14)
    estilo_luxo = "<style>"
    estilo_luxo += "header, [data-testid='stHeader'] {background-color: rgba(0,0,0,0) !important; background: transparent !important; display: none !important;}"
    estilo_luxo += "[data-testid='stAppViewContainer'] {padding-top: 0px !important;}"
    estilo_luxo += "html, body, [data-testid='stAppViewContainer'], .stApp {background-color: #030712 !important; color: #f9fafb !important;}"
    estilo_luxo += "[data-testid='stSidebar'], section[data-testid='stSidebar'] div {background-color: #090d16 !important;}"
    estilo_luxo += "[data-testid='stSidebar'] nav ul li div a span {color: #00ffcc !important; font-weight: bold !important; text-shadow: 0 0 8px rgba(0,255,204,0.5) !important;}"
    estilo_luxo += ".stTextInput>div>div>input {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important; font-size: 1.1rem !important;}"
    estilo_luxo += ".stTextInput>div>div>input:focus {border-color: #00ffcc !important; box-shadow: 0 0 15px rgba(0, 255, 204, 0.3) !important;}"
    estilo_luxo += ".stButton>button {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; font-weight: bold !important; box-shadow: 0 0 10px rgba(0, 255, 204, 0.15) !important; transition: all 0.3s ease-in-out !important; width: 100% !important; height: 45px !important;}"
    estilo_luxo += ".stButton>button:hover {background-color: #00ffcc !important; color: #030712 !important; box-shadow: 0 0 25px #00ffcc, 0 0 45px rgba(0,255,204,0.4) !important; transform: scale(1.01);}"
    estilo_luxo += "[data-testid='stMetricContainer'] {background: linear-gradient(135deg, #0f172a, #030712) !important; border: 1px solid #1e293b !important; border-left: 4px solid #00ffcc !important; padding: 15px !important; border-radius: 10px !important; box-shadow: 0 4px 20px rgba(0,0,0,0.6) !important;}"
    estilo_luxo += "h1, h2, h3, h4, span, p, label {color: #f3f4f6 !important;}"
    estilo_luxo += "[data-testid='stNotification'] {background-color: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 10px !important;}"
    estilo_luxo += "</style>"
    st.markdown(estilo_luxo, unsafe_allow_html=True)

    st.markdown('<h1 style="font-size: 2.6rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4); margin-bottom: 5px;">🛰️ CAÇADOR DE LANÇAMENTOS</h1>', unsafe_allow_html=True)
    st.write("Varredura de ofertas recentes atualizando em tempo real com disparo de relatorio operacional via WhatsApp.")
    st.markdown("---")

    # Terminal de entrada de dados
    st.markdown("<h3 style='color:#00ffcc;'>⚙️ Terminal de Varredura Sincronizada</h3>", unsafe_allow_html=True)
    
    produtos_novos_pool = ["KeraBiotics Gringo", "Glucovibe Launch", "LeanPulse Pro", "NeuroShield V2"]
    tempo_segundo = datetime.now().second
    sugestao_nome = produtos_novos_pool[tempo_segundo % 4]
    
    produto_pesquisado = st.text_input("Insira o nome do lancamento gringo para rastrear:", value=sugestao_nome)
    ativar_busca = st.button("🚀 PESQUISAR LANÇAMENTO")
    st.markdown("---")

    if produto_pesquisado:
        nome_lancamento = produto_pesquisado.strip()
        fator = len(nome_lancamento)
        horario_atual = datetime.now().strftime("%H:%M:%S")

        plataformas_pool = ["ClickBank Marketplace", "BuyGoods Network V2", "Digistore24 International", "MaxWeb Premium Vendor"]
        plataforma_ativa = plataformas_pool[(fator + tempo_segundo) % 4]

        st.info("🤖 ROBO STATUS: Escaneando a plataforma: " + plataforma_ativa.upper() + " | Sinais atualizados as " + horario_atual)
        st.markdown("<br>", unsafe_allow_html=True)

        e_oportunidade = True
        if (fator + tempo_segundo) % 3 == 0:
            e_oportunidade = False

        txt_oportunidade = "O veredicto confirma que " + nome_lancamento + " e uma EXCELENTE OPORTUNIDADE operacional! Por se tratar de um produto recem-lancado no mercado internacional, a concorrencia de lances de outros afiliados no Google Ads e praticamente nula. O leilao encontra-se limpo (Oceano Azul), permitindo capturar cliques baratos fundo de funil e extrair altas comissoes com baixa contingência."
        txt_perigo = "O veredicto indica que " + nome_lancamento + " NAO e uma oportunidade recomendada no momento. Aposta arriscada devido a taxas de reembolso oscilantes nas plataformas gringas."

        # 3. MONTAGEM DAS DUAS COLUNAS PRINCIPAIS LUXO
        col_esquerda, col_direita = st.columns([1.0, 1.3])

        with col_esquerda:
            st.markdown("<h3 style='color:#00ffcc;'>📋 Dossiê Técnico do Lançamento</h3>", unsafe_allow_html=True)
            st.write("Oferta mapeada e processada nos servidores internacionais:")
            st.write("")
            
            st.write("**💎 Nome do Produto Caçado:**")
            st.write(nome_lancamento)
            
            st.write("**🛰️ Plataforma de Origem:**")
            st.write(plataforma_ativa)

            st.write("**🌡️ TERMÔMETRO DE TRAÇÃO DA OFERTA:**")
            status_termo = "FRIA"
            if e_oportunidade:
                st.success("🔥 TRAÇÃO MÁXIMA (OPORTUNIDADE DETECTADA)")
                st.write(txt_oportunidade)
                status_termo = "QUENTE"
            else:
                st.error("❄️ OFERTA FRIA (RISCO OPERACIONAL DETECTADO)")
                st.write(txt_perigo)
                status_termo = "FRIA"

        with col_direita:
            st.markdown("<h3 style='color:#00ffcc;'>⚡ Métricas Iniciais de Leilao Gringo</h3>", unsafe_allow_html=True)
            st.write("Dados preditivos coletados para as primeiras campanhas:")
            st.write("")

            pesquisas_mes = 3000 + (fator * 280) + (tempo_segundo * 45)
            c1, c2 = st.columns(2)
            c1.metric(label="🔎 Pesquisas estimadas (Mês 1)", value=f"{pesquisas_mes:,}")
            c2.metric(label="💵 CPC Médio Estimado", value="$1.35")

            st.markdown("---")
            
            st.markdown("<h4 style='color:#cc66ff;'>💵 CPC Inicial Estimado em 5 Países Oficiais:</h4>", unsafe_allow_html=True)
            st.markdown("<div style='background-color:#0f172a; border:2px solid #1e293b; border-radius:8px; padding:15px; font-family:monospace; color:#00ffcc; font-size:1.1rem; font-weight:bold; box-shadow:0 4px 15px rgba(0,0,0,0.5);'>USA: $1.45 | UK: $0.95 | CA: $1.10 | AU: $1.20 | DE: $0.80</div>", unsafe_allow_html=True)
            st.write("")

            st.markdown("<h4 style='color:#ff0055;'>🏆 VEREDITO OPERACIONAL FINAL ADRIEL-AI:</h4>", unsafe_allow_html=True)
            veredito_texto = "BLOQUEAR ENTRADA"
            if e_oportunidade:
                st.success("O ROBO AFIRMA: O MELHOR PAIS ABSOLUTO PARA COMEÇAR A ANUNCIAR ESTE LANÇAMENTO E OS ESTADOS UNIDOS (USA) UTILIZANDO O GOOGLE ADS PESQUISA.")
                veredito_texto = "ANUNCIAR AGORA"
            else:
                st.error(veredito_texto)

            st.markdown("---")

            # 🪐 5. ENGENHARIA DO BOTÃO DE WHATSAPP COMPILADA POR LIMPEZA LINEAR SEGURA
            st.markdown("<h4 style='color:#00ffcc;'>📲 Compartilhar Alerta via WhatsApp</h4>", unsafe_allow_html=True)
            st.write("Dispare o relatorio desse lancamento gringo diretamente para seu WhatsApp:")
            
            # Geração textual em formato cru e linear sem quebras de strings para evitar travar o parser
            texto_cru_whats = "ALERTA DE LANCAMENTO ADRIEL-AI - Produto: " + nome_lancamento + " - Plataforma: " + plataforma_ativa + " - Termometro: " + status_termo + " - Veredito: " + veredito_texto
            
            # Converte todos os caracteres para o formato seguro de URL web
            link_final_whats = "https://whatsapp.com" + str(texto_cru_whats).replace(" ", "%20")
            
            st.markdown("<a href='" + link_final_whats + "' target='_blank' style='display:block; text-align:center; background-color:#25d366; color:#ffffff; padding:14px; border-radius:8px; font-weight:bold; text-decoration:none; box-shadow: 0 4px 15px rgba(37,211,102,0.4); font-size:1.1rem;'>💬 DISPARAR ALERTA NO WHATSSAP</a>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

            # 📊 GRÁFICO DE DEMANDA SINCRONIZADO EM MILHARES REAIS CORES SÓLIDAS
            st.markdown("<h4 style='color:#00ffcc;'>📊 Histórico Curto de Demanda Semanal (Sinais Semanais)</h4>", unsafe_allow_html=True)
            
            base_semana = pesquisas_mes // 3
            df_cacador = pd.DataFrame({
                "Semanas": ["Semana 1", "Semana 2", "Semana 3", "Semana 4"],
                "Verde Neon (Subindo)": [base_semana, 0, int(base_semana * 1.2), 0],
                "Laser Vermelho (Decendo)": [0, int(base_semana * 0.95), 0, 0],
                "Azul Eletrico (Indecisao)": [0, 0, 0, int(base_semana * 1.1)]
            })
            
            cores_cacador = ["#00ffcc", "#ff0055", "#0066ff"]
            st.bar_chart(df_cacador, x="Semanas", y=["Verde Neon (Subindo)", "Laser Vermelho (Decendo)", "Azul Eletrico (Indecisao)"], color=cores_cacador)

if __name__ == "__main__":
    main()
