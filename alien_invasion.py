#importaçoes necessarias
import sys
import pygame
#importaçoes de classes/modulos
from settings import Settings
from ship import Ship
#importando funçoes
import game_function as gf

def run_game():
    #inicializa o jogo e cria um objeto para a tela.
    #inicializa as configuracoes de objeto.
    ai_settings = Settings()
    screen = pygame.display.set_mode(ai_settings.screen_width, ai_settings.screen_height)
    pygame.display.set_caption("Alien Invasion")
    #cria uma espaço nave:
    ship = Ship( ai_settings, screen)
    #inicializa o laço principal do jogo
    while True :
        gf.check_events(ship)
        ship.update()
        gf.uptade_screen(ai_settings, screen, ship)        

    #inicializa o metodo para jogar 
    run_game()