

def jogar():
    print("Bem vindo ao jogo da forca")
    print("Fim de jogo")
    palavra_secreta = "banana"
    enforcou = False
    acertou = False
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    print(letras_acertadas)
    while(not enforcou and not acertou):
        chute = input("Qual a letra? ")
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
               letras_acertadas[index]=letra
            index = index + 1
        letras_faltando = str(letras_acertadas.count('_'))
        print(letras_acertadas)
        print("Ainda faltam acertar {} letras".format(letras_faltando))
        if(int(letras_faltando) == 0):
            acertou = True

    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()