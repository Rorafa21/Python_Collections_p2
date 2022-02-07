from collections import defaultdict
from unittest import defaultTestLoader

meu_texto = "Bem vindo meu nome é rodrigo eu gosto muito de nome e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()
aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    aparicoes[palavra] += 1

print(aparicoes)