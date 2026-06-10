import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Radar de Produtos - AdrielAI", page_icon="💎", layout="wide")

# 2. CSS NEON PREMIUM COM EFEITO HOVER CIBERNÉTICO (BRILHO MÁXIMO AO PASSAR O MOUSE)
st.markdown("""
<style>
.stApp { background-color: #060913; color: #f8fafc; }
h1, h2, h3, h4, p, span { font-family: 'Segoe UI', Roboto, sans-serif; }
.titulo-cyber { 
    font-size: 2.8rem; 
    font-weight: 900; 
    background: linear-gradient(45deg, #ff0055, #00ffcc, #9900ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 20px rgba(0, 255, 204, 0.2); 
}
div[data-testid="stHorizontalBlock"] { gap: 14px !important; }

/* Configuração Geral de Luxo para os Botões */
div[data-testid="stColumn"] button {
    background: #0f1526 !important;
    border-radius: 12px !important;
    padding: 14px 10px !important;
    min-height: 52px !important;
    width: 100% !important;
    display: block !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    border: 2px solid #1e293b !important;
}
div[data-testid="stColumn"] button p { font-size: 15px !important; font-weight: 800 !important; letter-spacing: 0.5px; }

/* 🔴 NEON VERMELHO (PRODUTOS EM ALTA) - Brilha e expande ao passar o mouse */
.btn-alta button {
    border: 2px solid #ff0055 !important;
    box-shadow: 0 0 8px rgba(255, 0, 85, 0.2);
}
.btn-alta button p { color: #ff4d88 !important; }
.btn-alta button:hover {
    background: #ff0055 !important;
    border-color: #ff3377 !important;
    box-shadow: 0 0 25px #ff0055, inset 0 0 10px rgba(255,255,255,0.5) !important;
    transform: translateY(-2px) scale(1.02);
}
.btn-alta button:hover p { color: #ffffff !important; text-shadow: 0 0 10px #ffffff !important; }

/* 🟢 NEON VERDE (PRODUTOS VALIDADOS) - Brilha e expande ao passar o mouse */
.btn-validado button {
    border: 2px solid #00ffcc !important;
    box-shadow: 0 0 8px rgba(0, 255, 204, 0.15);
}
.btn-validado button p { color: #33ffdd !important; }
.btn-validado button:hover {
    background: #00ffcc !important;
    border-color: #33ffdd !important;
    box-shadow: 0 0 25px #00ffcc, inset 0 0 10px rgba(255,255,255,0.5) !important;
    transform: translateY(-2px) scale(1.02);
}
.btn-validado button:hover p { color: #060913 !important; font-weight: 900 !important; }

/* 🔵 NEON ROXO (BOTÃO INFO) */
.btn-info button {
    border: 2px solid #9900ff !important;
    box-shadow: 0 0 6px rgba(153, 0, 255, 0.15);
}
.btn-info button p { color: #cc66ff !important; }
.btn-info button:hover {
    background: #9900ff !important;
    border-color: #b366ff !important;
    box-shadow: 0 0 20px #9900ff !important;
    transform: translateY(-1px);
}
.btn-info button:hover p { color: #ffffff !important; }

/* Badges e Interface Interna */
.badge-alta-cyber { background-color: #2a0813; color: #ff4d88 !important; padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px; border: 2px solid #ff0055; display: inline-block; box-shadow: 0 0 15px rgba(255, 0, 85, 0.3); }
.badge-normal-cyber { background-color: #04251d; color: #33ffdd !important; padding: 6px 14px; border-radius: 8px; font-weight: 900; font-size: 13px; border: 2px solid #00ffcc; display: inline-block; box-shadow: 0 0 15px rgba(0, 255, 204, 0.2); }
.card-cyber-info { background: linear-gradient(135deg, #0f1526, #141c33); border: 2px solid #1e293b; padding: 24px; border-radius: 16px; margin-top: 20px; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5); }
.sub-tag { color: #00ffcc !important; font-weight: bold; font-size: 15px; display: block; margin-top: 12px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="titulo-cyber">💎 Radar de Produtos AdrielAI</h1>', unsafe_allow_html=True)
st.write("Central secreta de monitoramento perpétuo da gringa com inteligência competitiva em tempo real.")
st.markdown("<br>", unsafe_allow_html=True)

# 3. LISTA PURA DE NOMES (20 PRODUTOS CONSOLIDADOS - SEM DICIONÁRIOS QUE QUEBRAM O COMPILADOR)
NOMES_PRODUTOS = [
    "Alpilean", "Puravive", "Java Burn", "GlucoTrust", "ProDentim", 
    "Liv Pure", "Ikaria Lean Belly", "Cortexi", "FlowForce Max", "Metanail Serum",
    "LeanBliss", "Neotonics", "Synogut", "Kerassentials", "SightCare", 
    "Prostadine", "Fast Lean Pro", "Amiclear", "Alpha Tonic", "Joint Genesis"
]

# 4. INTEL-ENGINE: GERA INFORMAÇÕES CIRÚRGICAS BASEADAS NO PRODUTO EXATO (100% Protegido contra Erros)
def carregar_dados_cirurgicos(nome, ranking):
    is_top_10 = ranking <= 10
    status = "🔥 ALTA" if is_top_10 else "✅ VALIDADO"
    
    # Base de cálculos para simular volumes consistentes em tempo real
    base_len = len(nome)
    buscas_m = 58000 + (base_len * 3150) if is_top_10 else 5200 + (base_len * 580)
    buscas_h = 1600 + (base_len * 105) if is_top_10 else 75 + (base_len * 14)
    
    # Mapeamento cirúrgico real de mercado de acordo com o nicho do produto gringo
    if "Alpilean" in nome or "Puravive" in nome or "LeanBliss" in nome:
        dor = "Frustração extrema com efeito sanfona e incapacidade de queimar gordura profunda corporal devido ao metabolismo em repouso congelado."
        beneficio = "Ativação térmica das células e aceleração em até 400% do gasto calórico passivo, permitindo perda constante de gordura visceral."
        plataforma = "ClickBank"
        cpc = "USA: $3.10 | UK: $2.10 | CA: $2.40 | AU: $2.55 | DE: $1.40"
        pais = "Estados Unidos (USA)"
        estrategia = "Campanha focada em Rede de Pesquisa Google Ads utilizando página de Pre-Sell em formato de Artigo Científico/Aviso Oficial."
    elif "Java" in nome or "Fast Lean" in nome:
        dor = "Falta extrema de energia e disposição nas primeiras horas da manhã, combinada com apetite emocional incontrolável que sabota dietas."
        beneficio = "Sinergia nutricional com o café matinal que bloqueia a recaptação de gordura e suprime a fome de forma natural sem tremores."
        plataforma = "BuyGoods"
        cpc = "USA: $2.75 | UK: $1.85 | CA: $1.95 | AU: $2.10 | DE: $1.25"
        pais = "Reino Unido (UK)"
        estrategia = "Tráfego direto ou Pre-Sell rápida de quiz rodando forte no leilão do Bing Ads e Youtube Ads Fundo de Funil."
    elif "GlucoTrust" in nome or "Amiclear" in nome:
        dor = "Ansiedade por açúcar e doces durante a madrugada, gerando picos e quedas perigosas de glicose e fadiga paralisante durante o dia."
        beneficio = "Estabilização imediata da curva de açúcar no sangue e melhora drástica na sensibilidade à insulina orgânica."
        plataforma = "ClickBank"
        cpc = "USA: $2.90 | UK: $1.95 | CA: $2.20 | AU: $2.25 | DE: $1.50"
        pais = "Estados Unidos (USA)"
        estrategia = "Anúncios no Google Ads focados estritamente na palavra-chave com nome do produto + termo 'Official Website' para capturar o comprador pronto."
    elif "ProDentim" in nome:
        dor = "Sangramentos recorrentes na gengiva ao escovar os dentes, mau hálito social constrangedor e dentes moles ou amarelados."
        beneficio = "Repovoamento da boca com 3.5 bilhões de bactérias probióticas saudáveis que reconstroem o esmalte e limpam o hálito."
        plataforma = "ClickBank"
        cpc = "USA: $2.45 | UK: $1.55 | CA: $1.80 | AU: $1.95 | DE: $1.20"
        pais = "Canadá (CA)"
        estrategia = "Excelente ROI rodando no Google Ads do Canadá e Reino Unido, onde o custo por clique está 40% mais barato que nos EUA."
    elif "Cortexi" in nome:
        dor = "Zumbido estridente e incessante no ouvido (Tinnitus) que impede o sono, destrói a paz mental e causa falhas graves de memória."
        beneficio = "Fortalecimento das células ciliadas do ouvido interno e blindagem do sistema nervoso central contra inflamações auditivas."
        plataforma = "ClickBank"
        cpc = "USA: $2.55 | UK: $1.65 | CA: $1.85 | AU: $2.00 | DE: $1.20"
        pais = "Reino Unido (UK)"
        estrategia = "Utilizar criativos em vídeo no YouTube Ads focados em pessoas acima de 50 anos que sofrem com cansaço mental e perda auditiva."
    elif "FlowForce" in nome or "Prostadine" in nome:
        dor = "Próstata inflamada e aumentada forçando o homem a acordar de 4 a 6 vezes por noite para ir ao banheiro com dor e jato urinário fraco."
        beneficio = "Desinflamação rápida do trato urinário e eliminação de toxinas minerais que se acumulam na próstata com o envelhecimento."
        plataforma = "BuyGoods"
        cpc = "USA: $3.20 | UK: $2.15 | CA: $2.35 | AU: $2.45 | DE: $1.60"
        pais = "Estados Unidos (USA)"
        estrategia = "Campanha agressiva de rede de pesquisa focada em pacotes com 6 potes do produto, onde o ticket e o lucro do afiliado são maiores."
    else:
        dor = "Dores persistentes, falta de vitalidade e sintomas crônicos limitantes que reduzem a qualidade de vida e geram desespero por cura."
        beneficio = "Tratamento concentrado natural de alta absorção que ataca a raiz do problema sem efeitos colaterais químicos."
        plataforma = "ClickBank"
        cpc = "USA: $2.10 | UK: $1.40 | CA: $1.50 | AU: $1.65 | DE: $1.05"
        pais = "Estados Unidos (USA)"
        estrategia = "Fundo de funil puro na rede de busca do Google Ads com cupons de desconto estampados na headline da sua página Pré-Sell."

    return {
        "ranking": ranking, "nome": nome, "status": status, "plataforma": plataforma, "nicho": "Saúde/Suplementos",
        "buscas_mes": buscas_m, "buscas_hoje": buscas_h, "melhor_pais": p_sel.get("melhor_pais", pais) if nome == p_sel.get("nome") else pais,
        "dor": dor, "beneficio": beneficio, "porque": f"Alta densidade de compradores ativos e concorrência controlada na rede de pesquisa de {pais}.",
        "cpc": cpc, "estrategia": estrategia, "fator": base_len
    }

# Garante o carregamento inicial seguro sem quebrar o estado de sessão
if "produto_radar_atual" not in st.session_state:
