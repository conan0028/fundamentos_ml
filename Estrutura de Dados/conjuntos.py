# Aula 1.3 - Estrutura de Dados
# Conjuntos (Sets): Slides 36-43

# Conjuntos são coleções não ordenadas de elementos únicos.
# Eles são mutáveis e não permitem duplicatas.
# Os conjuntos são definidos com chaves {} ou com a função set().
# Exemplo de conjunto

# meu_conjunto = {'maçã', 'banana', 'cereja'}
meu_conjunto = set(['maçã', 'banana', 'cereja'])
print(meu_conjunto)  # Saída: {'maçã', 'banana', 'cereja'}

# meu_conjunto.update([True, 1, 2]) # Adiciona elementos ao conjunto
# True == 1, remove a duplicata
# novos_elementos = {True, 1, 2}
# meu_conjunto.update(novos_elementos) # Adiciona novos elementos ao conjunto
# print(meu_conjunto)  # Saída: {'maçã', 'banana', 'cereja', True, 1, 2}

# Criando conjuntos vazios
conjunto_vazio = set()  # Conjunto vazio
print(conjunto_vazio)

# Adicionando ou removendo elementos ao conjunto
# add(item)
# remove(item)
# discard(item)
meu_conjunto.add(1)
meu_conjunto.add(2)
print(meu_conjunto)
meu_conjunto.remove(1)  # Remove o elemento 1
print(meu_conjunto)  # Saída: {'maçã', 'banana', 'cereja', 2}
# Se o elemento não estiver presente, discard não retorna nada
meu_conjunto.discard(3)  # Remove o elemento 3
print(meu_conjunto)  # Saída: {'maçã', 'banana', 'cereja'}

# Para acessar os itens, você precisa iterar sobre o conjunto
for fruta in meu_conjunto:
    print(fruta)  # Saída: 'maçã', 'banana', 'cereja', 2

# Adicionando um conjunto a outro conjunto
meu_conjunto = set (['maçã', 'banana', 'cereja'])
tropical = {'abacaxi', 'manga', 'mamão'}
# Adicionando elementos de tropical a meu_conjunto
meu_conjunto.update(tropical)
print(meu_conjunto)  # Saída: {'maçã', 'banana', 'cereja', 'abacaxi', 'manga', 'mamão'}

# Adicionando uma lista a um conjunto
meu_conjunto = set (['maçã', 'banana', 'cereja'])
lsita_frutas = ['kiwi', 'laranja']
meu_conjunto.update(lsita_frutas)
print(meu_conjunto)  # Saída: {'maçã', 'banana', 'cereja', 'kiwi', 'laranja'}

# pop() Remove e retorna um elemento aleatório do conjunto
# Se o conjunto estiver vazio, gera um erro KeyError
meu_conjunto.pop()  # Remove e retorna um elemento aleatório
print(meu_conjunto)  # Saída: {'banana', 'cereja', 'kiwi', 'laranja'}
meu_conjunto.clear()  # Limpa o conjunto
print(meu_conjunto)  # Saída: set()
del meu_conjunto  # Apaga o conjunto

# Operações com conjuntos

# União (|): Combina dois conjuntos, removendo duplicatas / equivalente a update
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
# set3 = set1 | set2  # União
set3 = set1.union(set2)  # Outra forma de fazer a união
lista_ordenada = sorted (set3, key=str)  # Ordena o conjunto
print('lista_ordenada', lista_ordenada)  # Saída: ['1', '2', '3', 'a', 'b', 'c']

print('\nunion: ', set3)  # Saída: {'a', 'b', 'c', 1, 2, 3}

# Interseção (&): Retorna os elementos comuns entre dois conjuntos
# intersecao = set1 & set2  # Interseção
# intersection_update()
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
# intersecao = x & y  # Interseção
intersecao = x.intersection(y)  # Outra forma de fazer a interseção
print('intersecao: ', intersecao)  # Saída: {'apple'}

# Disjunção exclusiva (Diferença simétrica)
# é o conjunto de elementos que pertencem a um ou outro conjunto, mas não a ambos simultaneamente.
# diferença_simetrica = set1 ^ set2  # Diferença simétrica
# symmetric_difference_update()
# diferença_simetrica = set1.symmetric_difference(set2)  # Outra forma de fazer a diferença simétrica
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
diferença_simetrica = x ^ y  # Diferença simétrica
print('diferença_simetrica: ', diferença_simetrica)
# Saída: {'banana', 'google', 'microsoft', 'cherry'}
# atualiza o conjunto x com a diferença simétrica entre x e y
x.symmetric_difference_update(y)
print('x_update: ', x)
