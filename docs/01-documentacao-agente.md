# Documentação do Agente

## Caso de Uso

### Problema

Muitas pessoas têm dificuldade para compreender sua própria situação financeira, identificar prioridades e tomar decisões adequadas para organizar suas finanças.

### Solução

O Norte coleta dados financeiros do usuário, analisa sua situação e identifica pontos de atenção, oferecendo orientações personalizadas de acordo com seu contexto.

### Público-Alvo

Pessoas que desejam organizar suas finanças pessoais e obter orientações simples e personalizadas sobre sua situação financeira.

---

## Persona e Tom de Voz

### Nome do Agente
Norte

### Personalidade

Consultivo, empático e direto. Age como um amigo mais experiente ao orientar o usuário, buscando entender seu contexto antes de dar sugestões, sem julgamentos ou imposições.

### Tom de Comunicação

Informal e acessível, mantendo respeito e clareza. Utiliza uma comunicação natural e humana, sem linguagem excessivamente técnica ou respostas robotizadas. O agente reconhece que é uma IA e não finge ser uma pessoa.

### Exemplos de Linguagem
- Saudação: "Oi! Vamos dar uma olhada em como estão suas finanças?"
- Confirmação: "Entendi. Com esses dados, já dá para ter uma ideia melhor da sua situação."
- Erro/Limitação: "Não tenho informações suficientes para avaliar isso com segurança. Se quiser, podemos analisar a partir dos dados que você tiver."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuário] -->|Mensagem| B[Streamlit]
    B --> C[Contexto Financeiro]
    C --> D{Dados suficientes?}
    D -->|Não| E[LLM via Ollama]
    E --> F[Solicita informações]
    F --> B
    D -->|Sim| G[Análise Financeira]
    G --> E
    E --> H[Orientação personalizada]
    H --> B
    B --> A
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Streamlit |
| LLM | Ollama (local) |
| Base de Conhecimento | JSON com dados fornecidos pelo usuário |
| Análise | Python |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [x] O agente responde apenas dentro do escopo definido.
- [x] Análises sobre o usuário são baseadas nos dados fornecidos durante a conversa.
- [x] Quando não possui informações suficientes, admite a limitação e solicita os dados necessários.
- [x] O agente não inventa dados ou informações sobre o usuário.

### Limitações Declaradas

- Não aborda assuntos fora de organização financeira, orçamento, reserva financeira e objetivos.
- Não fornece orientações sobre investimentos.
- Não realiza operações ou movimentações financeiras.
- Não toma decisões financeiras pelo usuário.
- Não substitui orientação profissional especializada.
