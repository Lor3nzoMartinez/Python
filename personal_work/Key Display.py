import pygame
import time

# Window Start

pygame.init()

display_width = 400

display_height = 200

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Key Press Capture")

clock = pygame.time.Clock()

black = (0, 0, 0)

white = (255, 255, 255)

# Definitions of core functions


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 75)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_height/3), (display_width/3))
    gameDisplay.blit(text_surf, text_rect)

    pygame.display.update()

    time.sleep(0.5)

    return True

    key_capping()

# While loop handling the closing of the window


def key_capping():
    game_exit = False

    while not game_exit:

        # Loop that gets current event and decides
        # how it is handled.

        for event in pygame.event.get():

            # Closes window when satisfied

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        while event.type == pygame.KEYDOWN:
            message_display(event.unicode)
            if message_display(event.unicode) == True:
                message_display('+' + event.unicode)

        gameDisplay.fill(white)

        pygame.display.update()

key_capping()



