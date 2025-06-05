'''
8 - Escreva uma função que receba uma lista de elementos e retorne a quantidade de
elementos duplicados na lista.
'''
def contar_duplicados(lista):
    contagem = 0
    # permite ver se o elemento já foi visto
    elementos_vistos = set()

    for elemento in lista:
        # se o elemento já foi visto, incrementa a contagem
        if elemento in elementos_vistos:
            contagem += 1
        else:
            # se não foi visto, adiciona ao conjunto de vistos
            elementos_vistos.add(elemento)
    # retorna a contagem de elementos duplicados
    return contagem

# Exemplo de uso
lista_exemplo = [1, 2, 3, 2, 4, 5, 1, 6, 7, 8, 8]
print("Quantidade de elementos duplicados:", contar_duplicados(lista_exemplo))
