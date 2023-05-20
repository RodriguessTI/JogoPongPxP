# Importe a biblioteca pygame
import pygame
# Importar a classe Paddle(barra)
from paddle import Paddle
# Importar a classe ball(bola)
from ball import Ball
# Inicializar o motor de jogo
pygame.init()

# Definir algumas cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Abre uma nova janela
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# Crie a Barra JOGADOR-1
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

# Crie a Barra JOGADOR-2
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

#Crie o sprite da bola
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# Esta será uma lista que conterá todos os sprites que pretendemos utilizar em nosso jogo.
all_sprites_list = pygame.sprite.Group()

# Adicione as 2 BARRAS e a BOLA à lista de objetos
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

# O loop continuará até que o usuário saia do jogo (por exemplo, clique no botão Fechar).
carryOn = True

# O relógio será usado para controlar a rapidez com que a tela é atualizada
clock = pygame.time.Clock()

# Inicializar as pontuações dos jogadores
scoreA = 0
scoreB = 0

# -------- Loop do programa principal -----------
while carryOn:
    # --- Loop de evento principal ---
    for event in pygame.event.get():  # O usuário fez algo
        if event.type == pygame.QUIT:  # Se o usuário clicou em fechar
            carryOn = False  # Sinalize que terminamos, então saímos deste loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressionar a tecla x encerrará o jogo
                carryOn = False

    # Mover as BARRAS quando usa as teclas de seta (jogador A) ou as teclas "W/S" (jogador B)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

        # --- A lógica do jogo deve ir aqui
    all_sprites_list.update()

    # Verifique se a bola está quicando em alguma das 4 paredes:
    if ball.rect.x >= 690:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

        # Detectar colisões entre a bola e as barra
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    # --- O código do desenho deve ir aqui
    # Primeiro, limpe a tela para preto.
    screen.fill(BLACK)
    # Desenhe a rede
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    # Agora vamos desenhar todos os sprites de uma só vez.
    all_sprites_list.draw(screen)

    # Exibir pontuações:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420, 10))

    # --- Vá em frente e atualize a tela com o que desenhamos.
    pygame.display.flip()

    # --- Limite a 60 quadros por segundo
    clock.tick(60)

# Depois de sair do loop principal do programa, podemos parar o mecanismo do jogo:
pygame.quit()
