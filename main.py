def main():
    print("Bem-vindo à Rent-a-Car (Projeto)")
    email= input("Digite seu e-mail: ")
    senha=input("Senha: ")
    print("(Deixar em branco se for cliente)")
    print(f"Email: {email}")
    print(f"Senha: {senha}")

    if email=="ola" and senha=="123":
        print("login com sucesso!")
    else:
        print("login invalido.")



if __name__ == '__main__':
    main()
