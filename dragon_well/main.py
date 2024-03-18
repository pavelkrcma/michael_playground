import pygame
import random
from game_plan import GamePlan

SCREEN_WIDTH = 1180
SCREEN_HEIGHT = 860
background_color = (255, 255, 255)

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

sword_img = pygame.image.load("graphics/sword.png")
artefact_1_img = pygame.image.load("graphics/artefact-1.png")
artefact_2_img = pygame.image.load("graphics/artefact-2.png")
artefact_3_img = pygame.image.load("graphics/artefact-3.png")
character_img = pygame.image.load("graphics/character-1.png")

def DrawWell(x,y):
     pass

def DrawScreen():
    SCREEN_WIDTH = window.get_width()
    SCREEN_HEIGHT = window.get_height()

    window.fill(background_color) # Set the background color
    pygame.draw.line(window, 0, (0, SCREEN_HEIGHT - SCREEN_HEIGHT // 6), (SCREEN_WIDTH, SCREEN_HEIGHT - SCREEN_HEIGHT // 6), 5)
    pygame.draw.line(window, 0, (0, SCREEN_HEIGHT // 7), (SCREEN_WIDTH, SCREEN_HEIGHT // 7), 5)

    artefact_y_possition = SCREEN_HEIGHT - SCREEN_HEIGHT // 12 - artefact_1_img.get_height() // 2
    window.blit(sword_img, (sword_img.get_width() // 2, artefact_y_possition))
    window.blit(artefact_1_img, (100, artefact_y_possition))
    window.blit(artefact_2_img, (200, artefact_y_possition))
    window.blit(artefact_3_img, (300, artefact_y_possition))

    DrawWell(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False

    DrawScreen()
    pygame.display.update()

pygame.quit()
