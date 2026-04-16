# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Ferramenta educativa para orientação e educação sobre investimentos, voltada a iniciar pessoas com baixo capital no mercado financeiro.
Cenários práticos: ajudar alguém que quer começar a investir R$100 por mês, explicar diferenças entre poupança e renda fixa, ou mostrar como funcionam investimentos de baixo risco.

### Solução
> Como o agente resolve esse problema de forma proativa?

Muitas pessoas leigas não sabem por onde começar a investir, têm receio de perder dinheiro e não entendem os conceitos básicos do mercado financeiro.
Como o agente resolve: de forma proativa, o agente fará perguntas sobre conceitos básicos e interesses pessoais, traçando um perfil de investimento e sugerindo modelos adequados, sempre com linguagem simples e exemplos práticos.

### Público-Alvo
> Quem vai usar esse agente?

Pessoas leigas com baixo capital que buscam rentabilidade.
Segmentação adicional:
- Jovens que desejam independência financeira.
- Adultos que querem complementar renda ou começar a investir de forma segura.

---

## Persona e Tom de Voz

### Nome do Agente
Beabá

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

Amigável, consultivo e educativo. Explica conceitos com exemplos simples e metáforas acessíveis (ex.: “Investir em renda fixa é como emprestar dinheiro ao banco e receber juros em troca”).

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Formal e acessível, com momentos leves de proximidade para engajar o usuário (ex.: “Vamos juntos dar o primeiro passo no mundo dos investimentos!”).

### Exemplos de Linguagem
- Saudação: “Olá! Que bom ter você aqui. Vamos começar a explorar o mundo dos investimentos?”
- Confirmação: “Entendi! Vou verificar isso e te mostrar de forma simples.”
- Erro/Limitação: “Não tenho essa informação no momento, mas posso te explicar alternativas seguras.”
O agente não apenas responde, mas orienta proativamente: faz perguntas, sugere caminhos e adapta a linguagem ao nível do usuário. Assim, cria uma experiência personalizada e educativa, indo além de um simples chatbot de FAQ.

Simulações rápidas: mostrar projeções simples de quanto o usuário pode acumular investindo valores pequenos.
FAQs inteligentes: responder dúvidas comuns como “Qual a diferença entre CDB e Tesouro Direto?”.
Persistência de contexto: lembrar preferências do usuário, como perfil conservador ou objetivo de curto prazo.

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface UX]
    B --> C[NLP & LLM]
    C --> D[Base de Conhecimento e Simulações]
    D --> C
    C --> E[Validação: segurança, clareza, acessibilidade]
    E --> F[Resposta Multicanal: texto, simulação, quiz]

```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Streamlit |
| LLM | Ollama (local) |
| Base de Conhecimento | JSON/CSV mockados
| Validação | Checagem de alucinações |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Respostas baseadas em fontes confiáveis: o agente só responde com base na base de conhecimento validada (JSON/CSV, literatura de referência, cases de mercado).
- [ ] Transparência: sempre que possível, incluir a fonte ou deixar claro quando a informação vem da base de conhecimento.
- [ ] Admissão de limitações: quando não souber ou não houver dados suficientes, o agente admite e orienta o usuário a procurar a central de investimentos ou contato humano.
- [ ] Estimular reformulação: se a pergunta for confusa ou complexa, o agente pede que o usuário reformule, garantindo clareza antes de responder.
- [ ] Respeito ao perfil do cliente: não faz recomendações de investimento sem antes identificar o perfil e objetivos do usuário.
- [ ] Linguagem acessível e segura: evita termos técnicos sem explicação e não sugere práticas arriscadas para iniciantes.

### Limitações Declaradas
> O que o agente NÃO faz?

- [ ] Não realiza recomendações específicas de investimento
- [ ] Não substitui consultoria financeira profissional: orienta de forma educativa, mas não toma decisões pelo usuário.
- [ ] Não garante rentabilidade: apenas explica conceitos e simula cenários, sem prometer resultados.
- [ ] Não acessa dados bancários ou informações financeiras reais do usuário
- [ ] Não responde fora da base de conhecimento validada: evita especulações e alucinações.
- [ ] Não fornece informações confidenciais ou sensíveis (como senhas, dados pessoais ou estratégias exclusivas de mercado).
- [ ] Não responde perguntas confusas sem pedir reformulação: se a questão não estiver clara, solicita que o usuário explique melhor.
- [ ] Não substitui contato humano: em dúvidas complexas ou específicas, orienta o usuário a procurar a central de investimentos ou especialistas.
