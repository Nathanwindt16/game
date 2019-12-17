import pygame
from Globals import *
from Character import *


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite = Character()
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()

    done = False

    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            print("MOVE RIGHT ......", my_sprite.x)
            my_sprite.move_right()
        if keys[pygame.K_LEFT]:
            print("MOVE RIGHT ......", my_sprite.x)
            my_sprite.move_left()
        if keys[pygame.K_UP]:
            print("MOVE UP ......", my_sprite.x)
            my_sprite.move_up()
        if keys[pygame.K_DOWN]:
            print("MOVE DOWN ......", my_sprite.x)
            my_sprite.move_down()
        # When the keys are released ... my_sprite.stop()

        my_group.update()

        screen.fill(BACKGROUND_COLOR)
        my_group.draw(screen)

        pygame.display.update()
        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()

if __name__ == '__main__':
    main()
