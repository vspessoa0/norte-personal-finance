# Código da Aplicação

## Estrutura

```
Estrutura
src/
├── app.py
├── agente.py
├── config.py
├── prompts.py
└── requirements.txt
```
``app.py``

Responsável pela interface e pelo fluxo principal da aplicação utilizando Streamlit.

``agente.py``

Contém a lógica responsável pela comunicação com o modelo de linguagem e pelo processamento dos dados financeiros.

``config.py``

Arquivo destinado às configurações utilizadas pela aplicação.

Permite centralizar parâmetros de configuração para evitar que informações relacionadas à execução do projeto fiquem espalhadas pelo código.

``prompts.py``

Contém os prompts utilizados pelo agente.

## requirements.txt

```
streamlit
ollama
```

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
streamlit run app.py
```
