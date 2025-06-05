'''
2 - Faça um programa que crie uma lista de 10 elementos aleatórios, calcule e imprima:
a) a média dos elementos;
b) o maior e menor elemento;
c) a quantidade de elementos positivos e a quantidade de elementos
negativos;
d) quantos elementos estão abaixo da média e quantos estão acima;
e) desvio padrão;
'''
import random

# n = número de elementos da lista
n = 10
# Cria uma lista de 10 elementos aleatórios entre -50 e 50
lista_aleatoria = [random.randint(-50, 50) for elemento in range(n)]
print('lista: ', lista_aleatoria)

# Soma todos os elementos da lista
soma = 0
for elemento in lista_aleatoria:
    soma += elemento

# Calcula a média dos elementos
media = soma / n
print(f"A média dos elementos é: {media}")

# Encontra o maior e menor elemento
maior = lista_aleatoria[0]
menor = lista_aleatoria[0]
for elemento in lista_aleatoria:
    if elemento > maior:
        maior = elemento
    if elemento < menor:
        menor = elemento
print(f"O maior elemento é: {maior}")
print(f"O menor elemento é: {menor}")
'''
Poderia usar as funções max() e min() para encontrar o maior e menor elemento
max = max(lista_aleatoria)
min = min(lista_aleatoria)
'''

# Conta a quantidade de elementos positivos e negativos
positivos = 0
negativos = 0
for elemento in lista_aleatoria:
    if elemento >= 0:
        positivos += 1
    if elemento < 0:
        negativos += 1
print(f"Quantidade de elementos positivos: {positivos}")
print(f"Quantidade de elementos negativos: {negativos}")

# Conta quantos elementos estão abaixo e acima da média
abaixo_media = 0
acima_media = 0
for elemento in lista_aleatoria:
    if elemento < media:
        abaixo_media += 1
    if elemento > media:
        acima_media += 1
print(f"Quantidade de elementos abaixo da média: {abaixo_media}")
print(f"Quantidade de elementos acima da média: {acima_media}")
'''
Poderia usar as funções filter() e len() para contar os elementos abaixo e acima da média
abaixo_media = len(list(filter(lambda x: x < media, lista_aleatoria)))
acima_media = len(list(filter(lambda x: x > media, lista_aleatoria)))
'''

'''
Desvio Padrão = √[ (1/(n-1)) * Σ(v[i] - m)² ]
onde:
v[i] = cada elemento da lista
m = média
n = número de elementos da lista
'''
# Calcula o desvio padrão amostral
soma_quadrados = 0
for elemento in lista_aleatoria:
    # Calcula a soma dos quadrados das diferenças entre cada elemento e a média
    # e armazena na variável soma_quadrados
    # Σ(v[i] - m)²
    soma_quadrados += (elemento - media) ** 2
# Calcula a variância
variancia = soma_quadrados / (n - 1)
# Calcula o desvio padrão
s = variancia ** 0.5
print(f"O desvio padrão é: {s}")
'''
Poderia usar a função statistics.stdev() para calcular o desvio padrão
import statistics
s = statistics.stdev(lista_aleatoria)
print(f"O desvio padrão é: {s}")
'''
import statistics
s = statistics.stdev(lista_aleatoria)
print(f"O desvio padrão é: {s:.2f}")

