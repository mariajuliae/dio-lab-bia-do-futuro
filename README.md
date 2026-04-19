# 🤖 LUMA — Agente Financeira Inteligente

## Sobre o Projeto

A **Bia** é uma agente de inteligência artificial desenvolvida para ajudar mulheres a entender, organizar e melhorar sua vida financeira de forma simples e acessível.

O projeto foi criado como parte de um desafio prático de desenvolvimento de agentes com IA generativa, com foco em:

- personalização
- segurança (anti-alucinação)
- impacto social

Diferente de chatbots tradicionais, a Bia analisa dados da usuária para oferecer orientações contextualizadas, respeitando sua realidade financeira.

---

## Problema

Muitas pessoas enfrentam dificuldades para lidar com dinheiro devido a:

- falta de educação financeira
- linguagem técnica e pouco acessível
- ausência de soluções personalizadas
- renda variável ou endividamento

---

## Solução

A Bia atua como uma assistente financeira que:

- analisa perfil, transações e histórico da usuária  
- identifica padrões de comportamento financeiro  
- sugere próximos passos de forma simples  
- apresenta opções financeiras seguras  

Sempre priorizando:
1. Organização financeira  
2. Controle de gastos  
3. Construção de reserva  
4. Investimentos (quando aplicável)  

---

## Funcionalidades

- Análise de transações financeiras  
- Personalização com base no perfil da usuária  
- Chat interativo  
- Continuidade com histórico de atendimento  
- Controle de respostas (anti-alucinação)  
- Recomendação de produtos financeiros (limitada à base)  

---

## Ferramentas Sugeridas

Todas as ferramentas abaixo possuem versões gratuitas:

| Categoria | Ferramentas |
|-----------|-------------|
| **LLMs** | [ChatGPT](https://chat.openai.com/), [Copilot](https://copilot.microsoft.com/), [Gemini](https://gemini.google.com/), [Claude](https://claude.ai/), [Ollama](https://ollama.ai/) |
| **Desenvolvimento** | [Streamlit](https://streamlit.io/), [Gradio](https://www.gradio.app/), [Google Colab](https://colab.research.google.com/) |
| **Orquestração** | [LangChain](https://www.langchain.com/), [LangFlow](https://www.langflow.org/), [CrewAI](https://www.crewai.com/) |
| **Diagramas** | [Mermaid](https://mermaid.js.org/), [Draw.io](https://app.diagrams.net/), [Excalidraw](https://excalidraw.com/) |

---

## Estrutura do Repositório

```
📁 lab-agente-financeiro/
│
├── 📄 README.md
│
├── 📁 data/                          # Dados mockados para o agente
│   ├── historico_atendimento.csv     # Histórico de atendimentos (CSV)
│   ├── perfil_investidor.json        # Perfil do cliente (JSON)
│   ├── produtos_financeiros.json     # Produtos disponíveis (JSON)
│   └── transacoes.csv                # Histórico de transações (CSV)
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # Código da aplicação
│   └── app.py                        # (exemplo de estrutura)
│
├── 📁 assets/                        # Imagens e diagramas
│   └── ...
│
└── 📁 examples/                      # Referências e exemplos
    └── README.md
```

---

## Tecnologias Utilizadas

- Python  
- Streamlit (interface)  
- JSON e CSV (base de dados)  
- LLM (ex: OpenAI API)  

---

## Segurança e Confiabilidade

A Luma foi projetada para evitar erros comuns em IA:

- utiliza apenas dados da base local  
- não inventa informações  
- recomenda apenas produtos disponíveis  
- evita sugestões inadequadas (ex: investimento para quem tem dívida)  

⚠️ **Importante:**  
Este agente possui caráter educativo e não substitui um consultor financeiro profissional.

---

## Base de Dados

O projeto utiliza dados mockados e estruturados:

- **15 perfis de usuárias** com diferentes realidades financeiras  
- **Histórico de transações** para análise de comportamento  
- **Histórico de atendimentos** para continuidade  
- **Produtos financeiros controlados** para evitar alucinações  

---

## Como Executar o Projeto

1. Clone o repositório:
```
git clone https://github.com/seu-usuario/lab-agente-financeiro.git
```

2. Acesse a pasta:
```
cd lab-agente-financeiro
```

4. Instale as dependências:
```
pip install -r requirements.txt
```
6. Execute a aplicação:
```
streamlit run src/app.py
```
---

## Testes e Avaliação

O agente foi avaliado com base em:

- assertividade das respostas  
- coerência com o perfil da usuária  
- segurança (anti-alucinação)  
- capacidade de personalização  

---

## Impacto

A Luma busca democratizar o acesso à orientação financeira, ajudando pessoas a:

- entender melhor seu dinheiro  
- tomar decisões mais conscientes  
- reduzir riscos financeiros  

---

## Melhorias Futuras

- análises financeiras mais avançadas  
- integração com APIs reais  
- aprendizado contínuo com interações  
- interface mais robusta  

---

## Autoria

Projeto desenvolvido por Maria Julia Elias como parte de um desafio de IA aplicada ao setor financeiro do Bootcamp Bradesco GenAI & Dados.


