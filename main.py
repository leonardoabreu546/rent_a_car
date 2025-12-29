def mostrar_login():
    print("Bem-vindo à Rent-a-Car (Projeto)")
    email = input("Digite seu e-mail: ")
    senha = input("Senha: ")
    print("(Deixar em branco se for cliente)")
    return email,senha

def main():

    while True:
        # ola 123
        email, senha = mostrar_login()

        if email=="ola" and senha=="123":
            print("login com sucesso!")

            while True:
                print("MENU CLIENTE")
                print(f"Utillizador: {email}")
                print("O que deseja fazer?")
                opçao=input("escolha 1 para efetuar reserva, 2 para consultar historico de reservas e 3 para sair.")

                if opçao=="1":
                    print("menu reserva")
                    input("qual reserva")
                    # voltar
                elif opçao=="2":
                    print("historico de reservas")
                    input("qual historico")
                elif opçao=="3":
                    print("vou sair do ciclo")
                    break

        else:
            print("login invalido.")







if __name__ == '__main__':
    main()
