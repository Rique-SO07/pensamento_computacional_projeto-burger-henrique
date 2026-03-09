# Definimos o dicionário (Base de dados)
preco_frutas = {
    'morango': 6.0,
    'kiwi': 7.0,
    'maracujá': 5.0,
    'abacaxi': 4.0,
    'melão': 3.0 
}
# Definimos qual fruta queremos procurar
fruta_desejada = 'morango'

# Fazemos a busca direta usando o método .get()
# O .get() tenta encontrar a fruta; se não achar, mostra 'Fruta não encontrada'
resultado = preco_frutas.get(fruta_desejada, 'Fruta não encontrada')

# Exibimos o resultado
print(f'O preço do {fruta_desejada} é R${resultado}')