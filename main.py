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

def main():

    while True:
        email, senha = mostrar_login()

        utilizadores=[
            {"email": "a",     "senha": "123", "tipo": "utilizador"},
            {"email": "b",     "senha": "456", "tipo": "utilizador"},
            {"email": "c",     "senha": "789", "tipo": "utilizador"},
            {"email": "d",     "senha": "888", "tipo": "utilizador"},
            {"email": "admin", "senha": "999", "tipo": "admin"}
        ]

        valido = False

        for utilizador in utilizadores:
            if email==utilizador["email"] and senha==utilizador["senha"]:
                valido = True
                break


        if valido==True:
            print("login com sucesso!")

            while True:
                opcao = mostrar_menu_cliente(email)

                if opcao=="1":
                    print("menu reserva")
                    input("qual reserva:")
                    # voltar
                elif opcao=="2":
                    print("historico de reservas")
                    input("qual historico:")
                elif opcao=="3":
                    print("vou sair do ciclo")
                    input("qual vou sair do ciclo:")
                    break

        # Validar administrador
        elif email=="admin" and senha=="999":
            # Mostrar menu administrador
            while True:
                opcao = mostrar_menu_admin(email)
                if opcao=="1":
                    print("menu gerir frota")
                    input("qual frota:")
                elif opcao=="2":
                    print("menu gerir classe")
                    input("qual classe:")
                elif opcao=="3":
                    print("menu definições gerais ")
                    input("quais definiçoes:")
                elif opcao=="4":
                    print("extrato diário")
                    input("qual extrato:")
                elif opcao =="5":
                    print("sair")
                    break
        else:
            print("login invalido.")




if __name__ == '__main__':
    main()
