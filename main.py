from io_json import carregar_utilizadores,  guardar_utilizadores
from ecras import (mostrar_login, mostrar_menu_cliente, mostrar_menu_admin,
                   mostrar_gestao_de_frota, mostrar_adicionar_carro, mostrar_adicionar_classe,
                   mostrar_gerir_classe, mostrar_descontos)


def main():
    utilizadores= carregar_utilizadores()
    carros = [
        {"marca": "BMW", "matrícula": "XX-XX-XX", "modelo": "Z3", "classe": "1", "estado": "ativo"},
        {"marca": "Toyota", "matrícula": "YY-YY-YY", "modelo": "corola", "classe": "2", "estado": "ativo"}
    ]
    classes = [
        {"nome": "económico"},
        {"nome": "compacto"}
    ]
    definicoes={
    "max_dias" : 10,
    "desconto_3" : 0,
    "desconto_4_7" : 10,
    "desconto_7": 20
    }

    reservas=[]

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
                    print("MENU RESERVA")
                    print("")
                    posicao=0
                    for carro in carros:
                        posicao += 1
                        print(f"{posicao}-{carro["marca"]} {carro["matrícula"]} {carro['modelo']} {carro['classe']} {carro['estado']}")
                    # resolver erro quando nao e int
                    carro_selecionado=int(input("Escolha o carro: "))
                    # resolver erro quando nº nao existe
                    carro=carros[carro_selecionado-1]
                    dias=input("Quantos dias?: ")
                    reserva = {
                        "carro": carro["matrícula"],
                        "dias": dias,
                        "user": email
                    }
                    reservas.append(reserva)

                    # voltar
                elif opcao=="2":
                    print("historico de reservas")
                    print(reservas)

                elif opcao=="3":
                    print("vou sair do ciclo")

                    break

        # Validar administrador
        elif valido==True and utilizador["tipo"]=="admin":
            print("login com sucesso!")
            # Mostrar menu administrador
            while True:
                opcao = mostrar_menu_admin(email)
                # gestao de frota
                if opcao=="1":
                    opcao=mostrar_gestao_de_frota(carros)

                    # adicionar carro
                    if opcao=="1":
                        carro=mostrar_adicionar_carro()
                        carros.append(carro)
                # gerir classe
                elif opcao=="2":
                    opcao=mostrar_gerir_classe(classes)

                    # adicionar classe
                    if opcao=="1":
                        classe=mostrar_adicionar_classe()
                        classes.append(classe)

                elif opcao=="3":
                    opcao=mostrar_descontos(definicoes)


                elif opcao=="4":
                    print("extrato diário")

                elif opcao =="5":
                    print("sair")
                    break


        else:
            print("login invalido.")




if __name__ == '__main__':
    main()
