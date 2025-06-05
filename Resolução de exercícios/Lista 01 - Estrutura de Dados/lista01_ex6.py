'''
6 - Faça uma função que, dada uma tupla com N notas, retorne a média das notas.
'''
# Função para calcular a média das notas em uma tupla
def calcular_media(notas):
    if not notas:  # Verifica se a tupla está vazia
        return 0.0
    return sum(notas) / len(notas)

# usuario insere as notas
notas = ()
while True:
    nota = input('Digite uma nota (ou "sair" para finalizar): ')
    # função .lower() para tratar casesensitive e sair do loop
    if nota.lower() == 'sair':
        break
    try:
        nota_float = float(nota)
        notas += (nota_float,)  # Adiciona a nota à tupla
    except ValueError:
        print('Por favor, insira um número válido.')

# Testando a função com uma tupla de notas
# notas = (7.5, 8.0, 6.5, 9.0, 10.0)
media = calcular_media(notas)
print(f'A média das notas {notas} é: {media:.2f}')

