import streamlit as st

# --- 1. CONFIGURAÇÃO E ESTILO (DESIGN CALENDÁRIO) ---
st.set_page_config(page_title="Bella Lola Fitness - Premium", page_icon="🍂", layout="centered")

C_GOLD = "#b87333"  
C_TAN = "#d2b48c"   
C_TERRA = "#b0665c" 
C_MARROM = "#58292d" 
C_FUNDO = "#331811"  

st.markdown(f"""
    <style>
    .stApp {{ background-color: {C_FUNDO}; color: white; font-family: 'Georgia', serif; }}
    .main-title {{ text-align: center; color: {C_GOLD}; font-size: 32px; font-weight: bold; margin-bottom: 0; }}
    .sub-title {{ text-align: center; color: {C_TAN}; letter-spacing: 2px; font-size: 12px; margin-top: -10px; margin-bottom: 20px; }}
    
    /* FORÇAR 7 COLUNAS NO CELULAR */
    [data-testid="column"] {{
        width: 13% !important;
        flex: 1 1 0% !important;
        min-width: 40px !important;
        padding: 2px !important;
    }}
    
    .stButton>button {{ 
        width: 100%; 
        border-radius: 5px; 
        background-color: {C_MARROM}; 
        color: {C_TAN}; 
        border: 1px solid {C_TERRA}; 
        font-weight: bold; 
        padding: 5px 0px;
        font-size: 14px;
    }}
    .stButton>button:hover {{ border-color: {C_GOLD}; color: white; }}
    .stTabs [data-baseweb="tab-list"] button {{ color: {C_TAN} !important; }}
    .stTabs [data-baseweb="tab-highlight"] {{ background-color: {C_GOLD} !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGICA DE DADOS ---
METS = {"Caminhada 🚶": 120, "Corrida 🏃‍♀️": 180, "Bicicleta 🚲": 250, "Musculação 🏋️": 150, "HIIT 🔥": 240, "Dança 💃": 200}
SENHA_MESTRE = "ALQUIMIA2024"

if 'autenticado' not in st.session_state: st.session_state.autenticado = False
if 'progresso' not in st.session_state: st.session_state.progresso = [False] * 21
if 'pesagem' not in st.session_state: st.session_state.pesagem = []

# --- 3. TELA DE ACESSO ---
if not st.session_state.autenticado:
    st.markdown("<h1 class='main-title'>BELLA LOLA FITNESS</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>SISTEMA DE REPROGRAMAÇÃO NEURAL</p>", unsafe_allow_html=True)
    senha_in = st.text_input("Chave de Acesso:", type="password")
    if st.button("DESBLOQUEAR PORTAL", key="login"):
        if senha_in == SENHA_MESTRE:
            st.session_state.autenticado = True
            st.rerun()
        else: st.error("Chave inválida.")
    st.stop()

# --- 4. APP PRINCIPAL (LOGADO) ---
st.markdown("<h1 class='main-title'>BELLA LOLA FITNESS</h1>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["⚔️ JORNADA", "🏋️ TREINO", "🧪 ALQUIMIA", "🧠 NEURO", "📈 EVOLUÇÃO"])

with tab1:
    st.subheader("Missão de 21 Dias")
    
    # GERADOR DE CALENDÁRIO (7 colunas por linha)
    for row in range(3): # 3 linhas
        cols = st.columns(7) # 7 colunas
        for col_idx in range(7):
            day_idx = row * 7 + col_idx
            with cols[col_idx]:
                if st.session_state.progresso[day_idx]:
                    st.button("✅", key=f"btn{day_idx}", disabled=True)
                else:
                    if st.button(f"{day_idx+1}", key=f"btn{day_idx}"):
                        st.session_state.progresso[day_idx] = True
                        st.rerun()
    
    concluidos = sum(st.session_state.progresso)
    st.progress(concluidos/21)
    
    missoes = [
        "Identifique o 'Eu Antigo'.", "Poder do Silêncio.", "Redução de Açúcar.", "Visualização.", 
        "Jejum (12h).", "Afirmação Neural.", "Registro Codex.", "3 respirações.", 
        "Treino Consciente.", "Hidratação.", "Domínio Vontade.", "Áudio 528Hz.", 
        "Jejum (14h).", "Gratidão.", "Nova Versão.", "Fim Sabotagem.", 
        "Nutrição Pura.", "Resiliência.", "Conexão Neural.", "Jejum (18h).", "Novo Eu."
    ]
    
    if concluidos < 21:
        st.info(f"🎯 **HOJE:** {missoes[concluidos]}")
    else:
        st.success("🌟 METAMORFOSE CONCLUÍDA!")

    if st.button("🚨 SOS COMPULSÃO", key="sos"):
        st.warning("⚠️ PARE! Respire fundo 4x. Beba água. A vontade passa em 5 min!")

with tab2:
    st.subheader("Forja Muscular")
    tipo = st.selectbox("O que treinou?", list(METS.keys()), key="sel_t")
    tempo = st.number_input("Minutos:", min_value=0, step=5, key="num_t")
    if st.button("REGISTRAR", key="reg_t"):
        cal = (METS[tipo]/30)*tempo
        st.success(f"🔥 Queimou ~{cal:.0f} calorias!")
        st.balloons()

with tab3:
    st.subheader("🧪 Alquimia Biológica")
    p_atual = st.number_input("Seu Peso (kg):", value=70.0, step=0.1, key="p_bio")
    a_atual = st.number_input("Sua Altura (m):", value=1.65, step=0.01, key="a_bio")
    if p_atual > 0:
        st.success(f"💧 Meta de Água: **{p_atual * 35 / 1000:.1f}L**")
    
    st.divider()
    h_jej = st.slider("Horas de Jejum:", 0, 24, 14, key="sl_jej")
    if h_jej >= 18: st.error("🧬 AUTOFAGIA: Renovação Celular.")
    elif h_jej >= 12: st.warning("🔥 QUEIMA: Gordura como combustível.")
    else: st.info("🍴 ABSORÇÃO: Processando nutrientes.")

with tab4:
    st.subheader("Reprogramação Mental")
    st.image("https://images.unsplash.com")
    st.markdown("**Decretos:**\n* 'Eu comando minha fome.'\n* 'Meu corpo é força pura.'")
    st.link_button("🎧 ÁUDIO 528Hz", "https://www.youtube.com")

with tab5:
    st.subheader("🧬 Simulador de Metamorfose")
    p_ev = st.number_input("Peso hoje (kg):", value=70.0, step=0.1, key="p_ev")
    a_ev = st.number_input("Altura (m):", value=1.65, step=0.01, key="a_ev")
    
    if st.button("💾 SALVAR NO CODEX", key="sv_ev"):
        st.session_state.pesagem.append(p_ev)
        st.rerun()

    imc = p_ev / (a_ev**2)
    c1, c2 = st.columns([1, 2])
    
    if imc >= 30:
        f, img, msg, cl = "🛡️ ARMADURA PESADA", "https://cdn-icons-png.flaticon.com", "'Libero o peso que não me pertence.'", "#8b3a3a"
    elif 25 <= imc < 30:
        f, img, msg, cl = "⚔️ GUERREIRO EM ASCENSÃO", "https://cdn-icons-png.flaticon.com", "'Minha armadura está ficando leve.'", "#b87333"
    else:
        f, img, msg, cl = "💎 MESTRE ALQUIMISTA", "https://cdn-icons-png.flaticon.com", "'O templo está em equilíbrio.'", "#D4AF37"

    with c1:
        st.image(img, width=80)
        st.markdown(f"<p style='color:{cl}; font-weight:bold; font-size:10px; text-align:center;'>{f}</p>", unsafe_allow_html=True)
    with c2:
        st.info(f"**COMANDO:**\n{msg}")

    if st.session_state.pesagem:
        st.line_chart(st.session_state.pesagem)

if st.sidebar.button("SAIR", key="logout"):
    st.session_state.autenticado = False
    st.rerun()
