# Aula 1.3 - Estrutura de Dados
# Dicionário: Slides 26-35

# Dicionários são estruturas de dados que armazenam pares de chave-valor.
# Eles são mutáveis, não ordenados e indexados por chaves únicas.
# Os dicionários são definidos com chaves {} e os pares de chave-valor são separados por vírgulas.

# nome_do_dicionario = {chave1: conteudo1, ..., chaveN: conteudoN}

# Exemplo de dicionário
inventario = {
    "Miojo": 10,
    "Ovo": 12,
    "Pão": 5
}
# Acessando valores em um dicionário
print(inventario["Miojo"])  # Saída: 10

dict = {'um': 'one', 'dois': 'two', 'três': 'three'}
print(dict)

# criando um dicionário vazio
dicionario_vazio = {}
print(dicionario_vazio)

# Acessando um valor em um dicionário
print(dict['um'])  # Saída: one

# Alterando um valor em um dicionário
dict['um'] = 'one updated'
print(dict)
# retornar ao valor original
dict['um'] = 'one'

# Adicionando elementos no dicionário
dict['quatro'] = 'four'
print(dict)

# forma geral de uso dos métodos
# nome_do_dicionario = nome_metodo(argumentos)

# clear() - remove todos os elementos do dicionário
dict.clear()
print(dict)  # Saída: {}
# copy() - retorna uma cópia do dicionário
dict = {'um': 'one', 'dois': 'two', 'três': 'three', 'quatro': '4'}
dict2 = dict.copy()
print(dict2)  # Saída: {'um': 'one', 'dois': 'two', 'três': 'three'}
print(id(dict))  # Saída: id do dicionário original
print(id(dict2))  # Saída: id da cópia do dicionário

# Obter o conteúdo de uma chave.
# get() - retorna o valor associado a uma chave, ou None se a chave não existir
print(dict.get('um'))  # Saída: one
# print(dict['cinco']) # Saída: KeyError
print(dict.get('cinco', 'five'))  # Saída: five
print(dict)

# Métodos sobre dicionários

# items() - retorna uma lista de tuplas com todos os pares chave-valor do dicionário
print(dict.items())  # Saída: dict_items([('um', 'one'), ('dois', 'two'), ('três', 'three')])
# keys() - retorna uma lista com todas as chaves do dicionário
print(dict.keys())  # Saída: dict_keys(['um', 'dois', 'três'])
# values() - retorna uma lista com todos os valores do dicionário
print(dict.values())  # Saída: dict_values(['one', 'two', 'three'])

dict = {'um': 'one', 'dois': 'two', 'três': 'three'}

# pop() - remove e retorna o valor associado a uma chave
print(dict.pop('um'))  # Saída: one
# primeiro elemento removido
print(dict)

# popitem() - remove e retorna o último par chave-valor inserido no dicionário
print(dict.popitem())  # Saída: ('três', 'three')