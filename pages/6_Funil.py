import streamlit as st
import random
import pandas as pd
from datetime import datetime

def main():
    # 1. CONFIGURACAO PREMIUM DA INTERFACE SAAS 2026
    st.set_page_config(page_title="Arquiteto de Funil - AdrielAI", layout="wide")

    # FORCADOR ULTRA LUXO CYBER-NEON COMPILADO (IMUNE AO BUG DO PYTHON 3.14)
    estilo_luxo = "<style>"
    estilo_luxo += "header, [data-testid='stHeader'] {background-color: rgba(0,0,0,0) !important; background: transparent !important; display: none !important;}"
    estilo_luxo += "[data-testid='stAppViewContainer'] {padding-top: 0px !important;}"
    estilo_luxo += "html, body, [data-testid='stAppViewContainer'], .stApp {background-color: #030712 !important; color: #f9fafb !important;}"
    estilo_luxo += "[data-testid='stSidebar'], section[data-testid='stSidebar'] div {background-color: #090d16 !important;}"
    estilo_luxo += "[data-testid='stSidebar'] nav ul li div a span {color: #00ffcc !important; font-weight: bold !important; text-shadow: 0 0 8px rgba(0,255,204,0.5) !important;}"
    estilo_luxo += ".stTextInput>div>div>input {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #1e293b !important; border-radius: 8px !important; font-size: 1.1rem !important;}"
    estilo_luxo += ".stTextInput>div>div>input:focus {border-color: #00ffcc !important; box-shadow: 0 0 15px rgba(0,255,204,0.3) !important;}"
    estilo_luxo += ".stButton>button {background-color: #0f172a !important; color: #00ffcc !important; border: 2px solid #00ffcc !important; border-radius: 8px !important; font-weight: bold !important; box-shadow: 0 0 10px rgba(0,255,204,0.15) !important; transition: all 0.3s ease-in-out !important; width: 100% !important; height: 45px !important;}"
    estilo_luxo += ".stButton>button:hover {background-color: #00ffcc !important; color: #030712 !important; box-shadow: 0 0 25px #00ffcc, 0 0 45px rgba(0,255,204,0.4) !important; transform: scale(1.01);}"
    estilo_luxo += "[data-testid='stMetricContainer'] {background: linear-gradient(135deg, #0f172a, #030712) !important; border: 1px solid #1e293b !important; border-left: 4px solid #00ffcc !important; padding: 15px !important; border-radius: 10px !important; box-shadow: 0 4px 20px rgba(0,0,0,0.6) !important;}"
    estilo_luxo += "h1, h2, h3, h4, span, p, label, .stMarkdown p {color: #f3f4f6 !important;}"
    estilo_luxo += "[data-testid='stNotification'] {background-color: #0f172a !important; border: 1px solid #1e293b !important; border-radius: 10px !important;}"
    
    # CUSTOMIZAÇÃO E ANULAÇÃO DE FUNDO BRANCO NOS GRÁFICOS (FIXAÇÃO DARK LUXO)
    estilo_luxo += "div[data-testid='stVegaLiteChart'], .stVegaLiteChart {background-color: rgba(0,0,0,0) !important; background: transparent !important; border: 1px solid #1e293b !important; padding: 10px !important; border-radius: 8px !important;}"
    estilo_luxo += "svg, canvas, g, path, rect {background-color: transparent !important; background: transparent !important;}"
    estilo_luxo += "text, span {fill: #f3f4f6 !important; color: #f3f4f6 !important; font-family: monospace !important;}"
    estilo_luxo += "</style>"
    st.markdown(estilo_luxo, unsafe_allow_html=True)

    st.markdown('<h1 style="font-size: 2.6rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4); margin-bottom: 5px;">📐 ARQUITETO DE FUNIL INTELIGENTE</h1>', unsafe_allow_html=True)
    st.write("Mapeador de intencao de busca. Analise se a sua oferta e Topo, Meio ou Fundo de Funil e capture a melhor estrategia gringa.")
    st.markdown("---")

    # 2. CENTRAL DE ENTRADA DO PRODUTO E ANÁLISE DE INTENÇÃO
    st.markdown("<h3 style='color:#00ffcc;'>🔍 Scanner de Intencao do Produto</h3>", unsafe_allow_html=True)
    
    # Pool dinâmico para sugestões inteligentes na caixa de texto
    sugestoes_pool = ["FitSpresso", "Weight Loss Supplement", "How to lose weight fast"]
    semente_tempo = datetime.now().second
    sugestao_ativa = sugestoes_pool[semente_tempo % 3]

    produto_analisado = st.text_input("Insira o Nome do Produto, Beneficio ou Termo que deseja anunciar:", value=sugestao_ativa)
    
    col_in1, col_in2, col_in3 = st.columns(3)
    with col_in1:
        orcamento = st.number_input("Orcamento diario estimado (USD):", min_value=10.0, value=50.0, step=5.0)
    with col_in2:
        cpc_medio = st.number_input("CPC Medio do Leilao (USD):", min_value=0.1, value=1.20, step=0.1)
    with col_in3:
        comissao_produto = st.number_input("Comissao da Oferta (USD):", min_value=10.0, value=135.0, step=5.0)

    ativar_analise = st.button("⚡ ANALISAR INTENÇÃO E MODELAR FUNIL")
    st.markdown("---")

    # 3. ENGINE MATEMÁTICO DE CLASSIFICAÇÃO E MODELAGEM DE ESTRATÉGIA
    termo_limpo = produto_analisado.strip().lower()
    
    # Dicionário estrito de classificação de níveis de funil
    nivel_funil = "FUNDO DE FUNIL (Marca Exata)"
    cor_alerta = "green"
    txt_estrategia = "ESTRATÉGIA DO ROBÓ AFILIADO ELITE: O leilao para este termo e cirurgico! Como o lead esta buscando pelo nome exato do produto, a intencao de compra e maxima (fundo de funil). Use correspondencia de frase ou exata no Google Ads, crie uma estrutura de Pre-Sell direta de alta velocidade e foque em cliques qualificados. Concorrencia forte mas com altissima taxa de conversao imediata."
    cor_grafico = "#00ffcc" # Verde Neon para Fundo de Funil
    
    # Análise de padrões para Meio de Funil (Buscando solução/categoria do produto)
    if "supplement" in termo_limpo or "tonic" in termo_limpo or "remedy" in termo_limpo or "juice" in termo_limpo or "pills" in termo_limpo or "diet" in termo_limpo:
        nivel_funil = "MEIO DE FUNIL (Solucao / Categoria)"
        cor_alerta = "blue"
        txt_estrategia = "ESTRATÉGIA DO ROBÓ AFILIADO ELITE: O lead sabe o que precisa (um suplemento, tonico ou capsula) mas ainda nao escolheu a marca. Voce deve usar uma Pre-Sell robusta do tipo 'Advertorial' ou comparativa (Top 3) para educar o lead antes de envia-lo para a oferta. CPC moderado e leilao mais amplo."
        cor_grafico = "#0066ff" # Azul Elétrico para Meio de Funil

    # Análise de padrões para Topo de Funil (Buscando sintoma ou dor genérica)
    if "how to" in termo_limpo or "lose" in termo_limpo or "cure" in termo_limpo or "fast" in termo_limpo or "ways to" in termo_limpo or "treatment" in termo_limpo:
        nivel_funil = "TOPO DE FUNIL (Sintoma / Nicho Amplo)"
        cor_alerta = "red"
        txt_estrategia = "ESTRATÉGIA DO ROBÓ AFILIADO ELITE: Intencao de descoberta! O lead possui uma dor (quer emagrecer ou tratar um sintoma) mas nao conhece nenhuma solucao comercial. Nao mande direto para a Pre-Sell de afiliado! Use paginas de captura (Nurturing), entregue uma isca digital gringa ou capture o e-mail para vender na sequencia. Cliques baratos mas exigem funil longo."
        cor_grafico = "#ff0055" # Laser Vermelho para Topo de Funil

    num_whats = st.session_state.get("user_whatsapp_saved", "5511999999999")
    horario_atual = datetime.now().strftime("%H:%M:%S")

    # Simulação de tráfego dinâmica baseada no nível identificado
    cliques_estimados = int(orcamento / cpc_medio)
    visitas_oferta = int(cliques_estimados * 0.38)
    vendas_estimadas = int(visitas_oferta * 0.028)
    
    if vendas_estimadas < 1:
        vendas_estimadas = 1
        
    faturamento_bruto = vendas_estimadas * comissao_produto
    lucro_liquido = faturamento_bruto - orcamento
    roi_porcentagem = round((lucro_liquido / orcamento) * 100, 2)

    # 4. EXIBIÇÃO DO VEREDITO INTELIGENTE DA OFERTA
    st.markdown("<h3 style='color:#00ffcc;'>🛰️ Diagnostico Estrategico Adriel-AI</h3>", unsafe_allow_html=True)
    
    if cor_alerta == "green":
        st.success("🎯 CLASSIFICAÇÃO DETECTADA: " + nivel_funil)
    elif cor_alerta == "blue":
        st.info("🛰️ CLASSIFICAÇÃO DETECTADA: " + nivel_funil)
    else:
        st.error("❄️ CLASSIFICAÇÃO DETECTADA: " + nivel_funil)
        
    st.write(txt_estrategia)
    st.markdown("<br>", unsafe_allow_html=True)

    # 5. QUADRO DE CRONOGRAMA E GRÁFICOS DO FUNIL
    c_etapa1, c_etapa2, c_etapa3 = st.columns(3)
    lista_dias = ["D1", "D2", "D3", "D4"]
    
    with c_etapa1:
        st.subheader("📊 Volume de Cliques")
        st.write("Previsao de acessos gerados na campanha:")
        st.metric(label="🔎 Cliques Totais (Dia)", value=f"{cliques_estimados:,}")
        
        df_g1 = pd.DataFrame({"Dias": lista_dias, "Cliques": [cliques_estimados, int(cliques_estimados*1.08), int(cliques_estimados*0.92), int(cliques_estimados*1.15)]})
        st.bar_chart(df_g1, x="Dias", y="Cliques", color=cor_grafico)

    with c_etapa2:
        st.subheader("🛡️ Retencao da Estrutura")
        st.write("Leads filtrados e aquecidos pela pagina:")
        st.metric(label="🛰️ Visitas na Oferta (Dia)", value=f"{visitas_oferta:,}")
        
        df_g2 = pd.DataFrame({"Dias": lista_dias, "Visitas": [visitas_oferta, int(visitas_oferta*1.1), int(visitas_oferta*0.88), int(visitas_oferta*1.12)]})
        st.bar_chart(df_g2, x="Dias", y="Visitas", color=cor_grafico)

    with c_etapa3:
        st.subheader("💵 Lucratividade Liquida")
        st.write("Retorno financeiro limpo estimado das campanhas:")
        st.metric(label="🏆 Lucro Liquido (Dia)", value=f"${lucro_liquido:,.2f}")
        
        df_g3 = pd.DataFrame({"Dias": lista_dias, "Lucro": [lucro_liquido, int(lucro_liquido*1.14), int(lucro_liquido*0.9), int(lucro_liquido*1.2)]})
        st.bar_chart(df_g3, x="Dias", y="Lucro", color=cor_grafico)

    st.markdown("---")

    # 6. ENVIAR MODELAGEM E VEREDITO OPERACIONAL PARA O WHATSAPP
    st.markdown("<h4 style='color:#00ffcc;'>📲 Compartilhar Diagnostico do Funil no WhatsApp</h4>", unsafe_allow_html=True)
    st.write("Envie este relatorio completo de nivel de funil e estrategia direto para o seu telefone salvo:")
    
    # Montagem linear pura de string sem quebras sintáticas
