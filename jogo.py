import pygame
from pygame.locals import *

# Inicialização do Pygame
pygame.init()

# Configurações da janela
largura = 1000
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sinuca')
espessura = 5
VELOCIDADE = 0.1
velx = VELOCIDADE


x = 100
y = 300
RAIO = 20
# Variáveis de cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0,255,0)

def balls (x, y, RAIO, BRANCO):
    bola_name = pygame.draw.circle(tela, BRANCO, (x, y), RAIO )
    return bola_name

def movimento_bola(VELOCIDADE,x, y, RAIO, BRANCO,velx):
    x = x + velx  # codigo que faz o objeto andar para frente e tras

    if x + RAIO > 990:  # para não passar da borda da tela
        velx = -VELOCIDADE  # para não passar da borda da tela
    if x - RAIO < 0:  # para não passar da borda da tela
        velx = VELOCIDADE  # para não passar da borda da tela

    bola_name = pygame.draw.circle(tela, BRANCO, (x, y), RAIO)
    return bola_name



#Bolas da sinuca


# Loop principal do jogo
rodando = True

while rodando:
    # Lidando com eventos


    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False

    # Lógica do jogo

    # Atualização da tela
    tela.fill(VERDE)
    # Desenhe outros objetos, personagens, etc. aqui
    bola_branca = balls(x,y,RAIO,BRANCO)
    move = movimento_bola(VELOCIDADE,x, y, RAIO, BRANCO,velx)


    pygame.display.flip()


# Encerramento do Pygame
pygame.quit()










