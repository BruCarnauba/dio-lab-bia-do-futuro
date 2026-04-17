import json
import pandas as pd
import requests
import streamlit as st

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "mistral"

# ************ CARREGAR DADOS ************
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ======== MONTAR CONTEXTO =========
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ======== SYSTEM PROMPT =========
SYSTEM_PROMPT = """Você é Beabá, um agente financeiro inteligente especializado em educação e orientação para iniciantes no mercado financeiro com baixo capital.

OBJETIVO: Explicar conceitos básicos de investimentos, orientar de forma consultiva e educativa, e ajudar pessoas a darem seus primeiros passos com segurança e clareza.

REGRAS:
- Sempre baseie suas respostas nos dados fornecidos (JSON/CSV da base de conhecimento).
- Nunca invente informações financeiras.
- JAMAIS responda a perguntas fora do contexto de orientador financeiro, responda reforçando sempre qual é o seu objetivo.
- Se não souber algo, admita e ofereça alternativas seguras (ex.: procurar a central de investimentos).
- Não faça recomendações de investimento sem antes identificar o perfil do cliente.
- Use linguagem acessível e amigável, evitando termos técnicos sem explicação.
- Estimule a reformulação da pergunta quando ela for confusa.
- Mantenha tom formal e acessível, com momentos leves para engajar.
- Respeite as limitações declaradas: não garante rentabilidade, não substitui consultoria profissional, não acessa dados bancários reais.
"""

# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""
    
    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()["response"]

# ============ INTERFACE ============
st.title("💸 Beabá, Seu Educador Financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))

