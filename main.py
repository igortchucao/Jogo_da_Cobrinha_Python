import pygame, sys

pygame.init()

'''Tamanho da janela'''
size = width, height = 1000, 500

'''Cria a tela do pygame'''
screen = pygame.display.set_mode(size)

'''Cores'''
BLACK = 0, 0, 0
WHITE = 255, 255, 255

'''Criação da Classe da Cobrinha'''
class cobrinha(pygame.sprite.Sprite):
    '''Metodo Construtor'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.directionX = 1
        self.directionY = 0
        self.rect = pygame.Rect(0,0,40,40)
        self.imagem = pygame.draw.circle(screen, WHITE, [80, 80], 80, 1)

    def update(self, pos):
        self.directionX = pos[0]
        self.directionY = pos[1]
        self.rect.move_ip(self.directionX*3, self.directionY*3)


class maca(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.posX = 40
        self.posY = 40

    #def update(self, pos):
cobrinha = cobrinha()               
pygame.display.set_caption('Cobrinha!')
clock = pygame.time.Clock()

def main():
    while 1:
        clock.tick(120)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.draw.circle(screen, WHITE, [80, 80], 80, 1)
        cobrinha.update([1, 0])
        screen.fill(BLACK)
        #screen.blit(cobrinha.rect)
        pygame.display.flip()

if __name__ == "__main__":
    main()