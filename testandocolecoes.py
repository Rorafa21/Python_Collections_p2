from collections import Counter



texto1 = '''Passiva – Financiamento
Os ataques básicos da Renata Glasc marcam inimigos e causam dano adicional. O dano de seus aliados consome a marca, causando ainda mais dano.
Q – Negócio Fechado
Renata Glasc lança um projétil do seu braço robótico, enraizando o primeiro inimigo atingido. Ela pode reativar a habilidade para arremessar o inimigo em uma direção-alvo, causando dano aos inimigos atingidos e atordoando-os se o alvo arremessado for um Campeão.
W – Empréstimo
Renata Glasc concede a um Campeão aliado ou a si mesma Velocidade de Ataque e Velocidade de Movimento crescente em direção a inimigos. Se o aliado conseguir eliminar um Campeão inimigo, a duração do efeito é reiniciada. Se o aliado for eliminado enquanto Empréstimo ainda estiver ativa, a Vida dele fica cheia, mas ele começa a queimar até a morte ao longo de 3s. O aliado pode parar a queima ao eliminar um Campeão antes de morrer.
E – Programa de Fidelidade
Renata Glasc lança foguetes Quimtec que concedem Escudo aos aliados e causam dano e Lentidão aos inimigos pelos quais ela passar. Os foguetes também aplicam seus efeitos ao redor dela na conjuração e em uma explosão no alcance máximo.
R – Apropriação Agressiva
Renata Glasc lança uma nuvem de produtos químicos que faz com que os inimigos entrem em estado de Berserk, aumentando sua Velocidade de Ataque e forçando-os a atacar qualquer coisa ao redor com o ataque básico. Inimigos em estado de Berserk priorizam atacar seus próprios aliados, depois unidades neutras, depois a equipe da Renata Glasc e, por último, a própria Renata Glasc.'''

texto2 = '''PASSIVA
TÉCNICAS DE GUERRILHA
Se Teemo permanecer imóvel e não fizer nada por um curto período, fica Invisível por tempo indefinido. Caso esteja em um arbusto, Teemo pode manter sua Invisibilidade enquanto se move. Ao sair da Invisibilidade, Teemo ativa Elemento Surpresa, aumentando a própria Velocidade de Ataque por alguns segundos.
Q
DARDO OFUSCANTE
Obscurece a visão de um inimigo com um poderoso veneno, causando dano à unidade-alvo e cegando-a pela duração do efeito.
W
MOVER DEPRESSA
Teemo corre por aí, aumentando passivamente sua Velocidade de Movimento até que seja atingido por um Campeão ou torre inimiga. Ele pode sair em disparada para receber Velocidade de Movimento adicional que não é interrompida por ataques por um certo período.
E
TIRO TÓXICO
Cada um dos ataques de Teemo envenenará o alvo, causando dano no impacto e a cada segundo seguinte por 4 segundos.
R
ARMADILHA VENENOSA
Teemo arremessa uma armadilha venenosa explosiva usando um dos cogumelos que guardou na mochila. Se um inimigo pisar na armadilha, ela soltará uma nuvem venenosa que causa dano e reduz a velocidade de inimigos ao longo do tempo. Se Teemo arremessar um cogumelo em cima de outro, ele saltará, recebendo alcance adicional.'''

def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_carac = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_carac) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caracteres, proporcao in mais_comuns:
        print(f"{caracteres} => {proporcao * 100 :.2f}%")
analisa_frequencia_de_letras(texto1)