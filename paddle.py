import pygame

BLACK = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):
    # Esta classe representa uma BARRA. Deriva da classe "Sprite" no Pygame.

    def __init__(self, color, width, height):
        # Chame o construtor da classe pai (Sprite)
        super().__init__()

        # Passe na cor da Paddle, sua largura e altura.
        # Defina a cor de fundo e defina-a como transparente
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Desenhe a Barra (um retângulo!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Busca o objeto retângulo que tem as dimensões da imagem.
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        # Verifique se você não está indo muito longe (fora da tela)
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        # Verifique se você não está indo muito longe (fora da tela)
        if self.rect.y > 400:
            self.rect.y = 400
