# Aula 1.3 - Estrutura de Dados
# Tuplas: Slides 16-25

# Tuplas são listas imutáveis
# Tuplas são listas que não podem ser alteradas
# Tuplas são criadas usando parênteses e não colchetes
aluno = ('Ana Maria', 2022, 1)
print(aluno[0])
print(aluno[1])
print(aluno[2])

# aluno[1] = 2023 # Erro, não podemos alterar o valor de uma tupla
aluno1 = ('Bernado', 2022, 1)
aluno2 = ('Bianca', 2023, 1)
# criando outra tupla com ano de 2023
aluno1 = (aluno1[0], 2023, aluno1[2])
print(aluno1, '\n')

print('concatenando tuplas:')
alunos = aluno1 + aluno2
print(alunos, '\n')

print('repetindo tuplas:')
alunosR1 = aluno1 * 2
print(alunosR1)
alunosR2 = aluno2 * 4
print(alunosR2)
print('\nTupla alunos:',alunos)
print()
# Pequenos detalhes

tupla1 = () # tupla vazia
tupla2 = (1) # Não é uma tupla, é um número inteiro
tupla3 = (1,) # tupla com um elemento
tupla4 = (1, 2) # tupla com dois elementos

print('tupla1:', tupla1)
print('tupla2:', tupla2)
print('tupla3:', tupla3)
print('tupla4:', tupla4)
print()

# Tuplas podem ser "desempacotadas" para variáveis distintas
aluno1 = ('Bernado', 2022, 1)

# Desempacotando a tupla
(nome, ano, semestre) = aluno1
print('Nome:', nome)
print('Ano:', ano)
print('Semestre:', semestre)
print()

# Criar e desempacotar uma tupla pode ocorrer simultaneamente
# Permite fazer SWAP de variáveis
a = 2
b = 3
print('Antes do SWAP:')
print('a =', a, ' e b =', b)
a, b = b, a
print('Depois do SWAP:')
print('a =', a, ' e b =', b)

