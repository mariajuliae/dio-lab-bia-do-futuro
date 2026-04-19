# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `perfil_investidor.json` | JSON | Define se o quiz deve ser mais detalhado ou direto |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os ficheiros CSV e JSON são carregados no início da aplicação utilizando as bibliotecas pandas e json. Os dados das APIs de cotação são consultados via pedidos HTTP (biblioteca requests) sempre que o utilizador inicia uma nova simulação, garantindo dados de mercado atualizados.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados são injetados de forma estruturada no contexto enviado à LLM:

- Dados de Perfil e Transações: São incluídos como "Fatos sobre o Utilizador" para que a IA saiba com quem está a falar.

- Dados de Mercado: As cotações reais são passadas como variáveis de contexto para alimentar os cálculos de projeção.

- Filtro de Produtos: Antes de enviar as opções ao prompt, o código Python filtra o produtos_financeiros.json, enviando para a IA apenas o que é adequado ao perfil do cliente.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
### PERFIL DO CLIENTE ###
- Nome: Gabriel Figueiredo
- Perfil Detectado: Moderado
- Capacidade de Aporte Mensal Calculada: R$ 850,00

### DADOS DE MERCADO ATUAIS ###
- Taxa Selic: 10.75% a.a.
- IPCA (últimos 12 meses): 4.50%

### OPÇÕES DE INVESTIMENTO COMPATÍVEIS ###
1. CDB Fácil Bradesco (Pós-fixado)
2. Letra de Crédito Imobiliário (LCI) - Isenta de IR
3. Fundo de Investimento em Renda Fixa

### HISTÓRICO RECENTE ###
- O cliente possui 3 transações de alto valor em lazer este mês. 
Sugestão: Abordar a importância da reserva de emergência antes de investir em ativos de longo prazo.
...
```
