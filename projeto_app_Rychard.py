'''
CRUD - Sistema de Hamburgueria

Este sistema simula um atendimento simples de uma hamburgueria.
O cliente pode se cadastrar, ver o cardápio, adicionar itens no carrinho
e finalizar um pedido.
'''

cliente = {}
carrinho = []

# Loop principal do sistema
while True:

    print("\n== Sistema da Hamburgueria ===")
    print("1. Cadastro")
    print("2. Esqueceu a senha")
    print("3. Menu")
    print("4. Carrinho")
    print("5. Opções")
    print("6. Finalizar pedido")
    print("7. Cupom")
    print("8. Chat da loja")
    print("9. Feedback")
    print("0. Sair")

    escolha = input("\nEscolha uma opção: ")

    # 1 - CADASTRO DE CLIENTE
    if escolha == '1':
        print("\n--- Novo Cadastro ---")

        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        cpf = input("CPF: ")
        senha = input("Senha: ")

        print(f"Seja bem-vindo(a), {nome}!")

        cliente = {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "cpf": cpf,
            "senha": senha
        }

        print("Cadastro realizado com sucesso!")

    # 2 - RECUPERAÇÃO DE SENHA
    elif escolha == '2':
        print("\n--- Recuperação de senha ---")

        email = input("Digite seu email cadastrado: ")
        print("Um código de recuperação foi enviado para seu email...")

        codigo = input("Digite o código: ")
        nova_senha = input("Digite sua nova senha: ")

        print("Senha alterada com sucesso.")

    # 3 - MENU / CARDÁPIO
    elif escolha == '3':
        while True:
            print("\n--- Menu ---")
            print("1. Lanches")
            print("2. Combos")
            print("3. Bebidas")
            print("0. Voltar")

            sub_escolha = input("Escolha uma opção do menu: ")

            # Lanches
            if sub_escolha == '1':
                print("\nLanches disponíveis:")
                print("1 - X-Burguer - 15,00R$")
                print("2 - X-Salada - 18,00R$")
                print("3 - X-Bacon - 20,00R$")

                item = input("Escolha um lanche para adicionar ao carrinho: ")

                if item == '1':
                    carrinho.append("X-Burguer")
                    print("X-Burguer adicionado ao carrinho.")

                elif item == '2':
                    carrinho.append("X-Salada")
                    print("X-Salada adicionado ao carrinho.")

                elif item == '3':
                    carrinho.append("X-Bacon")
                    print("X-Bacon adicionado ao carrinho.")

                else:
                    print("Opção inválida, tente novamente.")

            # Combos
            elif sub_escolha == '2':
                print("\nCombos disponíveis:")
                print("1 - Combo Família - 45,00R$")
                print("2 - Combo Duplo - 30,00R$")
                print("3 - Combo Kid - 20,00R$")

                item = input("Escolha um combo: ")

                if item == '1':
                    carrinho.append("Combo Família")
                    print("Combo Família adicionado ao carrinho.")

                elif item == '2':
                    carrinho.append("Combo Duplo")
                    print("Combo Duplo adicionado ao carrinho.")

                elif item == '3':
                    carrinho.append("Combo Kid")
                    print("Combo Kid adicionado ao carrinho.")

                else:
                    print("Opção inválida, tente novamente.")

            # Bebidas
            elif sub_escolha == '3':
                print("\nBebidas disponíveis:")
                print("1 - Refrigerante - 5,00R$")
                print("2 - Suco - 7,00R$")
                print("3 - Água - 3,00R$")

                item = input("Escolha uma bebida: ")

                if item == '1':
                    carrinho.append("Refrigerante")
                    print("Refrigerante adicionado ao carrinho.")

                elif item == '2':
                    carrinho.append("Suco")
                    print("Suco adicionado ao carrinho.")

                elif item == '3':
                    carrinho.append("Água")
                    print("Água adicionada ao carrinho.")

                else:
                    print("Opção inválida, tente novamente.")

            # Voltar ao menu principal
            elif sub_escolha == '0':
                print("Voltando ao menu principal...")
                break

            else:
                print("Opção inválida.")

    # 4 - CARRINHO
    elif escolha == '4':
        print("\n--- Seu Carrinho ---")

        if len(carrinho) == 0:
            print("Seu carrinho está vazio.")
        else:
            for item in carrinho:
                print(f"- {item}")

    # 5 - REMOVER INGREDIENTES
    elif escolha == '5':
        print("\n--- Opção de remover ingredientes ---")
        print("Exemplo: tirar cebola, tomate ou molho...")
        remover = input("O que deseja remover do lanche? ")
        print(f"{remover} removido!")

    # 6 - FINALIZAR PEDIDO
    elif escolha == '6':
        print("\n--- Finalizar Pedido ---")

        cep = input("CEP: ")
        endereco = input("Endereço: ")
        numero = input("Número da casa: ")
        referencia = input("Ponto de referência: ")
        pagamento = input("Forma de pagamento: ")

        print("\nPedido finalizado com sucesso!")
        print("Seu pedido chegará em breve.")

        print("1 - Sim")
        print("2 - Não")
        salvar = input("Deseja salvar as informações para a próxima compra? ")

        if salvar == '1':
            print("Informações salvas para a próxima compra.")

        elif salvar == '2':
            print("Informações não salvas.")

        else:
            print("Opção inválida, tente novamente.")

    # 7 - CUPOM
    elif escolha == '7'a:
        print("\nCupom disponível:")
        print("A cada compra você acumula 5% de desconto para o próximo pedido.")

    # 8 - CHAT DA LOJA
    elif escolha == '8':
        sugestao = input("\nDigite sua sugestão para a loja: ")
        print("Obrigado pela sugestão!")

    # 9 - FEEDBACK
    elif escolha == '9':
        nota = input("\nAvalie nossa loja de 0 a 5: ")
        print("Obrigado pela avaliação!")

    # 0 - SAIR
    elif escolha == '0':
        print("Saindo do sistema. Até logo!")
        break

    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida. Tente novamente.")
