
import adivinhacao
import Forca


def escolhe_jogo():

    print("Escolha o seu jogo")

    jogo = int(input("(1) Adivinhação (2) Forca"))

    if(jogo == 2):
        print("Jogando forca")
        Forca.jogar()
    elif(jogo == 1):
        print("Jogando Adivinhção")
        adivinhacao.jogar()


if(__name__ == "__main__"):
    escolhe_jogo()
