import ollama
import json

from prompts import SYSTEM_PROMPT, EXTRACTION_PROMPT


def responder(mensagem, dados_financeiros, indicadores, historico):
    contexto = f"""
Contexto financeiro atual do usuário:

Dados financeiros:
{dados_financeiros}

Indicadores calculados pela aplicação:
{indicadores}
"""

    mensagens = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "system",
            "content": contexto
        }
    ]

    for item in historico:
        mensagens.append({
            "role": item["role"],
            "content": item["content"]
        })

    mensagens.append({
        "role": "user",
        "content": mensagem
    })

    resposta = ollama.chat(
        model="qwen3:8b",
        messages=mensagens
    )

    return resposta["message"]["content"]
def extrair_dados(mensagem):
    resposta = ollama.chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "system",
                "content": EXTRACTION_PROMPT
            },
            {
                "role": "user",
                "content": mensagem
            }
        ]
    )

    conteudo = resposta["message"]["content"]

    try:
        return json.loads(conteudo)
    except json.JSONDecodeError:
        return {}

def validar_dados(dados):
    dados_validos = {}

    campos_numericos = {
        "renda_mensal",
        "despesas_fixas",
        "despesas_variaveis",
        "reserva_financeira",
        "dividas",
    }

    if not isinstance(dados, dict):
        return {}

    for campo, valor in dados.items():

        if campo in campos_numericos:
            if isinstance(valor, (int, float)) and valor >= 0:
                dados_validos[campo] = valor

        elif campo == "objetivos":
            if isinstance(valor, str) and valor.strip():
                dados_validos[campo] = valor.strip()

    return dados_validos

def calcular_indicadores(dados):
    indicadores = {}

    renda = dados.get("renda_mensal")
    despesas_fixas = dados.get("despesas_fixas")
    despesas_variaveis = dados.get("despesas_variaveis")

    if renda is not None and despesas_fixas is not None and despesas_variaveis is not None:
        total_despesas = despesas_fixas + despesas_variaveis
        saldo_mensal = renda - total_despesas

        indicadores["total_despesas"] = total_despesas
        indicadores["saldo_mensal"] = saldo_mensal

        if renda > 0:
            indicadores["comprometimento_renda"] = (
                total_despesas / renda
            ) * 100

    return indicadores