class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas

vingadores = Filme("Vingadores - guerra infinita", 2018, 160)
print(f"Nome: {vingadores.nome}, Ano: {vingadores.ano}, Temporadas: {vingadores.duracao}")
reign = Serie("Reign", 2013, 4)
print(f"Nome: {reign.nome}, Ano: {reign.ano}, Temporadas: {reign.temporadas}")