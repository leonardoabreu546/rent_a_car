import os
def mostrar_login():
    print("Bem-vindo à Rent-a-Car (Projeto)")
    email = input("Digite seu e-mail: ")
    senha = input("Senha: ")
    print("(Deixar em branco se for cliente)")
    return email,senha

def mostrar_menu_cliente(email):
    print("MENU CLIENTE")
    print(f"Utillizador: {email}")
    print("O que deseja fazer?")
    opcao = input("Escolha: \n1-para efetuar reserva \n2-para consultar historico de reservas \n3-para sair\n")
    return opcao

def mostrar_menu_admin(email):
    print("PAINEL DE ADMINISTRADOR")
    print(f"Utillizador: {email}")
    print("O que deseja fazer?")

    print("1-para gerir frota")
    print("2-para gerir classes")
    print("3-definições gerais")
    print("4-para estatíticas")
    print("5-para sair")
    opcao = input("Escolha: ")
    return opcao

def mostrar_gestao_de_frota(carros):
    os.system("cls")
    print("GESTÃO DE FROTA")

    for carro in carros:
        print(f"{carro["marca"]} {carro["matrícula"]} {carro['modelo']} {carro['classe']} {carro['estado']}")

    print("")
    print("1- Adicionar carro")
    print("2- Editar carro")
    print("3- Remover carro")
    print("4- Voltar ao menu principal")
    opcao = input("Introuzir opção: ")
    return opcao

def mostrar_adicionar_carro():
    print("ADICIONAR CARRO")
    marca = input("Intoduizir marca: ")
    matricula = input("Intoduizir matrícula: ")
    modelo = input("Intoduizir modelo: ")
    classe = input("Intoduizir classe: ")
    estado = input("Intoduizir estado: ")
    carro = {"marca": marca, "matrícula": matricula, "modelo": modelo, "classe": classe, "estado": estado}
    return carro

def mostrar_adicionar_classe():
    print("ECRÃ ADICIONAR CLASSE")
    nome = input("Introduza o nome  classe: ")
    classe = {"nome": nome}
    return classe

def mostrar_gerir_classe(classes):
    print("MENU GERIR CLASSE")
    for classe in classes:
        print(f"{classe["nome"]}")
    print("1-Adicionar classe")
    print("2-Editar classe (Selecionar ID)")
    print("3-Remover classe")
    print("4-Voltar ao menu principal")
    opcao = input("Escolha: ")
    return opcao