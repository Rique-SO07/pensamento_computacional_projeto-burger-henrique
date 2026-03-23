'''
CRUD
# Estou fazendo com o professor Ivan
HAMBURGUERIA

Este sistema irá gerenciar os pedidos de forma agil e oferecer uma experiência única 
para o atendimento da Hamburgueria 
Henrique
'''

'''print('\n === Sistema de Hamburgueria === \n')

print('1. Cadastro')
print('1.1 Login')
print('2. Esqueceu a senha')
print('3. Menu')
print('4. Carrinho')
print('5. Opções')
print('6. Finalizar Pedido')
print('7. Cupom')
print('8. Chat da loja')
print('9. Feedback')
print('0. Sair')
'''
carrinho = []
total = 0
#Variaveis para ajudar a realizar o carrinho (adição de itens, remoção, e mais).

while True:
    print('-' *25) 
    print('1. Cadastro')
    print('1.1 Login')
    print('2. Esqueceu a senha')        
    print('3. Menu')
    print('4. Carrinho')
    print('5. Opções')
    print('6. Finalizar Pedido')
    print('7. Cupom')
    print('8. Chat da loja')
    print('9. Feedback')
    print('0. Sair')
    print('-' * 25)

    acessar_menu = input("\n Escolha uma opção: ")

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
            print("4. Sobremesas")
            print("5. Voltar ao menu principal")
            print('-' *25)


            sub_escolha = input('\nEscolha uma categoria: \n')


            nome_item = ""
            preco_item = 0


            if sub_escolha == '1':
                print("\n[1] X-Burguer - R$ 15,00 | [2] X-Salada - R$ 18,00 | [3] X-Passa fome - R$ 25,00")
                escolha_lanche = input("Escolha o número do seu lanche (ou 0 para voltar ao menu): ")

                if escolha_lanche == '1':
                    nome_item, preco_item = "X-Burguer", 15.00

                elif escolha_lanche == '2':
                    nome_item, preco_item = "X-Salada", 18.00

                elif escolha_lanche == '3':
                    nome_item, preco_item = "X-Passa fome", 25.00


            elif sub_escolha == '2':
                print("\n [1] Combo Família - R$ 45,00 | [2] Combo Duplo - R$ 30,00 | [3] Combo Kid - R$ 22,00")
                escolha_combo = input("\nEscolha seu combo: \n")

                if escolha_combo == '1':
                    nome_item, preco_item = "Combo Família", 45.00

                elif escolha_combo == '2':
                    nome_item, preco_item = "Combo Duplo", 30.00

                elif escolha_combo == '3': 
                    nome_item, preco_item = "Combo Kid", 22.00


            elif sub_escolha == '3':
                print("\n[1] Refrigerante - R$ 5,00 | [2] Suco - R$ 7,00 | [3] Água - R$ 3,00")
                escolha_bebida = input("\nEscolha sua bebida: \n")

                if escolha_bebida == '1':
                    nome_item, preco_item = "Refrigerante", 5.00
              
                elif escolha_bebida == '2':
                    nome_item, preco_item = "Suco", 7.00
              
                elif escolha_bebida == '3':
                    nome_item, preco_item = "Água", 3.00


            elif sub_escolha == '4':
                print("\n[1] Geladinho de Amendoim - R$ 10,00 | [2] Geladinho Pudim - R$ 12,00 | [3] Geladinho de Maracujá - R$ 10,00")
                escolha_bebida= input("\nEscolha sua sobremesa: \n")
              
                if escolha_bebida == '1':
                    nome_item, preco_item = "Geladinho de Amendoim", 10.00 
              
                elif escolha_bebida == '2':
                    nome_item, preco_item = "Geladinho Pudim", 12.00 
              
                elif escolha_bebida == '3':
                    nome_item, preco_item = "Geladinho de Maracujá", 10.00    

            elif sub_escolha == '5':
                print("Retornando ao menu principal...")
                break      


            # Se um item foi selecionado, pergunta a personalização
            if nome_item != "":
                obs = input(f"Deseja personalizar o {nome_item}? (S/N): ").upper()
                detalhes = "Sem observações"
                if obs == 'S':
                    detalhes = input("\nDigite as alterações (ex: Sem cebola, ponto bem passado): ")
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
            print('\nNada para gerenciar. Seu carrinho está vazio.')
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
            print('\nO carrinho esstá vazio. Adicione itens antes de finalizar.')
        else:
            total = sum(item['preco'] for item in carrinho)
            print(f'\nTotal a pagar: R$ {total:.2f}')
            print('Formas de pagamento: 1. Cartão | 2. Pix | 3. Dinheiro')
            pagamento = input('\n>>Escolha a forma de pagamento: ')

            print('\nPedido enviado para a cozinha! Obrigado pela preferência.')
            carrinho.clear() #Aqui finalizaremos o pedido com opção de pagamento.

    elif acessar_menu == '7':
        print("\n === Cupom === \n")
        print('\nVeja nossos cupons!')
        input("\nVocê tem um cupom de 5%. Deseja adicioná-lo? ")
        print('\nAplicando cupom de 5% de desconto...')
        total = total * 0.95
        total = sum(item['preco'] for item in carrinho) 
        #Esse código faz o preco ficar igual ao do carrinho.
        print('-' * 25)
        print(f"Novo total: R$ {total:.2f}")
        print('-' * 25)
       #Código para aplicar 5% de desconto nos itens que estão no carrinho.


    elif acessar_menu == '8':
        print("\n === Chat da loja === \n")
        print('\n === Entre em contato ===\n')
        mensagem = input ("\nComo podemos ajudar? Digite sua dúvida: ")
        message_suporte.append(mensagem)
        print("\n[Sistema]: Mensagem enviada com sucesso!")
        print("\n[Sistema]: Um atendente entrará em contato em breve. Protocolo: #12345")
        #Código para criar um mini chat de breve interação com o cliente.
        #chat para tirar dúvidas ou fazer reclamações

    elif acessar_menu == '9':
        print("\n === Feedback === \n")
        print('Diga-nos o que achou?')

        carrinho = []
        total = []
        message_suporte = []
        avaliacoes = []

        while True:
          nota = input ("\nDe 0 a 5, Qual nota você nos avalia?")
          if nota in ['0','1','2','3','4','5']:
             break
          
          comentario = input("\nDeixe seu comentário (opcional): ")
          print("Muito obrigado pelo sue feedback! Isso nos ajuda demais!")

          feedback_client = {
             "nota": nota,
             "comentario": comentario
          }
          avaliacoes.append(feedback_client)
          break

          #Utilizando um dicionário, consegui criar um mini sistema de feedback. 
        #espaço para o cliente deixar um feedback sobre a experiência

    elif acessar_menu == '0':
        print("\n Obrigado por visitar nossa hamburgueria! Volte sempre! \n")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")