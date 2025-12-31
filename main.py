from io_json import (carregar_utilizadores, guardar_utilizadores, guardar_reservas, carregar_carros, carregar_reservas,
                     guardar_carros, guardar_classes, carregar_classes, carregar_definicoes)
from ecras import (mostrar_login, mostrar_menu_cliente, mostrar_menu_admin,
                   mostrar_gestao_de_frota, mostrar_adicionar_carro, mostrar_adicionar_classe,
                   mostrar_gerir_classe, mostrar_descontos, mostrar_criar_reserva, mostrar_historico_reservas)


def main():
    utilizadores= carregar_utilizadores()
    carros = carregar_carros()
    classes = carregar_classes()
    definicoes=carregar_definicoes()

    reservas=carregar_reservas()

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

                # Criar reserva
                if opcao=="1":
                    reserva=mostrar_criar_reserva(carros, email)
                    reservas.append(reserva)
                    guardar_reservas(reservas)

                    # voltar
                elif opcao=="2":
                    mostrar_historico_reservas(reservas, email)


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
                        guardar_carros(carros)

                # gerir classe
                elif opcao=="2":
                    opcao=mostrar_gerir_classe(classes)

                    # adicionar classe
                    if opcao=="1":
                        classe=mostrar_adicionar_classe()
                        classes.append(classe)
                        guardar_classes(classes)

                elif opcao=="3":
                    opcao=mostrar_descontos(definicoes)


                elif opcao=="4":
                    print("EXTRATO DIÁRIO")

                elif opcao =="5":
                    print("SAIR")
                    break


        else:
            print("login invalido.")




if __name__ == '__main__':
    main()
