import pygame
import spritesheet

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
FPS = 60

sprite_sheet_image = pygame.image.load('doux.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

BLACK = (0, 0, 0)

BG = (50, 50, 50)    

player_x = 0
player_y = 0
player_speed = 4

current_frame = 0
last_update = pygame.time.get_ticks()
ANIMATION_COOLDOWN = 100
is_moving = False

run = True

flip = False
while run:

    screen.fill(BG)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    is_moving = False
    
    if keys[pygame.K_a]:
        player_x -= player_speed
        is_moving = True
        flip = True
    if keys[pygame.K_d]:
        player_x += player_speed
        is_moving = True
        flip = False
    if keys[pygame.K_w]:
        player_y -= player_speed
        is_moving = True
    if keys[pygame.K_s]:
        player_y += player_speed
        is_moving = True

    current_time = pygame.time.get_ticks()
    if is_moving:
        if current_time - last_update >= ANIMATION_COOLDOWN:
            current_frame += 1
            last_update = current_time
            if current_frame >= 6:
                current_frame = 0
    else:
        current_frame = 0
    
    screen.blit(sprite_sheet.get_image(current_frame+2, 24, 24, 3, BLACK, flip), (player_x, player_y))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
