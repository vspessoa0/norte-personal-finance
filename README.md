# Norte — Agente Inteligente para Saúde Financeira Pessoal

O **Norte** é um agente conversacional de inteligência artificial desenvolvido para ajudar na **organização das finanças pessoais**.

Em vez de trabalhar com dados financeiros previamente cadastrados, o agente coleta as informações diretamente durante a conversa, estrutura esses dados e utiliza indicadores calculados pela aplicação para oferecer orientações contextualizadas.

> Projeto desenvolvido como projeto final do bootcamp **Accenture - Python para Análise e Automação de Dados**, da DIO.

---

## Sobre o projeto

O Norte foi desenvolvido para pessoas que desejam compreender melhor sua situação financeira e identificar prioridades para organizar suas finanças.

Durante a conversa, o usuário pode fornecer informações como:

- Renda mensal;
- Despesas fixas;
- Despesas variáveis;
- Reserva financeira;
- Dívidas;
- Objetivos financeiros.

A partir dessas informações, o sistema mantém um contexto financeiro durante a sessão e pode analisar aspectos como:

- Total de despesas;
- Saldo mensal;
- Comprometimento da renda;
- Relação entre orçamento e objetivos financeiros.

O agente utiliza essas informações para conduzir a conversa e apresentar orientações de forma simples e contextualizada.

---

## Como funciona

O processamento do Norte combina **Python** e um **modelo de linguagem local**.

O fluxo principal é:

```text
Usuário
   ↓
Streamlit
   ↓
Extração de informações pelo LLM
   ↓
Validação dos dados
   ↓
Atualização do contexto financeiro
   ↓
Cálculo dos indicadores pelo Python
   ↓
Contexto + histórico da conversa
   ↓
LLM
   ↓
Orientação personalizada
```

A divisão de responsabilidades é intencional:

| Responsabilidade | Componente |
|---|---|
| Interface | Streamlit |
| Gerenciamento da sessão | Python / Streamlit |
| Extração de informações | LLM |
| Validação dos dados | Python |
| Cálculos financeiros | Python |
| Interpretação do contexto | LLM |
| Geração das respostas | LLM |
| Regras de comportamento | Prompts |

Dessa forma, cálculos determinísticos não ficam sob responsabilidade do modelo de linguagem.

---

## Inteligência Artificial

O Norte utiliza o **Qwen3 8B**, executado localmente através do **Ollama**.

O modelo é utilizado para:

- Extrair informações financeiras das mensagens;
- Interpretar o contexto financeiro;
- Manter a continuidade da conversa;
- Identificar quando são necessárias informações adicionais;
- Gerar orientações dentro do escopo do agente.

A execução local elimina a necessidade de utilizar uma API externa de LLM para o funcionamento do protótipo.

---

## Escopo

O Norte foi projetado para atuar especificamente nos seguintes assuntos:

- Organização financeira;
- Orçamento;
- Reserva financeira;
- Objetivos financeiros.

### Fora do escopo

O agente não:

- Fornece recomendações de investimentos;
- Realiza operações ou movimentações financeiras;
- Toma decisões financeiras pelo usuário;
- Atua como consultor sobre produtos ou serviços relacionados aos objetivos;
- Responde a assuntos completamente fora de seu domínio;
- Inventa informações financeiras, preços, taxas ou dados sobre o usuário.

Quando não possui informações suficientes, o agente reconhece a limitação e solicita os dados necessários.

---

## Exemplo de interação

O usuário pode fornecer informações aos poucos durante a conversa:

```text
Usuário:
Eu ganho R$ 3.500 por mês.

Norte:
Entendi. Já tenho sua renda mensal. Se quiser, podemos analisar
 também suas despesas para entender melhor seu orçamento.

Usuário:
Tenho R$ 1.800 de despesas fixas e uns R$ 700 de despesas variáveis.

Norte:
Com esses dados, suas despesas somam R$ 2.500 e seu saldo mensal
estimado é de R$ 1.000. Podemos analisar como esse valor se relaciona
com suas prioridades e objetivos.

Usuário:
Quero comprar um carro de R$ 50.000 em 2 anos.

Norte:
Entendi. Podemos tratar a compra como um objetivo financeiro.
A partir do valor e do prazo que você informou, podemos analisar
quanto seria necessário reservar mensalmente e como isso se encaixa
no seu orçamento.
```

Os valores utilizados no exemplo são apenas ilustrativos.

---

## Tecnologias

- **Python** — lógica da aplicação, validação e cálculos;
- **Streamlit** — interface conversacional;
- **Ollama** — execução local do modelo de linguagem;
- **Qwen3 8B** — modelo de linguagem utilizado pelo agente;
- **JSON** — estruturação dos dados financeiros durante a sessão;
- **Git/GitHub** — versionamento e disponibilização do projeto.

---

## Estrutura do projeto

```text
norte-personal-finance/
│
├── docs/
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
│
├── examples/
│
├── src/
│   ├── app.py
│   ├── agente.py
│   ├── config.py
│   ├── prompts.py
│   ├── requirements.txt
│   └── README.md
│
├── .gitignore
└── README.md
```

### Documentação

A pasta [`docs/`](./docs/) contém os detalhes do desenvolvimento:

- [`01-documentacao-agente.md`](./docs/01-documentacao-agente.md) — caso de uso, persona, arquitetura e segurança;
- [`02-base-conhecimento.md`](./docs/02-base-conhecimento.md) — estrutura e utilização dos dados;
- [`03-prompts.md`](./docs/03-prompts.md) — prompts, exemplos de interação e aprendizados;
- [`04-metricas.md`](./docs/04-metricas.md) — avaliação e cenários de teste;
- [`05-pitch.md`](./docs/05-pitch.md) — material utilizado para apresentação do projeto.

A documentação técnica específica da implementação está disponível em [`src/README.md`](./src/README.md).

---

## Instalação

### Pré-requisitos

É necessário ter instalado:

- Python 3;
- Ollama.

### 1. Clone o repositório

```bash
git clone https://github.com/vspessoa0/norte-personal-finance.git
cd norte-personal-finance
```

### 2. Crie e ative o ambiente virtual

No Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r src/requirements.txt
```

### 4. Baixe o modelo

```bash
ollama pull qwen3:8b
```

### 5. Execute a aplicação

```bash
streamlit run src/app.py
```

Após iniciar, o Streamlit disponibilizará a aplicação no navegador.

---

## Dados e privacidade

Os dados financeiros utilizados pelo Norte são fornecidos pelo próprio usuário durante a conversa e permanecem disponíveis apenas durante a sessão da aplicação.

O projeto **não utiliza banco de dados nem possui persistência dos dados financeiros após o encerramento da sessão**.

O modelo de linguagem também é executado localmente através do Ollama.

> Apesar da execução local, este projeto é um protótipo educacional e não deve ser utilizado como substituto de orientação financeira profissional.

---

## Avaliação

O agente foi avaliado por meio de testes funcionais envolvendo:

- Assertividade das respostas;
- Segurança e respeito ao escopo;
- Coerência com o contexto financeiro;
- Extração de dados;
- Continuidade da conversa;
- Tratamento de informações insuficientes;
- Tratamento de solicitações fora do escopo.

Os resultados e cenários utilizados na avaliação estão documentados em [`docs/04-metricas.md`](./docs/04-metricas.md).

---

## Principais aprendizados

O desenvolvimento do Norte demonstrou que um LLM não precisa ser responsável por todas as etapas do processamento.

A aplicação combina:

**Python**
- Estruturação dos dados;
- Validação;
- Cálculos determinísticos;
- Gerenciamento do contexto.

**LLM**
- Interpretação da linguagem natural;
- Extração de informações;
- Condução da conversa;
- Geração das orientações.

Essa divisão permite aproveitar a flexibilidade dos modelos de linguagem sem delegar ao LLM operações que podem ser realizadas de forma determinística pela aplicação.

---

## Limitações

Esta versão do Norte possui algumas limitações:

- Os dados são mantidos somente durante a sessão;
- A extração de informações depende da interpretação do modelo de linguagem;
- Mensagens ambíguas ou incompletas podem exigir novas perguntas ao usuário;
- O tempo de resposta depende do hardware utilizado para executar o modelo localmente;
- A avaliação realizada foi predominantemente funcional e qualitativa.

---

## Próximos passos

Como possíveis evoluções futuras, o projeto poderia incorporar:

- Persistência opcional dos dados;
- Histórico financeiro entre sessões;
- Monitoramento mais detalhado das interações;
- Métricas automatizadas de qualidade;
- Melhorias na extração de informações;
- Novos indicadores de saúde financeira.

Essas funcionalidades não fazem parte do escopo atual do protótipo.

---

## Autor

**Vinicius Pessoa**

Projeto desenvolvido para conclusão do bootcamp **Accenture - Python para Análise e Automação de Dados**, da DIO.
