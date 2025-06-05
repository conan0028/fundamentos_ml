'''
3 - Faça um dicionário com dados de 5 pessoas, tendo o nome como chave e a cor da
camisa da pessoa como valor.
'''
pessoas = {
    'Alice': 'azul',
    'Bob': 'vermelho',
    'Carlos': 'verde',
    'Diana': 'amarelo',
    'Eduardo': 'preto'
}
# Exibindo o dicionário
for nome, cor in pessoas.items():
    print(f'{nome} usa camisa {cor}.')
# Adicionando uma nova pessoa
pessoas['Fábio'] = 'branco'


