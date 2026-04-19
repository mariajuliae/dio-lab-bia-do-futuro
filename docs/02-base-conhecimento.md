# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `perfil_investidor.json` | JSON | Armazena dados das usuárias (renda, dívidas, objetivos, comportamento) para personalizar respostas|
| `produtos_financeiros.json` | JSON | Define os produtos que podem ser recomendados, evitando alucinações |
| `transacoes.csv` | CSV | Permite analisar padrão de gastos, identificar desequilíbrios e gerar alertas |
| `historico_atendimento.csv` | CSV | Mantém contexto das interações anteriores, evitando repetição e permitindo continuidade |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados mockados fornecidos pelo desafio foram adaptados e expandidos para refletir cenários mais realistas e variados.

As principais modificações foram:
- Criação de uma base própria de 15 usuárias, com perfis diversos (empreendedoras e não empreendedoras), incluindo:
  - renda mensal
  - tipo de renda (fixa, variável ou informal)
  - presença de dívidas
  - objetivos financeiros
  - nível de conhecimento financeiro
  - perfil comportamental
- Expansão do arquivo transacoes.csv, com múltiplas transações por usuária, permitindo análise de padrões de receita e despesa.
- Criação de um historico_atendimento.csv, simulando interações anteriores para dar contexto e continuidade ao agente.
- Estruturação do arquivo produtos_financeiros.json, contendo apenas produtos controlados, garantindo que o agente não faça recomendações fora da base (estratégia anti-alucinação).

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os dados são carregados no início da aplicação utilizando:
- json para arquivos .json
- pandas para arquivos .csv
Esses dados ficam armazenados em memória e são acessados conforme o usuário interage com o agente.
Não há uso de APIs externas — todas as respostas são baseadas exclusivamente nos dados locais, garantindo controle e segurança.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados não são enviados de forma bruta para a LLM.

Antes disso, o sistema:

- Identifica a usuária pelo id
- Filtra:
  - seu perfil (perfil_investidor.json)
  - suas transações (transacoes.csv)
  - seu histórico (historico_atendimento.csv)
- Analisa regras simples (if/else) para entender o contexto
- Filtra os produtos compatíveis (produtos_financeiros.json)

Só então um contexto estruturado é enviado para a LLM.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
### PERFIL DA USUÁRIA ###
- Nome: Maria Souza
- Renda Mensal: R$ 1800
- Tipo de Renda: Informal
- Possui Dívida: Sim (R$ 2000)
- Objetivo: Expandir negócio
- Nível Financeiro: Baixo

### RESUMO FINANCEIRO ###
- Total de Receitas no mês: R$ 1100
- Total de Despesas no mês: R$ 620
- Situação: Renda instável e presença de dívidas

### HISTÓRICO RECENTE ###
- Usuária já demonstrou dificuldade em organizar finanças
- Já perguntou sobre empréstimos anteriormente

### PRODUTOS COMPATÍVEIS ###
1. Renegociação de Dívidas
2. Microcrédito Empreendedora
3. Planejamento Financeiro

### INSTRUÇÃO PARA O AGENTE ###
- Priorizar orientação sobre organização financeira
- Evitar recomendar novos créditos de alto risco
- Usar linguagem simples e acolhedora
...
```
