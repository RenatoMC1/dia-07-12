class ContaCorrente:
    def __init__(self, agencia, conta, saldo, favorecido):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.favorecido = favorecido

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"R$ {valor} é um valor inválido!")
        else:
            print(f"Você sacou R$ {valor}.")
            self.saldo = self.saldo - valor

conta01 = ContaCorrente(1, 2, 100, "Infinity")
print(f"Saldo atual é de R$ {conta01.saldo}")
conta01.sacar(10)
print(f"Saldo atual é de R$ {conta01.saldo}")
conta01.sacar(10)
print(f"Saldo atual é de R$ {conta01.saldo}")
conta01.sacar(90)
print(f"Saldo atual é de R$ {conta01.saldo}")
conta01.sacar(10)
print(f"Saldo atual é de R$ {conta01.saldo}")
conta01.sacar(1)
print(f"Saldo atual é de R$ {conta01.saldo}")