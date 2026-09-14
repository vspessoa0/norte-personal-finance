import streamlit as st

from agente import responder, extrair_dados, validar_dados, calcular_indicadores



if "dados_financeiros" not in st.session_state:
    st.session_state.dados_financeiros = {
        "renda_mensal": None,
        "despesas_fixas": None,
        "despesas_variaveis": None,
        "reserva_financeira": None,
        "dividas": None,
        "objetivos": None,
    }


if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {
            "role": "assistant",
            "content": (
                "Oi! Eu sou o Norte, uma IA criada para ajudar você a "
                "organizar suas finanças pessoais.\n\n"
                "Podemos conversar sobre seu orçamento, suas despesas, "
                "sua reserva financeira e seus objetivos.\n\n"
                "Pode começar me contando como estão suas finanças hoje."
            )
        }
    ]


st.title("Norte")
st.write("Agente Inteligente para Saúde Financeira Pessoal")


for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])


nova_mensagem = st.chat_input("Digite sua mensagem...")

if nova_mensagem:
    st.session_state.mensagens.append({
        "role": "user",
        "content": nova_mensagem
    })

    with st.chat_message("user"):
        st.write(nova_mensagem)

    with st.spinner("Norte está analisando..."):
        dados_extraidos = extrair_dados(nova_mensagem)
        dados_validos = validar_dados(dados_extraidos)
    
        for campo, valor in dados_validos.items():
            st.session_state.dados_financeiros[campo] = valor

        indicadores = calcular_indicadores(
        st.session_state.dados_financeiros
        )

    historico = st.session_state.mensagens[:-1]

    with st.spinner("Norte está pensando..."):    
        resposta = responder(
            nova_mensagem,
            st.session_state.dados_financeiros,
            indicadores,
            historico
        )

    st.session_state.mensagens.append({
        "role": "assistant",
        "content": resposta
    })

    with st.chat_message("assistant"):
        st.write(resposta)
