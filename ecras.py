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
    opcao = input("Escolha: \n1-para gerir frota \n2-para gerir classes \n3-para extrato diário \n4-para estatíticas \n5-para sair\n")
    return opcao