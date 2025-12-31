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
    id = input("Intoduiza o id: ")
    nome = input("Introduza o nome  classe: ")
    descricao = input("Intoduiza a descricao: ")
    # tratar erro do inteiro ao introduzir letras
    preco_dia = int(input("Intoduiza o preço por dia: "))

    classe = {"id":id, "nome": nome, "descricao": descricao, "preco_dia": preco_dia}
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

def mostrar_descontos(definicoes):
    print("DEFINIÇÕES GERAIS")
    print("")
    print(f"Máximo de dias de reserva: {definicoes["max_dias"]}")
    print("")
    print("Descontos (%):")
    print("")

    print(f"Até 3 dias: {definicoes["desconto_3"]}")
    print(f"De 4 a 7 dias: {definicoes["desconto_4_7"]} ")
    print(f"Mais de 7 dias: {definicoes["desconto_7"]}")
    print("")
    print("1-Editar")
    print("2-Voltar")
    opcao=input("Escolha: ")
    return opcao

def mostrar_criar_reserva(carros, email, classes, definicoes):
    print("MENU RESERVA")
    print("")
    posicao=0
    classe_escolhida={}
    for carro in carros:
        posicao += 1
        classe_escolhida = next(classe for classe in classes if classe["id"] == carro["classe"])
        print(f"{posicao}-{carro["marca"]} {carro["matrícula"]} {carro['modelo']} {classe_escolhida["preco_dia"]}€ {carro['estado']}")

    # resolver erro quando nao e int
    carro_selecionado=int(input("Escolha o carro: "))
    # resolver erro quando nº nao existe
    carro=carros[carro_selecionado-1]
    dias=int(input("Quantos dias?: "))

    if dias>definicoes["max_dias"]:
        print("Excedeu o número máximo de dias")
        dias=definicoes["max_dias"]

    reserva = {
        "matricula": carro["matrícula"],
        "dias": dias,
        "email": email,
        "preco_dia": classe_escolhida["preco_dia"],
        "preco_total": classe_escolhida["preco_dia"]*dias
    }
    return reserva

def mostrar_historico_reservas(reservas, email):
    print("HISTÓRICO DE RESERVAS")
    for reserva in reservas:
        if email == reserva["email"]:
            print(f"{reserva["matricula"]} {reserva["dias"]} {reserva["preco_dia"]}€ {reserva['preco_total']}€")
    print("0- para sair")
    opcao = input("Escolha: ")
    return opcao