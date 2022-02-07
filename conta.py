from collections import defaultdict

class Conta:
    def __init__(self):
        print("Imprimindo uma conta")


contas = defaultdict(Conta)
conta2 = defaultdict(Conta)
print(conta2[12])
print(contas[15])