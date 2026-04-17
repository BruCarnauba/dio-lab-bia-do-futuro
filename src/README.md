Passo a Passo de Execução do Projeto Beabá
Este documento descreve as etapas necessárias para executar o projeto Beabá, incluindo tempo aproximado de cada fase.

1. Preparação do Ambiente (10–15 minutos)
Instalar Python 3.9 ou superior.

Instalar dependências:

bash
pip install pandas requests streamlit
Garantir que o Ollama esteja rodando localmente na porta 11434.

2. Organização dos Dados (5–10 minutos)
Criar a pasta ./data/.

Inserir os arquivos:

perfil_investidor.json

transacoes.csv

historico_atendimento.csv

produtos_financeiros.json

3. Configuração do Script (5 minutos)
Verificar variáveis de configuração:

OLLAMA_URL = "http://localhost:11434/api/generate"

MODELO = "mistral"

Confirmar que os arquivos de dados estão corretamente referenciados.

4. Montagem do Contexto (automático)
O script carrega os dados JSON e CSV.

Gera o contexto do cliente com perfil, transações, histórico e produtos.

5. Definição do System Prompt (automático)
O script define regras e objetivos do agente Beabá.

Não requer intervenção manual.

6. Execução da Função perguntar (tempo variável)
Recebe a pergunta do usuário.

Monta o prompt com contexto e regras.

Faz requisição POST para Ollama.

Tempo de resposta: 2–5 segundos.

7. Interface com Streamlit (5 minutos para iniciar)
Executar:

bash
streamlit run app.py
Interface exibirá título e campo de chat.

Usuário interage enviando perguntas.

8. Uso do Sistema (tempo contínuo)
Usuário digita dúvidas sobre finanças.

Assistente responde com base nos dados fornecidos.

Tempo de uso depende da interação.

Tempo Total Estimado
Preparação inicial: 20–30 minutos.

Execução contínua: depende da interação do usuário.
