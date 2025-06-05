# Aula 1.3 - Estrutura de Dados
# Listas: Slides 04 - 15

lista_compras = [ 'banana', 'maçã', 'laranja']
print(lista_compras)

#Para acessarmos um item da lista
# Nome da lista + [posição do item]
print(lista_compras[1])

# Buscando posição [0]
print(lista_compras[0])

# print(lista_compras[3]) # Erro de indexação

# acessando a lista com números negativos
print(lista_compras[-1])

'''
posição do números positivos
[0, 1, 2]
posição do números negativos
[-3, -2, -1]
'''

lista_compras.append('abacaxi') # Adiciona um item no final da lista
lista_compras.insert(0, 'morango') # Adiciona um item na posição escolhida
print(lista_compras)

del lista_compras[0] # Deleta um item da lista
print(lista_compras)

# remove o último item da lista,
# mas não o exclui
lista_compras.pop() # remove 'abacaxi'

# Remove um item da lista pelo seu valor e não pela posição
lista_compras.remove('laranja')
print(lista_compras)

lista_compras.insert(1, 'laranja')

lista_compras.append('carro')
print(lista_compras)

del lista_compras[3] # Deleta o item na posição 3
print(lista_compras)

# insere o item na posição 1
lista_compras.insert(1,'carro')
print(lista_compras)

# Gerando uma lista com sequência de números
seq = list(range(5))
print(seq)

lista_compras = ['banana', 'laranja', 'maçã']
# Obter o tamanho da lista
print(len(lista_compras))






