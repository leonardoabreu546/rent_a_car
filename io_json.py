import json

def carregar_utilizadores():
    with open("utilizadores.json", "r", encoding="utf-8") as f:
        utilizadores = json.load(f)
    return utilizadores
