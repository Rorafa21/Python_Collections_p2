from collections import defaultdict
from unittest import defaultTestLoader

meu_texto = "Bem vindo meu nome é rodrigo eu gosto muito de nome e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()
meu_texto.split()
aparicoes = defaultdict()

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)