# Base de Conhecimento

## Dados Utilizados

| Dado | Formato | Utilização no Agente |
|---------|---------|---------------------|
| Renda mensal | Numérico | Analisar capacidade financeira |
| Despesas fixas | Numérico | Avaliar comprometimento da renda |
| Despesas variáveis | Numérico | Analisar gastos e saldo mensal |
| Reserva financeira | Numérico | Avaliar situação da reserva |
| Dívidas | Numérico | Identificar comprometimento financeiro |
| Objetivos financeiros | Texto | Orientar o planejamento financeiro |

---

## Adaptações nos Dados

Não são utilizados dados mockados. As informações financeiras são coletadas diretamente do usuário e estruturadas durante a sessão.

---

## Estratégia de Integração

### Como os dados são carregados?

Os dados são coletados durante a conversa e armazenados em uma estrutura Python na memória da aplicação, permanecendo disponíveis apenas durante a sessão.

### Como os dados são usados no prompt?

Os dados financeiros estruturados e os indicadores calculados pelo Python são inseridos dinamicamente no contexto enviado ao LLM para gerar respostas personalizadas.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Contexto financeiro do usuário:
- Renda mensal: R$ 3.500
- Despesas fixas: R$ 1.800
- Despesas variáveis: R$ 700
- Reserva financeira: R$ 0
- Dívidas: R$ 0
- Objetivo: Comprar um carro

Indicadores:
- Saldo mensal estimado: R$ 1.000
- Situação da reserva: Inexistente
```
