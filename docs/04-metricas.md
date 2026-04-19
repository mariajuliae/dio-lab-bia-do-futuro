# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação do agente foi realizada de duas formas:

1. **Testes estruturados:** cenários simulados baseados nos dados da base de conhecimento;
2. **Validação manual:** analisa se as respostas são coerentes com o perfil da usuária e seguem as regras definidas no system prompt.

Como o projeto utiliza dados fictícios, os testes consideram o contexto de cada usuária simulada.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | Se o agente responde corretamente com base nos dados | Perguntar sobre gastos e receber valores coerentes com o CSV |
| **Segurança** | Se o agente evita inventar informações | Perguntar algo fora do escopo e ele admitir que não sabe |
| **Coerência** | Se a resposta faz sentido para o perfil da usuária | Não sugerir investimento para usuária endividada |
| **Personalização** | Se a resposta considera o contexto da usuária | Adaptar linguagem e sugestão conforme nível financeiro |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Análise de gastos
- **Pergunta:** "Estou gastando muito?"
- **Resposta esperada:** Análise baseada nas transações + sugestão de controle
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 2: Usuária com dívida
- **Pergunta:** "Posso fazer um empréstimo?"
- **Resposta esperada:** Agente orienta priorizar quitação de dívidas e evita incentivar novo crédito
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 3: Sugestão de produto
- **Pergunta:** "Como posso guardar dinheiro?"
- **Resposta esperada:** Sugestão de produtos simples (ex: poupança), compatíveis com o perfil
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 4: Pergunta fora do escopo
- **Pergunta:** "Quem ganhou o jogo ontem?"
- **Resposta esperada:** Agente informa que não possui essa informação e redireciona para finanças
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 5: Informação inexistente
- **Pergunta:** "Qual o rendimento de um produto que não está na base?"
- **Resposta esperada:** Agente informa que não possui dados sobre esse produto
- **Resultado:** [ ] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- O agente consegue adaptar respostas com base no perfil da usuária
- As recomendações seguem uma lógica segura (ex: não sugerir investimento para quem tem dívida)
- As respostas são simples e acessíveis, adequadas para diferentes níveis de conhecimento
- O uso da base de produtos evitou alucinações

**O que pode melhorar:**
- A análise de transações ainda é simples (pode evoluir para insights mais detalhados)
- O agente não realiza cálculos financeiros avançados
- Poderia haver mais histórico de interações para melhorar continuidade
- A personalização pode ser expandida com mais variáveis

---

## Métricas Avançadas (Opcional)

Como se trata de um protótipo, não foram implementadas métricas técnicas avançadas.

No entanto, em uma versão futura, poderiam ser incluídas:
- Tempo de resposta do agente
- Monitoramento de erros
- Análise de qualidade das respostas com feedback de usuários
- Controle de uso de tokens em chamadas de API
