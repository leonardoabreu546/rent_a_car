def mostrar_login():
    print("Bem-vindo à Rent-a-Car (Projeto)")
    email = input("Digite seu e-mail: ")
    senha = input("Senha: ")
    print("(Deixar em branco se for cliente)")
    return email,senha

def main():

    while True:
        # xx 123
        email, senha = mostrar_login()

        if email=="ola" and senha=="123":
            print("login com sucesso!")
            input("o que queres fazer")

        else:
            print("login invalido.")




if __name__ == '__main__':
    main()
