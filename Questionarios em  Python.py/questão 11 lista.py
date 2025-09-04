'''
Usando list comprehension, crie um tabuleiro de xadrez vazio e depois adicione todas as peças do jogo na posição inicial. Para melhorar a visualização do tabuleiro, identifique as posições do tabuleiro da seguinte forma:



[ ] - para posições vazias
tor - para a torre
cav - para o cavalo
bis - para o bispo
rai - para a rainha
rei - para o rei
pea - para o peão


Por fim imprima o tabuleiro na tela, deixando cada linha da matriz abaixo da outra. (Dica você pode usar a biblioteca numpy para auxiliar na impressão da matriz)
'''



import numpy as np                                                        #biblioteca que questão pediu
tabuleiro = [["[ ]" for i in range(8)] for j in range(8)]
tabuleiro[0] = ["tor","cav","bis","rai","rei","bis","cav","tor"]
tabuleiro[1] = ["pea"]*8
tabuleiro[6] = ["pea"]*8
tabuleiro[7] = ["tor","cav","bis","rai","rei","bis","cav","tor"]
print(np.array(tabuleiro))

