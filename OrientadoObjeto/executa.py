from conta import Conta
from datas import Data


def __main__():
    conta = Conta(123, "Gustavo", 55.0, 1000.0)
    d = Data(21, 11, 2007)

    op = 1
    while(op != 0):
        op = int(input("\nExtrado = 1, Sacar = 2, Depositar = 3, Ver Data = 4\n Opção: "))
        if(op == 1):
            Conta.extrato(conta)
        if(op == 2):
            quant = float(input("\nValor a sacar: "))
            Conta.saca(conta, quant)
        if(op == 3):
            quant = float(input("\nValor a depositar: "))
            Conta.deposita(conta, quant)
        if(op == 4):
            d.formatada()


if(__name__ == "__main__"):
    __main__()
