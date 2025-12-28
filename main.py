def mostrar_login():
    print("Bem-vindo à Rent-a-Car (Projeto)")
    email = input("Digite seu e-mail: ")
    senha = input("Senha: ")
    print("(Deixar em branco se for cliente)")
    return email,senha

def main():
    email, senha = mostrar_login()

    if email=="ola" and senha=="123":
        print("login com sucesso!")
    else:
        print("login invalido.")
        mostrar_login()



if __name__ == '__main__':
    main()
