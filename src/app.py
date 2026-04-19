import streamlit as st
import pandas as pd
import json
import os
import sys

# Garante que o Python encontre o arquivo config e agentes na pasta src
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import config
from agente import AgenteLuma

# 1. Configuração da Página e Estado de Sessão
st.set_page_config(page_title="Luma - IA Financeira", page_icon="🤖", layout="centered")

if "logado" not in st.session_state:
    st.session_state.logado = False
    st.session_state.user_atual = None
if "messages" not in st.session_state:
    st.session_state.messages = []
if "agente" not in st.session_state:
    st.session_state.agente = AgenteLuma()


# 2. Carregamento de Dados (Base de Conhecimento)
@st.cache_data
def carregar_base():
    try:
        with open(config.PERFIL_PATH, 'r', encoding='utf-8') as f:
            perfis = json.load(f)
        with open(config.PRODUTOS_PATH, 'r', encoding='utf-8') as f:
            produtos = json.load(f)
        transacoes = pd.read_csv(config.TRANSACOES_PATH)
        return perfis, produtos, transacoes
    except Exception as e:
        st.error(f"Erro ao carregar base de dados: {e}")
        return [], [], pd.DataFrame()


perfis, produtos, transacoes = carregar_base()

# 3. Tela de Login (Proteção de Dados)
if not st.session_state.logado:
    st.title("🤖 Bem-vinda à Luma")
    st.subheader("Sua assistente para clareza financeira")

    with st.container():
        user_input = st.text_input("Digite seu ID de usuária ou 'admin':", placeholder="Ex: 2")

        if st.button("Entrar"):
            if user_input.lower() == "admin":
                st.session_state.logado = True
                # Admin usa o primeiro perfil como base para a demo
                st.session_state.user_atual = perfis[0] if perfis else {}
                st.rerun()
            else:
                try:
                    uid = int(user_input)
                    user = next((u for u in perfis if u['id'] == uid), None)
                    if user:
                        st.session_state.logado = True
                        st.session_state.user_atual = user
                        st.rerun()
                    else:
                        st.error("Usuária não encontrada. Verifique o ID.")
                except ValueError:
                    st.error("Por favor, insira um ID numérico válido ou 'admin'.")

# 4. Área Logada (Luma em Ação)
else:
    user = st.session_state.user_atual

    # Barra Lateral com Logout e Info
    st.sidebar.title("Luma")
    st.sidebar.info(f"Logada como: **{user['nome']}**")
    if st.sidebar.button("Sair"):
        st.session_state.logado = False
        st.session_state.messages = []
        st.rerun()

    # Cabeçalho do Chat
    st.title("🤖 Chat com Luma")
    st.write(f"Olá {user['nome']}, como posso ajudar na sua organização hoje?")

    # Exibição do Histórico
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input da Usuária
    if prompt := st.chat_input("Dúvida sobre seus gastos ou investimentos?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Lógica da Luma
        with st.chat_message("assistant"):
            # Filtra transações da usuária logada
            user_transacoes = transacoes[transacoes['id_usuario'] == user['id']]

            # Chama o Agente passando o contexto isolado
            resposta = st.session_state.agente.responder(
                pergunta=prompt,
                perfil=user,
                transacoes=user_transacoes,
                produtos=produtos,
                historico_chat=st.session_state.messages[:-1]
            )

            st.markdown(resposta)
            st.session_state.messages.append({"role": "assistant", "content": resposta})