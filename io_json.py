import json

def carregar_utilizadores():
    with open("utilizadores.json", "r", encoding="utf-8") as f:
        utilizadores = json.load(f)
    return utilizadores

def guardar_utilizadores(utilizadores):
    with open("utilizadores.json", "w", encoding="utf-8") as f:
        json.dump(utilizadores, f, indent=4, ensure_ascii=False)