import json

def carregar_utilizadores():
    with open("utilizadores.json", "r", encoding="utf-8") as f:
        utilizadores = json.load(f)
    return utilizadores

def guardar_utilizadores(utilizadores):
    with open("utilizadores.json", "w", encoding="utf-8") as f:
        json.dump(utilizadores, f, indent=4, ensure_ascii=False)

def guardar_reservas(reservas):
    with open("reservas.json", "w", encoding="utf-8") as f:
        json.dump(reservas, f, indent=4, ensure_ascii=False)

def carregar_reservas():
    with open("reservas.json", "r", encoding="utf-8") as f:
        reservas = json.load(f)
    return reservas

def carregar_carros():
    with open("carros.json", "r", encoding="utf-8") as f:
        carros = json.load(f)
    return carros

def guardar_carros(carros):
    with open("carros.json", "w", encoding="utf-8") as f:
        json.dump(carros, f, indent=4, ensure_ascii=False)

def guardar_classes(classes):
    with open("classes.json", "w", encoding="utf-8") as f:
        json.dump(classes, f, indent=4, ensure_ascii=False)

def carregar_classes():
    with open("classes.json", "r", encoding="utf-8") as f:
        classes = json.load(f)
    return classes

def carregar_definicoes():
    with open("definicoes.json", "r", encoding="utf-8") as f:
        definicoes = json.load(f)
    return definicoes