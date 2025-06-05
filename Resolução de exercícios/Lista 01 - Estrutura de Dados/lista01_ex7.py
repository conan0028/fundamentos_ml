'''
7 - Escreva uma função que receba uma lista de elementos e retorne a quantidade de
elementos únicos (distintos) na lista.
'''

def contar_elementos_unicos(lista):
    # Utiliza um conjunto para armazenar elementos únicos
    # conjuntos não permitem duplicatas
    elementos_unicos = set(lista)
    # len() retorna o número de elementos únicos
    return len(elementos_unicos)

# Exemplo de uso
lista_exemplo = [1, 2, 2, 3, 4, 4, 5]
quantidade_unicos = contar_elementos_unicos(lista_exemplo)
print(f"A quantidade de elementos únicos na lista é: {quantidade_unicos}")
