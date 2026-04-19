import os

# Configurações da API de exemplo
GROQ_API_KEY = "SUA_CHAVE_AQUI"
MODEL_NAME = "llama-3.3-70b-versatile"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

PERFIL_PATH = os.path.join(DATA_DIR, "perfil_investidor.json")
PRODUTOS_PATH = os.path.join(DATA_DIR, "produtos_financeiros.json")
TRANSACOES_PATH = os.path.join(DATA_DIR, "transacoes.csv")

# Parâmetros de comportamento da Luma
TEMPERATURE = 0.3
MAX_TOKENS = 1000