'''
5 - Crie um dicionário vazio filmes = { }. Utilize o nome de um filme como chave. E, como
valor, outro dicionário contendo o vilão e o ano em que o filme foi lançado. Preencha 5
filmes.
'''
filmes = {}
filmes['O Senhor dos Anéis'] = {'vilão': 'Sauron', 'ano': 2001}
filmes['Harry Potter e a Pedra Filosofal'] = {'vilão': 'Voldemort', 'ano': 2001}
filmes['O Rei Leão'] = {'vilão': 'Scar', 'ano': 1994}
filmes['Star Wars: Episódio IV - Uma Nova Esperança'] = {'vilão': 'Darth Vader', 'ano': 1977}
filmes['Jurassic Park'] = {'vilão': 'Hammond', 'ano': 1993}
# Exibindo o dicionário de filmes
for filme, detalhes in filmes.items():
    print(f'Filme: {filme}, Vilão: {detalhes["vilão"]}, Ano: {detalhes["ano"]}')