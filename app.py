import streamlit as st
import pandas as pd

# --- CONFIGURAÇÃO E DESIGN ARQUETÍPICO ---
st.set_page_config(page_title="Bella Lola - O Despertar do Guerreiro", layout="centered")

# Cores Outonais Profissionais
C_GOLD = "#b87333"
C_TAN = "#d2b48c"
C_DARK = "#331811"
C_RED = "#8b3a3a"

st.markdown(f"""
    <style>
    .stApp {{ background-color: {C_DARK}; color: white; font-family: 'Georgia', serif; }}
    .main-title {{ text-align: center; color: {C_GOLD}; font-size: 35px; font-weight: bold; text-shadow: 2px 2px 4px #000; }}
    .sub-title {{ text-align: center; color: {C_TAN}; letter-spacing: 2px; font-size: 14px; margin-top: -10px; font-style: italic; }}
    .stButton>button {{ width: 100%; border-radius: 20px; background-color: {C_RED}; color: white; border: 1px solid {C_GOLD}; font-weight: bold; transition: 0.3s; }}
    .stButton>button:hover {{ background-color: {C_GOLD}; color: {C_DARK}; transform: scale(1.02); }}
    .metric-card {{ background: rgba(255,255,255,0.05); padding: 15px; border-radius: 15px; border-left: 5px solid {C_GOLD}; }}
    div[data-testid="column"] {{ width: 14% !important; min-width: 45px !important; flex: 1 1 0% !important; padding: 2px !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- ESTADOS DA SESSÃO ---
if 'autenticado' not in st.session_state: st.session_state.autenticado = False
if 'pesagem' not in st.session_state: st.session_state.pesagem = []
if 'progresso' not in st.session_state: st.session_state.progresso = [False] * 21

# --- ACESSO ---
if not st.session_state.autenticado:
    st.markdown("<h1 class='main-title'>BELLA LOLA FITNESS</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>ALQUIMIA TRANSFORMAÇÃO & DOMÍNIO MENTAL</p>", unsafe_allow_html=True)
    # IMAGEM SUBLIMINAR NO LOGIN (Foco e Poder)
    st.image("https://images.unsplash.com", caption="VISUALIZE SUA VITÓRIA")
    
    senha = st.text_input("Chave do Portal:", type="password")
    if st.button("REIVINDICAR MEU PODER", key="login"):
        if senha == "ALQUIMIA2024":
            st.session_state.autenticado = True
            st.rerun()
        else: st.error("A frequência da chave está incorreta.")
    st.stop()
with tab5:
    st.subheader("🧬 Simulador de Metamorfose")
    
    # Entrada de dados para o gráfico
    novo_p = st.number_input("Registre seu peso de hoje (kg):", value=p, step=0.1, key="input_evolucao")
    
    col_foto, col_info = st.columns([1, 2])
    
    with col_info:
        if st.button("💾 SALVAR PESAGEM SEMANAL"):
            st.session_state.pesagem.append(novo_p)
            st.success("Registro gravado no seu Codex!")
        
        if st.session_state.pesagem:
            st.line_chart(st.session_state.pesagem)
            st.caption("Sua jornada em queda constante.")

    # --- LÓGICA DO BONECO DE TRANSFORMAÇÃO ---
    with col_foto:
        # Calculamos o progresso atual baseado no peso inicial e atual
        if p > 0 and a > 0:
            imc_atual = p / (a**2)
            
            # Escolha da imagem baseada no IMC (Simbolismo do Guerreiro)
            if imc_atual > 30:
                # Estágio: Armadura Pesada (Início)
                img_boneco = "https://cdn-icons-png.flaticon.com" 
                txt_status = "🛡️ FASE: ARMADURA PESADA"
            elif 25 <= imc_atual <= 29.9:
                # Estágio: Soldado em Treino
                img_boneco = "https://cdn-icons-png.flaticon.com"
                txt_status = "⚔️ FASE: GUERREIRO AGUERRIDO"
            else:
                # Estágio: Mestre da Agilidade (Meta)
                img_boneco = "https://cdn-icons-png.flaticon.com"
                txt_status = "💎 FASE: MESTRE ALQUIMISTA"

            st.image(img_boneco, width=120)
            st.markdown(f"<p style='text-align:center; color:{C_GOLD}; font-size:12px;'><b>{txt_status}</b></p>", unsafe_allow_html=True)
            
    # Mensagem de Incentivo Personalizada
    if len(st.session_state.pesagem) > 1:
        perda_total = st.session_state.pesagem[0] - st.session_state.pesagem[-1]
        if perda_total > 0:
            st.balloons()
            st.success(f"🏆 Você já transmutou **{perda_total:.1f}kg** de gordura em poder!")
        else:
            st.info("🔥 A constância é a chave. Mantenha o foco no protocolo!")
