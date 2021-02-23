import pygame
from pygame.sprite import Sprite
import settings as ai_settings

class Bullet(Sprite):
    #uma classe q administra os projeteis disparados pela nave
    def __init__(self, ai_settings, screen, ship):
        #cria um projetio na posição atual da nava
        super(Bullet, self).__init__()
        self.screen = screen
        #cria um retangulo para o projetio em (0,0) e em seguida
        #define sua posição correta
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet.height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #armazena a posição do projetil como um valor decimal 
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


