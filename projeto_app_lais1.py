'''
CRUD

HAMBURGUERIA

EEste sistema irá gerenciar os pedidos de forma agil e oferecer uma experiência única 
para o atendimento da Hamburgueria 
Lais
'''

print('\n === Sistema de Hamburgueria === \n')

print('1. Cadastro')
print('1.1 Login')
print('2. Esqueceu a senha')
print('3. Menu')
print('4. Carrinho')
print('5. Opições')
print('6. Cupom')
print('7. Finalizar pedido')
print('8. Chat da loja')
print('9. Feedback')
print('0. Sair')

while True:
    acessar_menu = input("\n escolha uma opção:")

    if acessar_menu == '1':
        print("\n === Cadastro === \n")

        nome_client = input("Digite seu nome: ")
        numero_client= input("Digite seu número de telefone:")
        email_client = input("Digite seu email: ")
        cpf_client = input("Digite seu CPF: ")
        endereco_client = input("Digite seu endereço: ")
        cep_client = input("Digite o CEP da sua rua: ")
        senha = input("Digite sua senha: ")

        print(f"Cadastro realizado com sucesso! Bem-vindo, {nome_client}!")

    elif acessar_menu == '1.1':
        print("\n === Login === \n")
        email_client = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        print(f"Login realizado com sucesso! Bem-vindo de volta, {email_client}!")

    elif acessar_menu == '2':
        print("\n === Esqueci minha senha === \n")
        email_client = input("Digite seu email para recuperar a senha: ")
        print(f"Um email de recuperação de senha foi enviado para {email_client}. Por favor, verifique.")

    elif acessar_menu == '3':
        print("\n === Menu === \n")
        print("1. Hambúrgueres")
        print("2. Acompanhamentos")
        print("3. Bebidas")
        print("4. Sobremesas")

        while True:
            print("\n=== Menu ===")
            print("1. Lanches")
            print("2. Combos")
            print("3. Bebidas")
            print("4. Voltar ao menu principal")
            
            sub_escolha = input("Escolha uma opção do menu: ")
            
            if sub_escolha == '1':
                print("Lanches disponíveis:")
                print("- X-Burguer - R$ 15,00")
                print("- X-Salada - R$ 18,00")
                print("- X-Bacon - R$ 20,00")
            
            elif sub_escolha == '2':
                print("Combos disponíveis:")
                print("- Combo Família - R$ 45,00")
                print("- Combo Duplo - R$ 30,00")
                print("- Combo Kid - R$ 20,00")
            
            elif sub_escolha == '3':
                print("Bebidas disponíveis:")
                print("- Refrigerante - R$ 5,00")
                print("- Suco - R$ 7,00")
                print("- Água - R$ 3,00")
            
            elif sub_escolha == '4':
                print("Voltando ao menu principal...")
                break
            
            else:
                print("Opção inválida. Tente novamente.")
                #Aqui consegui aprofundar minhas opções, colocando um outro While True


    elif acessar_menu == '4':
        print("\n === Carrinho === \n")
        #ficara amazenado os itens selecionados

    elif acessar_menu == '5':
        print("\n === Opções === \n")
        #opções de personalização do pedido ou se precisar retirar algum ingrediente


    elif acessar_menu == '6':
        print("\n === Cupom === \n")
        #se preferir usar um cupom de desconto

    elif acessar_menu == '7':
        print("\n === Finalizar pedido === \n")
        #finalização do pedido, escolha da forma de pagamento

    elif acessar_menu == '8':
        print("\n === Chat da loja === \n")
        #chat para tirar dúvidas ou fazer reclamações

    elif acessar_menu == '9':
        print("\n === Feedback === \n")
        #espaço para o cliente deixar um feedback sobre a experiência

    elif acessar_menu == '0':
        print("\n Obrigado por visitar nossa hamburgueria! Volte sempre! \n")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")