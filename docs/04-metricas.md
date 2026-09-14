# Avaliação e Métricas

A avaliação do Norte foi realizada por meio de testes estruturados, verificando o comportamento do agente em diferentes situações de uso.

Os testes foram utilizados para verificar principalmente:

1. **Assertividade:** capacidade de utilizar corretamente os dados fornecidos e responder de acordo com a solicitação do usuário;
2. **Segurança:** capacidade de respeitar o escopo, evitar a invenção de informações e reconhecer quando não possui dados suficientes;
3. **Coerência:** capacidade de utilizar o contexto financeiro e histórico da conversa para produzir orientações compatíveis com a situação apresentada;
4. **Extração de dados:** capacidade de identificar informações financeiras presentes nas mensagens e estruturá-las corretamente;
5. **Continuidade de contexto:** capacidade de utilizar informações fornecidas em mensagens anteriores durante a conversa.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente utiliza corretamente os dados disponíveis para responder à solicitação? | Informar renda e despesas e solicitar uma análise da situação |
| **Segurança** | O agente respeita o escopo e evita inventar informações? | Perguntar sobre um assunto fora do escopo ou solicitar uma informação que não foi fornecida |
| **Coerência** | A orientação é compatível com o contexto financeiro apresentado? | Informar renda, despesas e um objetivo e solicitar uma orientação |
| **Extração de dados** | O agente identifica e estrutura corretamente as informações financeiras fornecidas? | Informar renda, despesas, reserva e objetivo em uma mesma mensagem |
| **Continuidade de contexto** | O agente consegue utilizar informações fornecidas anteriormente na conversa? | Informar um objetivo em uma mensagem e fazer uma pergunta sobre ele posteriormente |

---

## Exemplos de Cenários de Teste

### Teste 1: Análise do orçamento
- **Pergunta:** "Eu ganho R$ 3.500 por mês, tenho R$ 1.800 de despesas fixas e R$ 700 de despesas variáveis. Como está minha situação?"
- **Resposta esperada:** O agente utiliza os dados fornecidos e apresenta uma análise coerente da situação financeira.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Extração e acumulação de dados
- **Pergunta:** Informar a renda em uma mensagem, as despesas em outra e a reserva financeira em uma terceira.
- **Resposta esperada:** As informações são identificadas e acumuladas corretamente na estrutura de dados da sessão.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Objetivo financeiro
- **Pergunta:** "Quero comprar um carro de R$ 50.000 em 2 anos."
- **Resposta esperada:** O agente reconhece a compra como um objetivo financeiro e utiliza o valor e o prazo informados para orientar a análise.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Continuidade da conversa
- **Pergunta:** Após informar o objetivo de comprar um carro por R$ 50.000 em 2 anos, perguntar: "Quanto eu precisaria guardar por mês?"
- **Resposta esperada:** O agente utiliza o objetivo informado anteriormente e relaciona o valor e o prazo à situação financeira apresentada.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 5: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo para amanhã?"
- **Resposta esperada:** O agente informa que o assunto está fora de seu escopo e redireciona a conversa para organização financeira.
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- O agente conseguiu extrair informações financeiras das mensagens e armazená-las corretamente durante a sessão.
- As informações fornecidas em mensagens diferentes foram acumuladas sem sobrescrever os dados anteriores.
- Os cálculos de total de despesas, saldo mensal e comprometimento da renda foram realizados pela aplicação em Python.
- O LLM conseguiu utilizar os indicadores calculados pela aplicação para contextualizar suas respostas.
- O histórico da conversa permitiu que o agente recuperasse informações apresentadas anteriormente sem que o usuário precisasse repeti-las.
- O agente apresentou comportamento adequado diante de perguntas fora do escopo e solicitações de recomendações de investimento.
- O agente foi capaz de reconhecer objetivos financeiros mesmo quando o usuário não utilizou explicitamente a palavra "objetivo".
- Ajustes no System Prompt e no prompt de extração foram suficientes para corrigir comportamentos inadequados observados durante os testes.

**O que pode melhorar:**
- A extração de informações ainda depende da interpretação do LLM e pode apresentar limitações diante de mensagens ambíguas ou com informações incompletas.
- A aplicação mantém os dados financeiros apenas durante a sessão, não possuindo persistência após o encerramento da aplicação.
- A avaliação realizada foi predominantemente funcional e qualitativa, não tendo sido realizada uma coleta estruturada de notas com um grupo de usuários.
- O projeto utiliza um modelo local, portanto o tempo de resposta pode variar de acordo com o hardware disponível para execução do Ollama.

---

## Métricas Avançadas (Opcional)

Nesta versão do projeto, não foram implementadas ferramentas específicas de observabilidade ou métricas avançadas de LLM.

Como possíveis evoluções futuras, poderiam ser monitorados:

- Latência e tempo de resposta;
- Taxa de erros;
- Número de interações;
- Falhas na extração de dados;
- Consumo de recursos durante a execução do modelo local.

Ferramentas especializadas de observabilidade de aplicações com LLMs poderiam ser utilizadas em uma versão futura caso houvesse necessidade de monitoramento mais detalhado.
