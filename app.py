import streamlit as st

# --- CONFIGURAÇÃO VISUAL BELLA LOLA ---
st.set_page_config(page_title="Bella Lola Fitness - Premium", page_icon="🔐")

# --- CHAVE DE ACESSO (A QUE VOCÊ VENDE) ---
SENHA_MESTRE = "ALQUIMIA2024" 

# --- CONTROLE DE ACESSO ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    # TELA DE VENDAS E LOGIN
    st.markdown("<h1 style='text-align: center; color: #00f2ff;'>BELLA LOLA FITNESS</h1>", unsafe_allow_argument=True)
    st.markdown("<p style='text-align: center;'>SISTEMA EXCLUSIVO DE REPROGRAMAÇÃO NEURAL</p>", unsafe_allow_argument=True)
    
    st.divider()
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.warning("🔒 CONTEÚDO RESTRITO A ALUNOS")
        senha_input = st.text_input("Insira sua Chave de Acesso:", type="password")
        
        if st.button("DESBLOQUEAR MEU ACESSO"):
            if senha_input == SENHA_MESTRE:
                st.session_state.autenticado = True
                st.rerun()
            else:
                st.error("Chave inválida. Verifique seu e-mail de compra.")
        
        st.divider()
        st.info("✨ Ainda não é aluno? Toque no botão abaixo para adquirir sua chave e começar a transformação.")
        st.link_button("🔥 COMPRAR ACESSO AGORA", "https://seu-link-de-venda.com") # COLOQUE SEU LINK AQUI
    st.stop() # Interrompe o app aqui para quem não tem senha

# --- ÁREA LOGADA (SÓ APARECE APÓS A SENHA) ---
st.markdown("<h1 style='text-align: center; color: #00f2ff;'>BEM-VINDA, GUERREIRA!</h1>", unsafe_allow_argument=True)

if 'progresso' not in st.session_state: 
    st.session_state.progresso = [False] * 21

missoes = [
    "Dia 1: Identifique o 'Eu Antigo' e seus gatilhos.", "Dia 2: O Poder do Silêncio. 5 min de meditação.",
    "Dia 3: Redução de Açúcar. Limpando os receptores.", "Dia 4: Visualização do Guerreiro(a).",
    "Dia 5: Início do Jejum (12h). Controle hormonal.", "Dia 6: Afirmação: 'Eu comando minha biologia'.",
    "Dia 7: Registro no Codex. Encare sua sombra.", "Dia 8: Troque o impulso por 3 respirações profundas.",
    "Dia 9: Treino Consciente. Sinta cada músculo.", "Dia 10: Hidratação Estratégica.",
    "Dia 11: Domínio da Vontade. Espere o desejo passar.", "Dia 12: Ouça o Áudio 528Hz de Reparação.",
    "Dia 13: Ampliação do Jejum (14h-16h).", "Dia 14: Gratidão pelas micro-vitórias.",
    "Dia 15: Comporte-se como sua versão de 10kg a menos.", "Dia 16: O Fim da Autossabotagem.",
    "Dia 17: Alimentos da Terra. Nutrição Pura.", "Dia 18: Resiliência. Cair e levantar rápido.",
    "Dia 19: Conexão Neural. Sinta a mudança interna.", "Dia 20: Jejum Profundo (18h). Limpeza Total.",
    "Dia 21: Celebração. O Nascimento do Novo Eu."
]

# Dashboard de Medidas (Agora dentro da área paga)
with st.expander("📊 MEU PAINEL DE MEDIDAS"):
    c1, c2 = st.columns(2)
    peso = c1.number_input("Peso Atual (kg)", step=0.1)
    altura = c2.number_input("Altura (m)", step=0.01)
    if peso > 0 and altura > 0:
        st.metric("Seu IMC", f"{peso/(altura**2):.1f}")

# Desafio 21 Dias
st.subheader("⚔️ JORNADA 21 DIAS")
cols = st.columns(7)
for i in range(21):
    with cols[i % 7]:
        if st.session_state.progresso[i]:
            st.button(f"✅", key=f"d{i}", disabled=True)
        else:
            if st.button(f"{i+1}", key=f"d{i}"):
                st.session_state.progresso[i] = True
                st.rerun()

atual = sum(st.session_state.progresso)
st.progress(atual / 21)

if atual < 21:
    st.info(f"🚀 **SUA MISSÃO:** {missoes[atual]}")
else:
    st.balloons()
    st.success("METAMORFOSE COMPLETA NO STUDIO BELLA LOLA!")

if st.button("Sair do Sistema"):
    st.session_state.autenticado = False
    st.rerun()
