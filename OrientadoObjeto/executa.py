from conta import Conta
from datas import Data


def __main__():
    conta = Conta(1, "Gustavo", 55.0, 1000.0)
    conta2 = Conta(2, "Pedro", 50.0, 1000.0)
    d = Data(21, 11, 2007)

    op = 1
    while(op != 0):
        op = int(input("\nExtrado = 1, Sacar = 2, Depositar = 3, Ver Data = 4, Transfere = 5\n Opção: "))
        if(op == 1):
            print(conta.extrato())
        if(op == 2):
            quant = float(input("\nValor a sacar: "))
            conta.saca(quant)
        if(op == 3):
            quant = float(input("\nValor a depositar: "))
            conta.deposita(quant)
        if(op == 4):
            d.formatada()
        if(op == 5):
            conta2.transfere(50, conta)
        if(op == 6):
            codigos = conta.codigo_banco()
            print(codigos['BB'])


if(__name__ == "__main__"):
    __main__()
