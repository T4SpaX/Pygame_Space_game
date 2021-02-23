import pygame
from settings import Settings

class Ship():
    #uma classe para espacionave do jogador
    def __ini__(self, screen):
        #inicializa a espacionave e define a posição 
        self.screen = screen

        #carrega a imagem da espacionave e obtem seu rect
        self.image = pygame.image.load("./images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #inicializa cada nova espacionave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #armazena um valor decimal para o centro da tela
        self.center = float(self.rect.centerx)

        #flag de movimento
        self.moving_right = False
        self.moving_left = False

        self.ai_settings = Settings()
    
    def update(self):
        #atuliza posição da espacionave de acordo com a flag
        #atualiza o valor no centro da nave e nao no retangulo
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left < self.screen_rect.left:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
        #atualiza o objeto rect de acordo com self center
        self.rect.centex = self.center

    
    def blitme(self):
        #desenha a espacionave na sua posiçao atual 
        self.screen.blit(self.image, self.rect)