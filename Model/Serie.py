class Serie:

    def __init__(self, nome, ano, temporada, likes):
        self.__nome = nome
        self.__ano = ano
        self.__temporada = temporada
        self.__likes = likes

    @property
    def nome(self):
        self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def duracao(self, duracao):
        self.__duracao = duracao

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1
