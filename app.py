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
    st.stop() # --- APP PRINCIPAL (LOGADO) ---
st.markdown("<h1 class='main-title'>BELLA LOLA FITNESS</h1>", unsafe_allow_html=True)

# AQUI ESTÁ A CORREÇÃO: Definindo as 5 abas corretamente
tab1, tab2, tab3, tab4, tab5 = st.tabs(["⚔️ JORNADA", "🏋️ TREINO", "🧪 ALQUIMIA", "🧠 NEURO", "📈 EVOLUÇÃO"])

with tab1:
    st.subheader("Missão de 21 Dias")
    concluidos = sum(st.session_state.progresso)
    for r in range(3):
        cols = st.columns(7)
        for c in range(7):
            idx = r * 7 + c
            with cols[c]:
                label = "✅" if st.session_state.progresso[idx] else f"{idx+1}"
                if st.button(label, key=f"k{idx}"):
                    st.session_state.progresso[idx] = True
                    st.rerun()
    st.progress(concluidos/21)
    if st.button("🚨 SOS: COMPULSÃO!", key="sos"):
        st.warning("⚠️ **PARE!** Respire fundo 4 vezes. Beba água. A fome é uma onda, ela vai passar.")

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
    if horas_jejum < 12: st.info("🍴 **4-12h:** Queda de Insulina.")
    elif 12 <= horas_jejum < 18: st.success("🔥 **12-18h:** Queima de gordura!")
    else: st.error("🧬 **18h+:** Autofagia Iniciada!")
    if st.button("CONCLUÍ O BANHO GELADO 🥶", key="btn_banho"): st.success("Reset Biológico!")

with tab4:
    st.subheader("Reprogramação Mental")
    st.image("https://images.unsplash.com")
    st.markdown("**Decretos de Poder:**\n* 'Eu comando minha fome.'\n* 'Meu corpo é energia pura.'")
    st.link_button("🎧 OUVIR 528Hz", "https://www.youtube.com")

with tab5:
    st.subheader("🧬 Simulador de Metamorfose")
    # Usando valores padrão para evitar erros se o usuário não preencher
    p_evol = st.number_input("Peso hoje (kg):", value=70.0, step=0.1, key="p_evol")
    a_evol = st.number_input("Altura (m):", value=1.65, step=0.01, key="a_evol")
    
    if st.button("💾 SALVAR NO CODEX", key="save_codex"):
        if 'pesagem' not in st.session_state: st.session_state.pesagem = []
        st.session_state.pesagem.append(p_evol)
        st.rerun()

    st.divider()
    c_boneco, c_comando = st.columns([1, 2])
    
    imc = p_evol / (a_evol**2)
    if imc >= 30:
        f, img, msg, cor = "🛡️ ARMADURA PESADA", "https://cdn-icons-png.flaticon.com", "'Libero o peso que não me pertence.'", "#8b3a3a"
    elif 25 <= imc < 30:
        f, img, msg, cor = "⚔️ GUERREIRO EM ASCENSÃO", "https://cdn-icons-png.flaticon.com", "'Minha armadura está ficando leve.'", "#b87333"
    else:
        f, img, msg, cor = "💎 MESTRE ALQUIMISTA", "https://cdn-icons-png.flaticon.com", "'O templo está em equilíbrio.'", "#D4AF37"

    with c_boneco:
        st.image(img, width=100)
        st.markdown(f"<p style='color:{cor}; font-weight:bold; font-size:10px; text-align:center;'>{f}</p>", unsafe_allow_html=True)
    with c_comando:
        st.info(f"**COMANDO:**\n{msg}")

    if 'pesagem' in st.session_state and st.session_state.pesagem:
        st.line_chart(st.session_state.pesagem)

if st.sidebar.button("SAIR", key="btn_logout"):
    st.session_state.autenticado = False
    st.rerun()

