from datetime import datetime
import sys
import time

def efeito_digitacao(texto, delay=0.03):
    print("\nAssistente: ", end="")
    for letra in texto:
        print(letra, end="")
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

def escolher_chain(mensagem, data_hoje, chain_geral, chain_resumo, chain_intencao):
    try:
        resposta_intencao = chain_intencao.invoke({
            "mensagem_usuario": mensagem,
            "data": data_hoje,
            })
        intencao = resposta_intencao["text"].strip().lower()
        if intencao == "resumo":
            return chain_resumo
        else:
            return chain_geral
    except Exception as e:
        print(f"Erro ao classificar intenção: {e}")
        return chain_geral

def resposta_interface(texto):
    return texto
