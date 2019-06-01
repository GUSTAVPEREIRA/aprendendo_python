class Filme:

    def __init__(self, nome, ano, duracao, likes):
        self.__nome = nome.title()
        self.__ano = ano
        self.__duracao = duracao
        self.__likes = likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def ano(self):
        return self.__ano

    def ano(self, ano):
        self.__ano = ano

    @property
    def duracao(self):
        return self.duracao

    @duracao.setter
    def duracao(self, duracao):
        self.duracao = duracao
