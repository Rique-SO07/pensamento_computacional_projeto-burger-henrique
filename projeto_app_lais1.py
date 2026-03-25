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
print('6. Finalizar Pedido')
print('7. Cupom')
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
        while True:
            print("\n === Menu === \n")
            print("1. Lanches")
            print("2. Combos")
            print("3. Bebidas")
            print("4. Voltar ao meu principal")


            sub_escolha = input('Escolha uma categoria: ')


            nome_item = ""
            preco_item = 0


            if sub_escolha == '1':
                print("\n1. X-Burguer (R$ 15,00) | 2. X-Salada (R$ 18,00) | 3. X-Bacon (R$ 20,00)")
                escolha_lanche = input("Escolha o número do lanche (ou 0 para voltar): ")
                if escolha_lanche == '1':
                    nome_item, preco_item = "X-Burguer", 15.00
                elif escolha_lanche == '2':
                    nome_item, preco_item = "X-Salada", 18.00
                elif escolha_lanche == '3':
                    nome_item, preco_item = "X-Bacon", 20.00


            elif sub_escolha == '2':
                print("\n1. Combo Família (R$ 45,00) | 2. Combo Duplo (R$ 30,00)")
                escolha_combo = input("Escolha o combo: ")
                if escolha_combo == '1':
                    nome_item, preco_item = "Combo Família", 45.00
                elif escolha_combo == '2':
                    nome_item, preco_item = "Combo Duplo", 30.00


            elif sub_escolha == '3':
                print("\n1. Refrigerante (R$ 5,00) | 2. Suco (R$ 7,00) | 3. Água (R$ 3,00)")
                escolha_bebida = input("Escolha a bebida: ")
                if escolha_bebida == '1':
                    nome_item, preco_item = "Refrigerante", 5.00
                elif escolha_bebida == '2':
                    nome_item, preco_item = "Suco", 7.00
                elif escolha_bebida == '3':
                    nome_item, preco_item = "Água", 3.00


            elif sub_escolha == '4':
                break


            # Se um item foi selecionado, pergunta a personalização
            if nome_item != "":
                obs = input(f"Deseja personalizar o {nome_item}? (S/N): ").upper()
                detalhes = "Sem observações"
                if obs == 'S':
                    detalhes = input("Digite as alterações (ex: Sem cebola, ponto bem passado): ")
               
                carrinho.append({
                    "item": nome_item,
                    "preco": preco_item,
                    "obs": detalhes
                })
                print(f"\n>> {nome_item} adicionado ao carrinho!")


    # --- VISUALIZAR CARRINHO ---
    elif acessar_menu == '4':
        print("\n === SEU CARRINHO === \n")
        total = 0
        
        if not carrinho:
            print("Seu carrinho está vazio.")
        else:
            for i, produto in enumerate(carrinho):
                print(f'{i + 1}. {produto['item']} - R$ {produto['preco']:.2f}')
                print(f'   Obs: {produto['obs']}')
                total += produto['preco']


            print("-" * 25)
            print(f"TOTAL DO PEDIDO: R$ {total:.2f}")
            print("-" * 25)
     
     # --- GERENCIAR ITENS (REMOVER) ---
    elif acessar_menu == '5':
        if not carrinho:
            print('\nNada para gerenciar. Carrinho está vazio.')
        else:
            print('\n1. Remover um item específico')
            print('2. Esvaziar carrinho')
            sub_opc = input('Escolha: ')


            if sub_opc == '1':
                for i, produto in enumerate(carrinho):
                    print(f"{i + 1}. {produto['item']}")
                idx = int(input("Número do item para remover: "))
                removido = carrinho.pop(idx - 1)
                print(f">> {removido['item']} removido.")
            elif sub_opc == '2':
                carrinho.clear()
                print(">> Carrinho vazio.")


    # --- FINALIZAR PEDIDO ---            
    elif acessar_menu == '6':
        print("\n === Finalizar Pedido === \n")
        if not carrinho:
            print('\nO carrinho esstá vazio1 Adicione itens antes de finalizar.')
        else:
            total = sum(item['preco'] for item in carrinho)
            print(f'\nTotal a pagar: R$ {total:.2f}')
            print('Formas de pagamento: 1. Cartão | 2. Pix | 3. Dinheiro')
            pagamento = input('Escolha a forma: ')
            print('\nPedido enviado para a cozinha! Obrigado pela preferência.')
            carrinho.clear() #limpa o carrinho após finalizar

    elif acessar_menu == '7':
        print("\n === Cupom === \n")
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
