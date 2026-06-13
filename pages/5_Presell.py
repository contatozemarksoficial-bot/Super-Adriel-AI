import streamlit as st

def extrair_dados_produto_premium(url):
    """
    Banco de dados de elite. Identifica o produto no link e injeta o frasco 
    PNG oficial recortado de fábrica e as copys reais da oferta.
    """
    url_lower = url.lower()
    
    # 🔹 BANCO DE DADOS: PROSTAVIVE
    if "prostavive" in url_lower or "provive" in url_lower:
        return {
            "nome": "Prostavive",
            "img_logo": "https://postimg.cc", # Frasco recortado real
            "img_produto": "https://postimg.cc",
            "headline_main": "Specially Designed For The Advanced Health of Prostate & Bladder Support",
            "desc": "Try Prostavive: a unique proprietary blend of nutrient strains supported by clinical research.",
            "sub": "NATURAL PROSTATE SUPPORT"
        }
    
    # 🔹 BANCO DE DADOS REGULAR: PRODENTIM (PADRÃO IGUAL AO SEU PRINT VENCEDOR)
    return {
        "nome": "ProDentim",
        "img_logo": "https://postimg.cc",
        "img_produto": "https://postimg.cc",
        "headline_main": "Specially Designed For The Health Of Your Teeth And Gums",
        "desc": "Try ProDentim: a unique blend of 3.5 billion probiotic strains and nutrients supported by clinical research.",
        "sub": "NEW ORAL PROBIOTICS"
    }

def main():
    st.markdown('<h1 style="font-size: 2.2rem; font-weight: 900; color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4);">🌐 FABRICANTE DE PRÉ-SELL SUPREME GREEN</h1>', unsafe_allow_html=True)
    st.write("Gere páginas pontes com o design profissional de agência idêntico ao seu modelo de alta conversão.")
    st.markdown("---")

    # 📥 INPUT DO AFILIADO
    link_afiliado = st.text_input("👉 Cole aqui o seu Link de Afiliado (ClickBank/Digistore/BuyGoods):", value="https://clickbank.net")
    
    # Processamento Inteligente do Banco de Dados
    dados = extrair_dados_produto_premium(link_afiliado)
    p_nome = dados["nome"]
    p_id = p_nome.replace(" ", "_").lower()

    st.write("")
    botao_gerar = st.button("⚡ CONSTRUIR PRÉ-SELL PROFISSIONAL DE AGÊNCIA")
    st.markdown("---")

    if botao_gerar and link_afiliado:
        # CÓDIGO HTML IMPECÁVEL CÓPIA EXATA DO SEU MODELO QUE VENDE
        codigo_html_supreme = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{p_nome} Official Page</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ 
            background-color: #f4f7f6; 
            font-family: 'Segoe UI', Arial, sans-serif; 
            display: flex; 
            flex-direction: column; 
            align-items: center; 
            justify-content: flex-start;
            min-height: 100vh;
        }}
        .top-banner {{ 
            background-color: #f6d14b; 
            color: #000000; 
            width: 100%; 
            text-align: center; 
            padding: 10px; 
            font-weight: 800; 
            font-size: 13.5px; 
            border-bottom: 1px solid #dcb52a; 
            letter-spacing: 0.5px;
        }}
        .header-brand {{ 
            background-color: #1a7a4a; 
            width: 100%; 
            text-align: center; 
            padding: 25px 10px 10px 10px; 
            font-size: 42px; 
            font-weight: 900; 
            color: #ffffff;
            letter-spacing: 1px; 
        }}
        .content-container {{ 
            background-color: #1a7a4a; 
            max-width: 650px; 
            width: 100%; 
            padding: 0px 25px 40px 25px; 
            text-align: center; 
        }}
        .headline-sub {{ 
            font-size: 13px; 
            font-weight: 800; 
            color: #f6d14b; 
            text-transform: uppercase; 
            margin-bottom: 8px; 
            letter-spacing: 1px; 
        }}
        .headline-main {{ 
            font-size: 15px; 
            font-weight: 700; 
            color: #ffffff; 
            margin-bottom: 25px; 
            line-height: 1.4; 
            max-width: 380px; 
            margin-left: auto; 
            margin-right: auto; 
        }}
        .img-box {{ 
            background: transparent; 
            margin-bottom: 25px; 
        }}
        .product-img {{ 
            max-width: 200px; 
            height: auto; 
            filter: drop-shadow(0 15px 25px rgba(0,0,0,0.2)); 
        }}
        .desc-text {{ 
            font-size: 13.5px; 
            color: #ffffff; 
            line-height: 1.5; 
            margin-bottom: 15px; 
            max-width: 420px; 
            margin-left: auto; 
            margin-right: auto; 
        }}
        /* LINHA DOS SELOS DA SUAFOTO (GMP, FDA, ETC) */
        .badges-row {{
            display: flex;
            justify-content: center;
            gap: 8px;
            margin-bottom: 30px;
        }}
        .badge-icon {{
            max-width: 42px;
            height: auto;
            opacity: 0.9;
        }}
        .btn-buy {{ 
            display: inline-block; 
            background-color: #f6d14b; 
            color: #000000; 
            text-decoration: none; 
            padding: 15px 55px; 
            border-radius: 35px; 
            font-weight: 900; 
            font-size: 24px; 
            transition: all 0.2s ease;
            box-shadow: 0 4px 15px rgba(246,209,75,0.3);
        }}
        .btn-buy:hover {{ 
            transform: scale(1.02); 
            box-shadow: 0 6px 20px rgba(246,209,75,0.5);
        }}
        footer {{ 
            margin-top: auto; 
            width: 100%; 
            text-align: center; 
            padding: 25px; 
            font-size: 11px; 
            color: #718096; 
            background-color: #ffffff; 
            border-top: 1px solid #e2e8f0; 
            line-height: 1.5; 
        }}
    </style>
</head>
<body>
    <div class="top-banner">⚠️ Limited Time Offer: Claim Up To 80% OFF + Free Shipping Today!</div>
    <div class="header-brand">• {p_nome} •</div>
    
    <div class="content-container">
        <div class="headline-sub">{dados["sub"]}</div>
        <div class="headline-main">{dados["headline_main"]}</div>
        
        <div class="img-box">
            <img class="product-img" src="{dados["img_produto"]}" alt="{p_nome}">
        </div>
        
        <div class="desc-text">{dados["desc"]}</div>
        
        <!-- INJEÇÃO DA GRADE DE SELOS VERIFICADOS DO SEU PRINT -->
        <div class="badges-row">
            <img class="badge-icon" src="https://postimg.cc">
            <img class="badge-icon" src="https://postimg.cc">
            <img class="badge-icon" src="https://postimg.cc">
            <img class="badge-icon" src="https://postimg.cc">
        </div>
        
        <a class="btn-buy" href="{link_afiliado}">🛒 buy now</a>
    </div>

    <footer>
        <p>Privacy Policy | Terms of Service | Disclaimer. The content of this site is for informational purposes only and is not intended to replace professional medical advice, diagnosis, or treatment. {p_nome} is a registered trademark of its respective owners.</p>
    </footer>
</body>
</html>"""

        st.markdown("### 👁️ Painel de Pré-visualização Profissional (Modelo Agência):")
        
        # Renderização idêntica de alto nível dentro da área do robô
        st.markdown(f"""
        <div style="background-color: #1a7a4a; padding: 0px 20px 35px 20px; border-radius: 8px; max-width: 460px; margin: 0 auto; text-align: center; color: white; font-family: sans-serif; box-shadow: 0 10px 25px rgba(0,0,0,0.25);">
            <div style="background-color: #f6d14b; color: black; font-weight: bold; padding: 6px; font-size: 11px; border-radius: 0 0 4px 4px; margin-bottom: 20px; text-transform: uppercase;">⚠️ Limited Time Offer: Claim Up To 80% OFF!</div>
            <h2 style="color: white !important; font-size: 36px; font-weight: 900; margin-bottom: 5px; letter-spacing:1px;">• {p_nome} •</h2>
            <p style="color: #f6d14b !important; font-weight: 800; font-size: 11px; margin-bottom: 5px; text-transform: uppercase;">{dados["sub"]}</p>
            <p style="color: white !important; font-size: 13px; font-weight: bold; margin-bottom: 20px; max-width: 320px; margin-left: auto; margin-right: auto; line-height:1.3;">{dados["headline_main"]}</p>
            <div style="margin-bottom: 20px;">
                <img src="{dados["img_produto"]}" style="max-width: 140px; filter: drop-shadow(0 10px 15px rgba(0,0,0,0.2));">
            </div>
            <p style="font-size: 12.5px; color: #ffffff !important; margin-bottom: 15px; line-height:1.4; max-width:360px; margin-left:auto; margin-right:auto;">{dados["desc"]}</p>
            
            <div style="display: flex; justify-content: center; gap: 8px; margin-bottom: 20px;">
                <span style="background: rgba(255,255,255,0.1); padding: 4px 8px; border-radius: 4px; font-size: 9px; font-weight: bold;">GMP</span>
                <span style="background: rgba(255,255,255,0.1); padding: 4px 8px; border-radius: 4px; font-size: 9px; font-weight: bold;">FDA</span>
                <span style="background: rgba(255,255,255,0.1); padding: 4px 8px; border-radius: 4px; font-size: 9px; font-weight: bold;">100% NATURAL</span>
                <span style="background: rgba(255,255,255,0.1); padding: 4px 8px; border-radius: 4px; font-size: 9px; font-weight: bold;">MADE IN USA</span>
            </div>
            
            <a href="{link_afiliado}" target="_blank" style="display: inline-block; background-color: #f6d14b; color: black !important; font-weight: 900; padding: 14px 50px; border-radius: 35px; text-decoration: none; font-size: 20px; text-transform: lowercase;">🛒 buy now</a>
        </div>
