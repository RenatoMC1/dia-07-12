class ContaCorrente:
    def __init__(self):
        self.agencia = 1218
        self.conta = 625659
        self.saldo = 1500

conta01 = ContaCorrente()

print("-="*50)
print("Cliente 01")
print(f"Sua agência: ", conta01.agencia)
print(f"Sua conta corrente: ", conta01.conta)
print(f"Seu saldo atual é: ", conta01.saldo)
print("-="*50)

resp = int(input("Deseja realizar um depósito? \n[1] Sim\n[2] Não\n"))

if resp == 1:
    ag = input("Digite agência: ")
    cc = input("Digite conta: ")
    sd = float(input("Digite saldo a depositar: "))
    fav = input("Digite favorecido: ")

    resp2 = int(input("Dados do favorecido estão corretos? \n[1] Sim\n[2] Não\n"))
    if resp2 == 2:
        ag = input("Digite agência: ")
        cc = input("Digite conta: ")
        sd = float(input("Digite saldo a depositar: "))
        fav = input("Digite favorecido: ")
    else:
        sd = float(input("Confirme saldo a depositar: "))
        if sd > 0:
            print("-=" * 50)
            print("Você recebeu um depósito e seu novo saldo é: R$", (conta01.saldo + sd))
        else:
            print("Digite um valor maior que zero!")



