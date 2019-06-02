class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.duracao} min - {self.ano} - {self.likes} likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} - {self.temporadas} temporada - {self.ano} - {self.likes} likes'

class Playlist:
    def __init__(self, nome, programa):
        self.nome = nome
        self._programa = programa

    def tamanho(self):
        return len(self.programa)

    def __getitem__(self, item):
        return self._programa[item]

    def __add__(self, item):
        if item == 1:
            self.__add__(item)


    @property
    def listagem(self):
        return self._programa

    @property
    def tamanho(self):
        return len(self._programa)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
tmep = Filme('Todo mundo em pánico 3',1995, 80)
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

filmes_series = [vingadores]


playlist = Playlist("Filmes e series", filmes_series)


print (f'Tamanho do playlist: {len(playlist.listagem)}')

for programas in playlist.listagem:
    print(programas)
