import pygame

# Python Games Display Setup

pygame.init()

display_width = 800

display_height = 600

background = pygame.image.load('JnZJUXH.png')

white_background = (255, 255, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Drive on my dude.")

clock = pygame.time.Clock()

# Character Image Settings

char_width = 80

char_height = 80

charImage = pygame.image.load('char.jpg')


def char(x, y):
    gameDisplay.blit(charImage, (x, y))


# Game loop function handles all the logic and events

def game_loop():

    x = (display_height * 0.55)

    y = (display_width * 0.65)

    x_change = 0

    y_change = 0

    game_exit = False

    while not game_exit:

        # Loop that gets current event and decides
        # how it is handled.

        for event in pygame.event.get():

            # Closes window when satisfied

            if event.type == pygame.QUIT:
                game_exit = True

            # Logic for handling key presses/ events

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -1
                elif event.key == pygame.K_RIGHT:
                    x_change = 1
                elif event.key == pygame.K_UP:
                    y_change = -1
                elif event.key == pygame.K_DOWN:
                    y_change = 1

            # Handles when keys are released

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        # Updates x

        x += x_change

        # Updates y

        y += y_change

        # Creates background

        gameDisplay.fill(white_background)

        # Passes Updated x and y to character

        char(x, y)

        # Passes characters new position to screen

        pygame.display.update()

        # Sets clock

        clock.tick(60)


# Calls our function game_loop()

game_loop()

# Calls built-in function to quit display after
# game_loop is satisfied

pygame.quit()

# Quits process after display is removed

quit()
