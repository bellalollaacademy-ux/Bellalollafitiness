import streamlit as st

# --- CONFIGURAÇÃO VISUAL BELLA LOLA ---
st.set_page_config(page_title="Bella Lola Fitness - Premium", page_icon="🍂", layout="centered")

C_GOLDEN_BROWN = "#b87333"  
C_TAN = "#d2b48c"           
C_MEDIUM_TERRA = "#b0665c"  
C_DARK_ROSEWOOD = "#58292d" 
C_BLACK_BROWN = "#331811"   

st.markdown(f"""
    <style>
    .stApp {{ background-color: {C_BLACK_BROWN}; color: white; }}
    .main-title {{ text-align: center; color: {C_GOLDEN_BROWN}; font-size: 32px; font-weight: bold; margin-bottom: 0; }}
    .sub-title {{ text-align: center; color: {C_TAN}; letter-spacing: 2px; font-size: 12px; margin-top: -10px; margin-bottom: 20px; }}
    div[data-testid="column"] {{ width: 14% !important; min-width: 45px !important; flex: 1 1 0% !important; padding: 2px !important; }}
    .stButton>button {{ width: 100%; border-radius: 8px; background-color: {C_DARK_ROSEWOOD}; color: {C_TAN}; border: 1px solid {C_MEDIUM_TERRA}; font-weight: bold; }}
    .stButton>button:hover {{ border-color: {C_GOLDEN_BROWN}; color: white; }}
    .stTabs [data-baseweb="tab-list"] button {{ color: {C_TAN} !important; }}
    .stTabs [data-baseweb="tab-highlight"] {{ background-color: {C_GOLDEN_BROWN} !important; }}
    </style>
    """, unsafe_allow_html=True)

# --- DICIONÁRIOS E ESTADOS ---
METS = {"Caminhada 🚶": 120, "Corrida 🏃‍♀️": 180, "Bicicleta 🚲": 250, "Musculação 🏋️": 150, "HIIT 🔥": 240, "Dança 💃": 200}
SENHA_MESTRE = "ALQUIMIA2024" 

if 'autenticado' not in st.session_state: st.session_state.autenticado = False
if 'progresso' not in st.session_state: st.session_state.progresso = [False] * 21

# --- TELA DE ACESSO ---
if not st.session_state.autenticado:
    st.markdown("<h1 class='main-title'>BELLA LOLA FITNESS</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>SISTEMA DE REPROGRAMAÇÃO NEURAL</p>", unsafe_allow_html=True)
    senha_input = st.text_input("Chave de Acesso:", type="password")
    if st.button("DESBLOQUEAR", key="btn_login"):
        if senha_input == SENHA_MESTRE:
            st.session_state.autenticado = True
            st.rerun()
        else: st.error("Chave incorreta!")
    st.stop()# --- APP PRINCIPAL ---
st.markdown("<h1 class='main-title'>BELLA LOLA FITNESS</h1>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["⚔️ JORNADA", "🏋️ TREINO", "🧪 ALQUIMIA", "📊 EVOLUÇÃO"])

with tab1:
    missoes = ["Dia 1: Identifique o 'Eu Antigo'.", "Dia 2: O Poder do Silêncio.", "Dia 3: Redução de Açúcar.", "Dia 4: Visualização.", "Dia 5: Jejum (12h).", "Dia 6: Afirmação Neural.", "Dia 7: Registro Codex.", "Dia 8: 3 respirações.", "Dia 9: Treino Consciente.", "Dia 10: Hidratação.", "Dia 11: Domínio Vontade.", "Dia 12: Áudio 528Hz.", "Dia 13: Jejum (14h).", "Dia 14: Gratidão.", "Dia 15: Nova Versão.", "Dia 16: Fim Sabotagem.", "Dia 17: Alimentos da Terra.", "Dia 18: Resiliência.", "Dia 19: Conexão Neural.", "Dia 20: Jejum (18h).", "Dia 21: Celebração."]
    for r in range(3):
        cols = st.columns(7)
        for c in range(7):
            idx = r * 7 + c
            with cols[c]:
                if st.session_state.progresso[idx]: st.button("✅", key=f"k{idx}", disabled=True)
                else:
                    if st.button(f"{idx+1}", key=f"k{idx}"):
                        st.session_state.progresso[idx] = True
                        st.rerun()
    st.progress(sum(st.session_state.progresso) / 21)
    st.info(f"🎯 {missoes[sum(st.session_state.progresso)] if sum(st.session_state.progresso) < 21 else 'CONCLUÍDO!'}")

with tab2:
    st.subheader("Forja Muscular")
    tipo = st.selectbox("Treino de hoje:", list(METS.keys()), key="sel_treino")
    tempo = st.number_input("Duração (min):", min_value=0, step=5, key="num_tempo")
    if st.button("REGISTRAR ESFORÇO", key="btn_treino"):
        cal = (METS[tipo] / 30) * tempo
        st.success(f"🔥 Sensacional! Queimou ~{cal:.0f} calorias.")
        st.balloons()

with tab3:
    st.subheader("🧪 Alquimia Biológica")
    idade = st.number_input("Sua Idade:", min_value=18, max_value=80, value=30, key="num_idade")
    horas_jejum = st.slider("Horas de Jejum:", 0, 24, 12, key="sli_jejum")
    if horas_jejum < 12: st.info("🍴 **4-12h:** Queda de Insulina e Glicose.")
    elif 12 <= horas_jejum < 18: st.success("🔥 **12-18h:** Queima de gordura e HGH elevado!")
    else: st.error("🧬 **18h+:** Autofagia e Renovação Celular Profunda!")
    st.divider()
    if st.button("CONCLUÍ O BANHO GELADO 🥶", key="btn_banho"): st.success("Biologia resetada!")

with tab4:
    st.subheader("Medidas")
    peso = st.number_input("Peso (kg)", step=0.1, key="num_peso")
    if peso > 0: st.metric("Peso Atual", f"{peso}kg")
    st.camera_input("Registro Visual (Codex)", key="cam_codex")

if st.sidebar.button("Sair", key="btn_sair"):
    st.session_state.autenticado = False
    st.rerun()

