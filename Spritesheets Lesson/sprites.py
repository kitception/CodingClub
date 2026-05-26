import pygame

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

spritesheet = pygame.image.load('doux.png').convert_alpha()

BG = (50, 50, 50)
BLACK = (0, 0, 0)

def get_image(sheet, frame, width, height, scale, colour):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(colour)

    return image

frame_0 = get_image(spritesheet, 0, 24, 24, 2, BLACK)

run = True
while run:
    screen.fill(BG)

    #screen.blit(spritesheet, (0, 0))

    screen.blit(frame_0, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()