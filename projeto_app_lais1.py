'''
CRUD

HAMBURGUERIA

Este sistema irá gerenciar os pedidos de forma agil e oferecer uma experiência única 
para o atendimento da Hamburgueria

Lais, Henrique e Rychard
'''

print('\n === Sistema de Hamburgueria === \n')

import datetime

# --- CONFIGURAÇÕES INICIAIS ---
carrinho = []
cliente = {}
message_suporte = []
avaliacoes = []
historico_pedidos = [] # Para o sistema de cupom acumulativo

print('='*30)
print('  HAMBURGUERIA ')
print('='*30)

while True: 
    print('-' * 25)
    print('1. Cadastro / Login')
    print('2. Esqueceu a senha')
    print('3. Menu')
    print('4. Carrinho')
    print('5. Opções (Remover Itens)')
    print('6. Finalizar Pedido')
    print('7. Cupom')
    print('8. Chat da loja')
    print('9. Feedback')
    print('0. Sair')
    print('-' * 25)

    acessar_menu = input("\nEscolha uma opção: ")

    # 1 - CADASTRO / LOGIN
    if acessar_menu == '1':
        print("\n--- Novo Cadastro ---")
        nome = input("Nome completo: ").title().strip()
        email = input("Email: ").lower().strip()
        
        while True:
            telefone = input("Telefone (somente números): ")
            if telefone.isdigit(): break
            print("Erro: Digite apenas números.")

        cpf = input("CPF: ").replace(".", "").replace("-", "")
        cep = input("CEP: ")
        endereco = input("Endereço: ")
        
        while True:
            numero = input("Número da casa: ")
            if numero.isdigit(): break
            print("Erro: Digite apenas o número.")

        referencia = input("Ponto de referência: ")
        senha = input("Crie uma Senha: ")

        cliente = {
            "nome": nome, 
            "email": email, 
            "senha": senha,
            "endereco": f"{endereco}, {numero} - {referencia}"
        }
        print(f"\nCadastro realizado com sucesso! Bem-vindo(a), {nome}.")

    # 2 - RECUPERAÇÃO DE SENHA
    elif acessar_menu == '2':
        print("\n--- Recuperação de senha ---")
        if not cliente:
            print("Erro: Nenhum usuário cadastrado.")
            continue
            
        email_busca = input("Digite seu email cadastrado: ").lower().strip()
        if email_busca == cliente['email']:
            print("Um código foi enviado (Simulação).")
            nova_senha = input("Digite sua nova senha: ")
            cliente['senha'] = nova_senha
            print("\nSenha alterada com sucesso!\n")
        else:
            print("\nE-mail não encontrado.\n")

    # 3 - MENU
    elif acessar_menu == '3':
        while True:
            print("\n === Menu ===\n ")
            print("1. Lanches\n2. Combos\n3. Bebidas\n4. Sobremesas\n5. Voltar")
            sub_escolha = input('\nEscolha uma categoria: ')

            nome_item = ""
            preco_item = 0
            

            if sub_escolha == '1':
                print("\n[1] X-Burguer - R$15 | [2] X-Salada - R$18 | [3] X-Passa Fome - R$25")
                esc = input("\nEscolha seu lanche: ")
                if esc == '1': nome_item, preco_item = "X-Burguer", 15.00
                elif esc == '2': nome_item, preco_item = "X-Salada", 18.00
                elif esc == '3': nome_item, preco_item = "X-Passa Fome", 25.00

            elif sub_escolha == '2':
                print("\n[1] Combo Família - R$45 | [2] Combo Duplo - R$30 | [3] Combo Esfomeados - R$65")
                esc = input("\nEscolha seu combo: ")
                
                if esc == '1': nome_item, preco_item = "Combo Família", 45.00
                elif esc == '2': nome_item, preco_item = "Combo Duplo", 30.00
                elif esc == '3': nome_item, preco_item = "Combo Esfomeados", 65.00

            elif sub_escolha == '3':
                print("\n[1] Refrigerante - R$5 | [2] Suco - R$7 | [3] Água - R$3")
                esc = input("\nEscolha sua bebida: ")
             
                if esc == '1': nome_item, preco_item = "Refrigerante", 5.00
                elif esc == '2': nome_item, preco_item = "Suco", 7.00
                elif esc == '3': nome_item, preco_item = "Água", 3.00

            elif sub_escolha == '4':
                print("\n[1] Geladinho Amendoim - R$10 | [2] Geladinho Pudim - R$12 | [3] Geladinho de Maracujá - R$8")
                esc = input("\nEscolha sua sobremesa: ")
                
                if esc == '1': nome_item, preco_item = "Geladinho Amendoim", 10.00
                elif esc == '2': nome_item, preco_item = "Geladinho Pudim", 12.00
                elif esc == '3': nome_item, preco_item = "Geladinho de Maracujá", 8.00

            elif sub_escolha == '5':
                break

            if nome_item != "":
                obs = input(f"Deseja personalizar o {nome_item}? (S/N): ").upper()
                detalhes = "Sem observações" 
                if obs == 'S':
                    detalhes = input("\nDeseja fazer alguma alteração: ")
                carrinho.append({
                    "item": nome_item,
                    "preco": preco_item,
                    "obs": detalhes
                })
                print(f"\n>> {nome_item} adicionado ao carrinho!")


    # 4 - VISUALIZAR CARRINHO
    elif acessar_menu == '4':
        print("\n === SEU CARRINHO ===")
        if not carrinho:
            print("\nSeu carrinho está vazio.")
        else:
            total_carrinho = 0
            for i, produto in enumerate(carrinho, 1):
                print(f"{i}. {produto['item']} - R$ {produto['preco']:.2f} | Obs: {produto['obs']}")
                total_carrinho += produto['preco']
            print("-" * 25)
            print(f"\nTOTAL ATUAL: R$ {total_carrinho:.2f}")
            print("-" * 25)

    # 5 - REMOVER ITENS
    elif acessar_menu == '5':
        if not carrinho:
            print('\nCarrinho vazio.')
        else:
            print('\n1. Remover item específico | 2. Limpar tudo')
            sub = input('\nEscolha o seu item: ')
            if sub == '1':
                for i, p in enumerate(carrinho, 1): print(f"{i}. {p['item']}")
                idx = int(input("Número para remover: "))
                removido = carrinho.pop(idx - 1)
                print(f"\n>> {removido['item']} removido.")

            elif sub == '2':
                carrinho.clear()
                print(">> Carrinho vazio.")

    # 6 - FINALIZAR PEDIDO
    elif acessar_menu == '6':
        if not carrinho:
            print('\nCarrinho vazio! Adicione itens primeiro.')
        else:
            total = sum(item['preco'] for item in carrinho)
            print(f'\nTotal a pagar: R$ {total:.2f}')
            if cliente:
                print(f"Entrega para: {cliente['nome']} em {cliente['endereco']}")
            pagamento = input('Pagamento (1. Cartão | 2. Pix | 3. Dinheiro): ')
            print("=" *25)
            print('\nPedido enviado para a cozinha! Obrigado!')
            print("=" *25)
            historico_pedidos.append(total) # Salva para o cupom
            carrinho.clear()

    # 7 - CUPOM de 5%
    elif acessar_menu == '7':
        print("\n === Cupom de Desconto ===")
        if not carrinho:
            print("\nAdicione itens ao carrinho primeiro para aplicar o cupom.")
        else:
            confirmar = input("\nVocê tem um cupom de 5%. Aplicar? (S/N): ").upper()
            if confirmar == 'S':
                for item in carrinho:
                    item['preco'] *= 0.95

                # 2. Calculamos o novo total somando os preços já com desconto
                novo_total = sum(item['preco'] for item in carrinho)

                print("Desconto de 5% aplicado em todos os itens do carrinho!")
                print('-' * 25)
                print(f"Novo total: R$ {novo_total:.2f}")
                print('-' * 25)

    # 8 - CHAT breve
    elif acessar_menu == '8':
        print("\n === Chat da Loja ===")
        duvida = input("\nComo podemos ajudar? ")
        message_suporte.append(duvida)
        print("\n[Sistema]: Mensagem enviada! Protocolo: #12345")

    # 9 - FEEDBACK da loja
    elif acessar_menu == '9':
        print("\n === Feedback ===")
        while True:
            nota = input("De 0 a 5, qual nossa nota? ")
            if nota in ['0','1','2','3','4','5']: break
            print("Digite uma nota válida entre 0 e 5.")
        coment = input("Deixe seu comentário: ")
        avaliacoes.append({"nota": nota, "comentario": coment})
        print("\nObrigado pelo seu feedback!")

    # 0 - SAIR
    elif acessar_menu == '0':
        print("\nObrigado por visitar a Hamburgueria!  Volte sempre!")
        break

    else:
        print("Opção inválida. Tente novamente.")
