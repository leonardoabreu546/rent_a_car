import json

from io_json import carregar_utilizadores,  guardar_utilizadores
from ecras import mostrar_login, mostrar_menu_cliente, mostrar_menu_admin

def main():
    utilizadores= carregar_utilizadores()


    while True:
        email, senha = mostrar_login()
        valido = False
        utilizador=""
        criar=True

        for utilizadorValidar in utilizadores:
            if email==utilizadorValidar["email"]:
                criar=False

            if email==utilizadorValidar["email"] and senha==utilizadorValidar["senha"]:
                valido = True
                utilizador= utilizadorValidar
                break

        #J 123
        if criar==True:
            novo_utilizador={"email": email ,     "senha": senha, "tipo": "utilizador"}
            utilizadores.append(novo_utilizador)
            valido=True
            utilizador= novo_utilizador
            guardar_utilizadores(utilizadores)

        if valido==True and utilizador["tipo"]=="utilizador":
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
        elif valido==True and utilizador["tipo"]=="admin":
            print("login com sucesso!")
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
