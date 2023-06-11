import pygame
from pygame.locals import *

# Inicialização do Pygame
pygame.init()

# Configurações da janela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Meu Jogo')

# Variáveis de cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Loop principal do jogo
rodando = True
while rodando:
    # Lidando com eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False

    # Lógica do jogo

    # Atualização da tela
    tela.fill(BRANCO)
    # Desenhe outros objetos, personagens, etc. aqui

    pygame.display.flip()

# Encerramento do Pygame
pygame.quit()










