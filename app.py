import streamlit as st

# --- CONFIGURAÇÃO VISUAL BELLA LOLA (CORES DA IMAGEM) ---
st.set_page_config(page_title="Bella Lola Fitness - Premium", page_icon="🍂", layout="centered")

# Cores da Paleta Stitch Palettes:
C_GOLDEN_BROWN = "#b87333"  # DMC 3826
C_TAN = "#d2b48c"           # DMC 436
C_MEDIUM_TERRA = "#b0665c"  # DMC 356
C_DARK_TERRA = "#8b3a3a"    # DMC 3777
C_DARK_ROSEWOOD = "#58292d" # DMC 3857
C_BLACK_BROWN = "#331811"   # DMC 3371

st.markdown(f"""
    <style>
    .stApp {{ background-color: {C_BLACK_BROWN}; color: white; }}
    .main-title {{ text-align: center; color: {C_GOLDEN_BROWN}; font-size: 32px; font-weight: bold; margin-bottom: 0; }}
    .sub-title {{ text-align: center; color: {C_TAN}; letter-spacing: 2px; font-size: 12px; margin-top: -10px; }}
    
    /* Estilo dos Botões */
    div[data-testid="column"] {{ width: 14% !important; min-width: 45px !important; flex: 1 1 0% !important; padding: 2px !important; }}
    .stButton>button {{ 
        width: 100%; border-radius: 8px; background-color: {C_DARK_ROSEWOOD}; 
        color: {C_TAN}; border: 1px solid {C_MEDIUM_TERRA}; font-weight: bold;
    }}
    .stButton>button:hover {{ border-color: {C_GOLDEN_BROWN}; color: white; }}
    
    /* Abas */
    .stTabs [data-baseweb="tab-list"] button {{ color: {C_TAN} !important; }}
    .stTabs [data-baseweb="tab-highlight"] {{ background-color: {C_GOLDEN_BROWN} !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- LOGICA DE ACESSO ---
SENHA_MESTRE = "ALQUIMIA2024" 

if 'autenticado' not in st.session_state: st.session_state.autenticado = False
if 'progresso' not in st.session_state: st.session_state.progresso = [False] * 21

if not st.session_state.autenticado:
    st.markdown("<h1 class='main-title'>BELLA LOLA FITNESS</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>TRANSFORMAÇÃO NEURAL & ALQUIMIA</p>", unsafe_allow_html=True)
    
    with st.container():
        st.write("")
        senha_input = st.text_input("Chave de Acesso:", type="password")
        if st.button("DESBLOQUEAR"):
            if senha_input == SENHA_MESTRE:
                st.session_state.autenticado = True
                st.rerun()
            else: st.error("Chave incorreta!")
        st.divider()
        st.link_button("🔥 ADQUIRIR MINHA CHAVE", "https://seu-link-de-venda.com")
    st.stop()

# --- ÁREA DO ALUNO ---
st.markdown("<h1 class='main-title'>BELLA LOLA FITNESS</h1>", unsafe_allow_html=True)

missoes = [
    "Dia 1: Identifique o 'Eu Antigo'.", "Dia 2: O Poder do Silêncio.", "Dia 3: Redução de Açúcar.",
    "Dia 4: Visualização do Guerreiro.", "Dia 5: Início do Jejum (12h).", "Dia 6: Afirmação Neural.",
    "Dia 7: Registro no Codex.", "Dia 8: 3 respirações profundas.", "Dia 9: Treino Consciente.",
    "Dia 10: Hidratação Estratégica.", "Dia 11: Domínio da Vontade.", "Dia 12: Áudio 528Hz.",
    "Dia 13: Jejum (14h-16h).", "Dia 14: Gratidão.", "Dia 15: Comporte-se como sua nova versão.",
    "Dia 16: Fim da Autossabotagem.", "Dia 17: Alimentos da Terra.", "Dia 18: Resiliência.",
    "Dia 19: Conexão Neural.", "Dia 20: Jejum Profundo (18h).", "Dia 21: Celebração do Novo Eu."
]

tab1, tab2 = st.tabs(["⚔️ JORNADA 21 DIAS", "📊 EVOLUÇÃO"])

with tab1:
    # Grade de Botões (7 por linha)
    for row in range(3):
        cols = st.columns(7)
        for col in range(7):
            idx = row * 7 + col
            with cols[col]:
                if st.session_state.progresso[idx]:
                    st.button("✅", key=f"p{idx}", disabled=True)
                else:
                    if st.button(f"{idx+1}", key=f"p{idx}"):
                        st.session_state.progresso[idx] = True
                        st.rerun()
    
    concluidos = sum(st.session_state.progresso)
    st.progress(concluidos / 21)
    if concluidos < 21:
        st.info(f"🎯 **HOJE:** {missoes[concluidos]}")
    else: st.success("🌟 METAMORFOSE CONCLUÍDA!")

with tab2:
    st.subheader("Medidas e Progresso")
    peso = st.number_input("Peso (kg)", step=0.1)
    meta = st.number_input("Meta (kg)", step=0.1)
    if peso > 0:
        st.metric("Peso Atual", f"{peso}kg", delta=f"{meta-peso:.1f}kg p/ meta")
    st.divider()
    st.camera_input("Registro Visual (Codex)")

if st.sidebar.button("Sair"):
    st.session_state.autenticado = False
    st.rerun()# --- APP PRINCIPAL (LOGADO) ---
st.markdown("<h1 class='main-title'>BELLA LOLA FITNESS</h1>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["⚔️ JORNADA", "🏋️ TREINO", "🧪 ALQUIMIA", "📊 EVOLUÇÃO"])

with tab1:
    missoes = ["Dia 1: Identifique o 'Eu Antigo'.", "Dia 2: O Poder do Silêncio.", "Dia 3: Redução de Açúcar.", "Dia 4: Visualização.", "Dia 5: Jejum (12h).", "Dia 6: Afirmação Neural.", "Dia 7: Registro Codex.", "Dia 8: 3 respirações.", "Dia 9: Treino Consciente.", "Dia 10: Hidratação.", "Dia 11: Domínio Vontade.", "Dia 12: Áudio 528Hz.", "Dia 13: Jejum (14h-16h).", "Dia 14: Gratidão.", "Dia 15: Nova Versão.", "Dia 16: Fim Sabotagem.", "Dia 17: Alimentos da Terra.", "Dia 18: Resiliência.", "Dia 19: Conexão Neural.", "Dia 20: Jejum (18h).", "Dia 21: Celebração."]
    for r in range(3):
        cols = st.columns(7)
        for c in range(7):
            idx = r * 7 + c
            with cols[c]:
                if st.session_state.progresso[idx]: st.button("✅", key=f"p{idx}", disabled=True)
                else:
                    if st.button(f"{idx+1}", key=f"p{idx}"):
                        st.session_state.progresso[idx] = True
                        st.rerun()
    st.progress(sum(st.session_state.progresso) / 21)
    st.info(f"🎯 {missoes[sum(st.session_state.progresso)] if sum(st.session_state.progresso) < 21 else 'CONCLUÍDO!'}")

with tab2:
    st.subheader("Forja Muscular")
    tipo = st.selectbox("Treino de hoje:", list(METS.keys()))
    tempo = st.number_input("Duração (min):", min_value=0, step=5)
    if st.button("REGISTRAR ESFORÇO"):
        cal = (METS[tipo] / 30) * tempo
        st.success(f"🔥 Sensacional! Queimou ~{cal:.0f} calorias.")
        st.balloons()

with tab3:
    st.subheader("🧪 Alquimia Biológica")
    idade = st.number_input("Sua Idade:", min_value=18, max_value=80, value=30)
    horas_jejum = st.slider("Horas de Jejum:", 0, 24, 12)
    if horas_jejum < 12: st.info("🍴 Fase de Absorção.")
    elif 12 <= horas_jejum < 16: st.success("🔥 Queima de Gordura Ativa!")
    else: st.error("🧬 Autofagia (Faxina Celular) Iniciada!")
    st.divider()
    if st.button("CONCLUÍ O BANHO GELADO 🥶"): st.success("Dopamina e Imunidade no topo!")

with tab4:
    st.subheader("Medidas")
    peso = st.number_input("Peso (kg)", step=0.1)
    if peso > 0: st.metric("Peso Atual", f"{peso}kg")
    st.camera_input("Registro Visual (Codex)")

if st.sidebar.button("Sair"):
    st.session_state.autenticado = False
    st.rerun()
