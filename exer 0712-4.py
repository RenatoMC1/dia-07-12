class ContaCorrente:
    def __init__(self, agencia, conta, saldo, favorecido):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.favorecido = favorecido

ag = input("Digite agência: ")
cc = input("Digite conta: ")
sd = float(input("Digite saldo: "))
fav = input("Digite favorecido: ")

cliente01 = ContaCorrente(ag, cc, sd, fav)

print("-="*50)
print("Cliente 01")
print(f"Agência do cliente: ", cliente01.agencia)
print(f"Conta do cliente: ", cliente01.conta)
print(f"Saldo do cliente: ", cliente01.saldo)
print(f"Nome do Favorecido: ", cliente01.favorecido)
print("-="*50)
