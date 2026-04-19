from groq import Groq
import config

class AgenteLuma:
    def __init__(self):
        """Inicializa o cliente Groq com a persona da Luma."""
        self.client = Groq(api_key=config.GROQ_API_KEY)
        self.modelo = "llama-3.1-70b-versatile"
        self.modelo = config.MODEL_NAME

        # Persona e Regras extraídas da sua documentação
        self.system_prompt_base = """
        Você é a Luma, uma assistente de IA especializada em orientação financeira para mulheres.
        Personalidade: Acolhedora, educativa, prática e sem julgamentos.
        Linguagem: Acessível, direta e não técnica.

        REGRAS DE OURO:
        1. Use APENAS os dados fornecidos no contexto.
        2. Se a usuária tem dívidas, priorize organização e quitação antes de qualquer investimento.
        3. Recomende apenas produtos que existam na lista de produtos fornecida.
        4. Se não souber algo, admita que não possui a informação.
        5. Nunca substitua um consultor financeiro profissional.
        """

    # No agentes.py, mude essa parte:
    def preparar_contexto(self, perfil, transacoes, produtos):
        contexto = f"""
        ### PERFIL DA USUÁRIA ###
        - Nome: {perfil.get('nome')}
        - Renda: R$ {perfil.get('renda_mensal')} 
        - Possui Dívida: {'Sim' if perfil.get('tem_divida') else 'Não'}
        - Objetivo: {perfil.get('objetivo')}
        """
        return contexto

    def responder(self, pergunta, perfil, transacoes, produtos, historico_chat=[]):
        """Executa a chamada para a API do Groq."""
        contexto_dinamico = self.preparar_contexto(perfil, transacoes, produtos)

        # Montagem das mensagens seguindo o fluxo de histórico
        messages = [
            {"role": "system", "content": self.system_prompt_base},
            {"role": "system", "content": f"CONTEXTO DA USUÁRIA:\n{contexto_dinamico}"}
        ]

        # Adiciona o histórico da conversa atual
        messages.extend(historico_chat)

        # Adiciona a pergunta atual
        messages.append({"role": "user", "content": pergunta})

        try:
            completion = self.client.chat.completions.create(
                model=self.modelo,
                messages=messages,
                temperature=0.3,  # Baixa temperatura para manter a precisão
                max_tokens=1000
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Luma: Ops, tive um probleminha técnico para acessar meus dados. (Erro: {e})"