import sys
import pygame

def check_keydown_event(event, ship):
    #responde a precionamento de tecla
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_event(event, ship):
    #responde a soltura de tecla
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    
def check_events(ship):
    #observa eventos do teclado e mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)

def uptade_screen(ai_settings, sreen, ship):
    #redesenha a tela a passagem pelo loop 
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    #deixa a tela mais recente visivel
    pygame.display.flip()
