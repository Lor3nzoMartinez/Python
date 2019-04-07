import pygame

pygame.init()

display_width = 800

display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("-Window Text Here-")

clock = pygame.time.Clock()

game_exit = False

while not game_exit:

    # Loop that gets current event and decides
    # how it is handled.

    for event in pygame.event.get():

        # Closes window when satisfied

        if event.type == pygame.QUIT:
            game_exit = True

# Calls built-in function to quit display after
# game_loop is satisfied

pygame.quit()

# Quits process after display is removed

quit()
