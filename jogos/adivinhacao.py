import random


def jogar():

    print("Bem vindo ao jogo de adivinhaçao")
    print("Qual o nivel de dificuldade?")
    print("(1) Facil (2) Medio (3) Dificil")
    pontos = 1000
    nivel = int(input("Define o nivel: "))
    numero_secreto = random.randrange(1, 101)
    round(numero_secreto)
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    rodada = 1
    for rodada in range(1, total_de_tentativas + 1):
        chute = input("Digite um numero entre 1 e 100: ")
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(chute)
        if (chute < 1 or chute > 100):
            print("Você tem que digitar um numero entre 1 e 100")
            continue
        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        if (acertou):
            print("Você acertou")
            break
        else:
            if(maior):
                print("Voce errou,e o seu chute foi maior que o segredo")
            elif(menor):
                print("Voce errou, e o seu chute foi menor que o segredo")
            rodada = rodada + 1
            pontos_perdidos = numero_secreto - chute
            pontos = pontos - abs(pontos_perdidos)

    print("Fim do jogo")
    print("Voce fez {} pontos: ".format(pontos))


if(__name__ == "__main__"):
    jogar()
