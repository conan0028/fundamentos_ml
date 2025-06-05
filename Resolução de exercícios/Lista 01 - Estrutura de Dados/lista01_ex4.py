'''
4 - Crie um dicionário vazio semana = { } e o complete com uma chave para cada dia da
semana, tendo como seu valor uma lista com as aulas que você tem nesse dia (sábado e
domingo recebem listas vazias, ou você tem aula?).
'''
semana = {}
semana['segunda-feira'] = 'POOBD','LFA', 'PAA2'
semana['terça-feira'] = 'Sistemas Operacionais 2'
semana['quarta-feira'] = 'LFA', 'REDES 2'
semana['quinta-feira'] = 'POOBD','LFA', 'PAA2'
semana['sexta-feira'] = 'Sistemas Operacionais 2'
semana['sábado'] = 'REDES 2'
semana['domingo'] = []

for dia_da_semana, aula in semana.items():
    if (dia_da_semana != 'domingo'):
        print(f'{dia_da_semana} tenho aula de: {aula}')
    else:
        print(f'{dia_da_semana} não tenho aula!')