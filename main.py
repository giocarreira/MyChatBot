from langchain_community.chat_models import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
from utilidades import resposta_interface, escolher_chain
from prompts import prompts_personalizados
from datetime import datetime
import streamlit as st
import time
import os

load_dotenv()

base = os.getenv("AZURE_OPENAI_ENDPOINT")
key = os.getenv("AZURE_OPENAI_API_KEY")
version = os.getenv("AZURE_OPENAI_API_VERSION")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

modelo = AzureChatOpenAI(
    azure_endpoint=base,
    openai_api_version=version,
    openai_api_key=key,
    deployment_name=deployment,
    openai_api_type="azure",
    temperature=1,
    streaming= True
)

template_geral, template_resumo, template_intencao = prompts_personalizados()

if "memoria" not in st.session_state:
    st.session_state.memoria = ConversationBufferMemory(
        memory_key="historico_conversa",
        return_messages=True,
        input_key="mensagem_usuario"
    )

memoria = st.session_state.memoria

prompt_geral = PromptTemplate(
    input_variables = ["data", "mensagem_usuario", "historico_conversa"],
    template = template_geral
)

prompt_resumo = PromptTemplate(
    input_variables = ["data", "mensagem_usuario", "historico_conversa"],
    template = template_resumo
)

prompt_intencao = PromptTemplate(
    input_variables = ["data", "mensagem_usuario"],
    template = template_intencao
)

chain_geral = LLMChain(
    llm = modelo,
    prompt = prompt_geral,
    memory = memoria
)

chain_resumo = LLMChain(
    llm = modelo, 
    prompt = prompt_resumo,
    memory = memoria
)

chain_intencao = LLMChain(
    llm = modelo, 
    prompt = prompt_intencao,
    memory = memoria
)

st.title("ChatBot Gigi Carreira")

if "historico" not in st.session_state:
    st.session_state.historico = []

entrada_usuario = st.chat_input("Digite sua mensagem...")

for autor, texto in st.session_state.historico:
    with st.chat_message(autor):
        st.markdown(texto)

if entrada_usuario:
    data_hoje = datetime.now().strftime("%Y/%m/%d")

    st.session_state.historico.append(("user", entrada_usuario))
    with st.chat_message("user"):
            st.markdown(entrada_usuario)

    chain_escolhida = escolher_chain(entrada_usuario, data_hoje, chain_geral, chain_resumo, chain_intencao)      

    resposta = chain_escolhida.invoke({
        "data" : data_hoje,
        "mensagem_usuario" : entrada_usuario,
    })
        
    st.session_state.historico.append(("assistant", resposta["text"]))
    with st.chat_message("assistant"):
        placeholder = st.empty()
        texto = ""
        for letra in resposta["text"]:
            texto += letra
            placeholder.markdown(texto)
            time.sleep(0.018)


