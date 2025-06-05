'''
1 - Faça um programa que leia duas listas de 10 posições (utilizando a função input) e
construa outra lista contendo, nas posições pares, os valores da primeira e, nas posições
ímpares, os valores da segunda.
'''
input_list1 = []
input_list2 = []
output_list = []
for i in range(10):
    input_list1.append(int(input(f"Digite o {i+1}º valor da primeira lista: ")))
    input_list2.append(int(input(f"Digite o {i+1}º valor da segunda lista: ")))
for i in range(10):
    if i % 2 == 0:
        output_list.append(input_list1[i])
    else:
        output_list.append(input_list2[i])
print(f"A lista resultante é: {output_list}")
