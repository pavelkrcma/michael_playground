import pygame
import random
from game_plan import GamePlan
from game_plan import GamePlanBlock

SCREEN_WIDTH = 1180
SCREEN_HEIGHT = 860
GAME_BLOCK_SIZE = 80
background_color = (255, 255, 255)
green = (0, 255, 0)
black = (0, 0, 0)
gray = (220,220,220)
BLOCK_LINE_WIDTH = 5

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

sword_img = pygame.image.load("graphics/sword.png")
artefact_1_img = pygame.image.load("graphics/artefact-1.png")
artefact_2_img = pygame.image.load("graphics/artefact-2.png")
artefact_3_img = pygame.image.load("graphics/artefact-3.png")
character_img = pygame.image.load("graphics/character-1.png")

random_block = GamePlanBlock()

game_plan = GamePlan()
# Fill test data
#game_plan.add_block(1, 0, {'top': 'opaque', 'bottom': 'transparent', 'left': 'transparent', 'right': 'opaque'})
#game_plan.add_block(1, 1, {'top': 'transparent', 'bottom': 'opaque', 'left': 'transparent', 'right': 'opaque'})

# 1: generate new random block; 2: wait for a mouse click
generate_new_block_state = 1

def CreateNewRandomBlock():
    global random_block

    while True:
        top = random.choice(('transparent', 'opaque', 'transparent', 'opaque', 'transparent'))
        bottom = random.choice(('transparent', 'opaque', 'transparent'))
        left = random.choice(('transparent', 'opaque', 'transparent', 'opaque', 'transparent'))
        right = random.choice(('transparent', 'opaque'))
        list_of_edges = [top, bottom, left, right]
        filtered = [edge for edge in list_of_edges if edge=='transparent']
        if len(filtered) > 1:
            break

    random_block = GamePlanBlock(0, 0, edges={'top': top, 'bottom': bottom, 'left': left, 'right': right})

def GetEdgeColor(edge):
    return green if edge == 'transparent' else black

def DrawGamePlan(x,y):
    for block in game_plan.get_all_blocks().values():
        draw_block(x, y, block)

def draw_block(x, y, block):
    pygame.draw.line(
        window,
        GetEdgeColor(block.edges['top']), # y + BLOCK_LINE_WIDTH // 2
        (x - GAME_BLOCK_SIZE // 2 + block.x * GAME_BLOCK_SIZE, y - GAME_BLOCK_SIZE // 2 + block.y * GAME_BLOCK_SIZE),
        (x - GAME_BLOCK_SIZE // 2 + (block.x+1) * GAME_BLOCK_SIZE, y - GAME_BLOCK_SIZE // 2 + block.y * GAME_BLOCK_SIZE),
        BLOCK_LINE_WIDTH)

    pygame.draw.line(
        window,
        GetEdgeColor(block.edges['bottom']), # y - BLOCK_LINE_WIDTH // 2
        (x - GAME_BLOCK_SIZE // 2 + block.x * GAME_BLOCK_SIZE, y - GAME_BLOCK_SIZE // 2 + (block.y+1) * GAME_BLOCK_SIZE),
        (x - GAME_BLOCK_SIZE // 2 + (block.x+1) * GAME_BLOCK_SIZE, y - GAME_BLOCK_SIZE // 2 + (block.y+1) * GAME_BLOCK_SIZE),
        BLOCK_LINE_WIDTH)

    pygame.draw.line(
        window,
        GetEdgeColor(block.edges['left']), # x + BLOCK_LINE_WIDTH // 2
        (x - GAME_BLOCK_SIZE // 2 + block.x * GAME_BLOCK_SIZE, y - GAME_BLOCK_SIZE // 2 + (block.y) * GAME_BLOCK_SIZE + BLOCK_LINE_WIDTH),
        (x - GAME_BLOCK_SIZE // 2 + block.x * GAME_BLOCK_SIZE, y - GAME_BLOCK_SIZE // 2 + (block.y+1) * GAME_BLOCK_SIZE - BLOCK_LINE_WIDTH),
        BLOCK_LINE_WIDTH)

    pygame.draw.line(
        window,
        GetEdgeColor(block.edges['right']), # x - BLOCK_LINE_WIDTH // 2
        (x - GAME_BLOCK_SIZE // 2 + (block.x+1) * GAME_BLOCK_SIZE, y - GAME_BLOCK_SIZE // 2 + block.y * GAME_BLOCK_SIZE + BLOCK_LINE_WIDTH),
        (x - GAME_BLOCK_SIZE // 2 + (block.x+1) * GAME_BLOCK_SIZE, y - GAME_BLOCK_SIZE // 2 + (block.y+1) * GAME_BLOCK_SIZE - BLOCK_LINE_WIDTH),
        BLOCK_LINE_WIDTH)

def DrawWell(x,y):
    font = pygame.font.Font("seguisym.ttf", 48) # 48 is font size
    text_surf = font.render(f"\u2764\ufe0f", True, (0,0,0), (255,255,255))
    text_rect = text_surf.get_rect(center=(x, y))
    window.blit(text_surf, text_rect)  # Draw the text on the screen
    pygame.draw.rect(window, (0, 0, 0), pygame.Rect(x - GAME_BLOCK_SIZE // 2, y - GAME_BLOCK_SIZE // 2, GAME_BLOCK_SIZE, GAME_BLOCK_SIZE), BLOCK_LINE_WIDTH)

def DrawScreen():
    global SCREEN_WIDTH, SCREEN_HEIGHT
    global generate_new_block_state

    SCREEN_WIDTH = window.get_width()
    SCREEN_HEIGHT = window.get_height()

    window.fill(background_color) # Set the background color
    pygame.draw.line(window, 0, (0, SCREEN_HEIGHT - SCREEN_HEIGHT // 6), (SCREEN_WIDTH, SCREEN_HEIGHT - SCREEN_HEIGHT // 6), 5)
    pygame.draw.line(window, 0, (0, SCREEN_HEIGHT // 7), (SCREEN_WIDTH, SCREEN_HEIGHT // 7), 5)

    # Draw grid
    current_x = GAME_BLOCK_SIZE
    while current_x < SCREEN_WIDTH:
        pygame.draw.line(window, gray, (current_x, SCREEN_HEIGHT // 7 + BLOCK_LINE_WIDTH // 2), (current_x, SCREEN_HEIGHT - SCREEN_HEIGHT // 6 - BLOCK_LINE_WIDTH // 2), 1)
        current_x += GAME_BLOCK_SIZE

    current_y = SCREEN_HEIGHT // 7 + GAME_BLOCK_SIZE
    while current_y < SCREEN_HEIGHT - SCREEN_HEIGHT // 6:
        pygame.draw.line(window, gray, (0, current_y), (SCREEN_WIDTH, current_y), 1)
        current_y += GAME_BLOCK_SIZE

    artefact_y_possition = SCREEN_HEIGHT - SCREEN_HEIGHT // 12 - artefact_1_img.get_height() // 2
    window.blit(sword_img, (sword_img.get_width() // 2, artefact_y_possition))
    window.blit(artefact_1_img, (100, artefact_y_possition))
    window.blit(artefact_2_img, (200, artefact_y_possition))
    window.blit(artefact_3_img, (300, artefact_y_possition))
 
    rounded_center_x = ((SCREEN_WIDTH // 2) // GAME_BLOCK_SIZE) * GAME_BLOCK_SIZE - GAME_BLOCK_SIZE // 2
    rounded_center_y = ((SCREEN_HEIGHT // 2 - SCREEN_HEIGHT // 7) // GAME_BLOCK_SIZE) * GAME_BLOCK_SIZE - GAME_BLOCK_SIZE // 2 + SCREEN_HEIGHT // 7

    DrawWell(rounded_center_x, rounded_center_y)
    DrawGamePlan(rounded_center_x, rounded_center_y)

    if generate_new_block_state == 2:
        draw_block(SCREEN_WIDTH - 100, SCREEN_HEIGHT - SCREEN_HEIGHT // 12, random_block)

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP and generate_new_block_state == 2:
            posx, posy = pygame.mouse.get_pos()
            if posy < SCREEN_HEIGHT // 7 or posy > SCREEN_HEIGHT - SCREEN_HEIGHT // 6 - GAME_BLOCK_SIZE // 2: # out of playground
                continue
            rel_x = (posx - SCREEN_WIDTH // 2 + GAME_BLOCK_SIZE // 2) // GAME_BLOCK_SIZE + 1
            rel_y = (posy - SCREEN_HEIGHT // 2 + SCREEN_HEIGHT // 7 + GAME_BLOCK_SIZE // 2 ) // GAME_BLOCK_SIZE
            if rel_x == 0 and rel_y == 0:
                continue
            if game_plan.get_block(rel_x, rel_y):
                continue
            random_block.x = rel_x
            random_block.y = rel_y
            # =============
            on_right = game_plan.get_block(rel_x+1, rel_y)
            if on_right:
                if on_right.edges['left'] == 'opaque':
                    random_block.edges['right'] = 'opaque'
            # =============
            game_plan.add_existing_block(random_block)
            generate_new_block_state = 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False

    if generate_new_block_state == 1:
        CreateNewRandomBlock()
        generate_new_block_state = 2

    DrawScreen()
    pygame.display.update()

pygame.quit()
