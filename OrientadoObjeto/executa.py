from conta import Conta


def __main__():
    conta = Conta(123, "Gustavo", 55.0, 1000.0)

    op = 1
    while(op != 0):
        op = int(input("Extrado = 1, Sacar = 2, Depositar = 3\n"))
        if(op == 1):
            Conta.extrato(conta)
        if(op == 2):
            quant = float(input("Valor a sacar"))
            Conta.saca(conta, quant)
        if(op == 3):
            quant = float(input("Valor a depositar"))
            Conta.deposita(conta, quant)


if(__name__ == "__main__"):
    __main__()
