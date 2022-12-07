class ContaCorrente:
    def __init__(self, agencia, conta, saldo, favorecido):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.favorecido = favorecido

    def depositar(self, valor):
        if valor <= 0:
            print(f"R$ {valor} é um valor inválido!")
        else:
            print(f"Você depositou R$ {valor}.")
            self.saldo = self.saldo + valor

conta01 = ContaCorrente(1, 2, 0, "Infinity")
print(f"Saldo atual é de R$ {conta01.saldo}")
conta01.depositar(10)
print(f"Saldo atual é de R$ {conta01.saldo}")
conta01.depositar(10)
print(f"Saldo atual é de R$ {conta01.saldo}")
conta01.depositar(0)
print(f"Saldo atual é de R$ {conta01.saldo}")
conta01.depositar(10)
print(f"Saldo atual é de R$ {conta01.saldo}")
conta01.depositar(1)
print(f"Saldo atual é de R$ {conta01.saldo}")

