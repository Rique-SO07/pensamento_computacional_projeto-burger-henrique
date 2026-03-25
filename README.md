# pensamento_computacional_projeto_hamburgueria

# 🍔🥤 Sistema de Gerenciamento - Hamburgueria

Este é um projeto em **Python** desenvolvido para gerenciar pedidos de forma ágil, oferecendo uma experiência completa de autoatendimento. 
O software foca em praticidade e organização de dados, desde o cadastro de usuários até a gestão de feedbacks.

## 🚀 Funcionalidades

O sistema está estruturado em módulos que simulam o fluxo real de uma operação de Food Service:

1.  **Cadastro e Segurança:** Registro detalhado de clientes (CPF, CEP, Endereço) e módulo de recuperação de senha.
2.  **Cardápio Interativo:** Divisão por categorias (Lanches, Combos, Bebidas e Sobremesas) com seleção via teclado.
3.  **Personalização de Pedidos:** Opção para o cliente adicionar observações em cada item (ex: "Sem cebola").
4.  **Gestão de Carrinho:** Visualização de itens, preços individuais, soma total e opção para remover itens ou limpar o carrinho.
5.  **Sistema de Cupom:** Aplicação dinâmica de desconto (5%) sobre o valor total da compra.
6.  **Atendimento e Feedback:** Chat de suporte com protocolo automático e sistema de avaliação com notas e comentários.

## 🛠️ Diferenciais Técnicos e Estruturas

O projeto se destaca por aplicar conceitos avançados de manipulação de dados em Python:

* **Dicionários Compostos (`{}`):** Utilizamos para representar o `cliente` e os itens do `carrinho`.
Isso permite associar múltiplas informações (nome, preço, observação) a uma única variável, facilitando a organização.
* **Tratamento e Sanitização de Dados:** * Uso de `.strip()`, `.title()` e `.lower()` para padronizar as entradas e evitar erros de busca.
* Uso de `.replace()` para limpar pontuações de CPF e CEP, garantindo que apenas números essenciais sejam processados.
* **Validação com Laços de Repetição:** O sistema utiliza `while True` combinado com `.isdigit()` para forçar a entrada correta de
dados numéricos (Telefone, Número da casa), impedindo que o programa feche por erros de digitação.
* **Lógica de Desconto Iterativa:** O cupom de desconto percorre cada item da lista do carrinho e recalcula o preço em tempo real
(`item['preco'] *= 0.95`), demonstrando domínio sobre estruturas de repetição e aritmética.
* **Persistência em Tempo de Execução:** Uso de listas como `avaliacoes` e `message_suporte` para criar um log de interações durante o uso do programa.

## 📋 Como Executar

1.  Certifique-se de ter o **Python 3.x** instalado.
2.  Baixe o arquivo do projeto (`hamburgueria.py`).
3.  Abra o terminal na pasta do arquivo.
4.  Execute o comando:
   ```bash
   python hamburgueria.py
   ```

## 👥 Participantes
* **Lais Renata**
* **Henrique Souza**
* **Rychard Rodrigues**

---

*Desenvolvido como projeto de aprendizado em Python, focado em lógica de programação e estruturas de dados.*

---

