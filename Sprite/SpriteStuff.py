import pygame
SIZE = WIDTH, HEIGHT = 1925, 1000  # the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white')  # The background colod of our window
FPS = 100  # Frames per second

#comment

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        self.x = 25
        self.y = 25
        width = 116
        height = 176
        self.speed_x = 0
        self.speed_y = 0

        self.speed_x = 0
        self.speed_y = 0
        self.images = []
        self.images.append(pygame.transform.scale(pygame.image.load('./Images/Idle__000.png'),(width, height)))
        self.images.append(pygame.transform.scale(pygame.image.load('./Images/Idle__001.png'),(width, height)))
        self.images.append(pygame.transform.scale(pygame.image.load('./Images/Idle__002.png'),(width, height)))
        self.images.append(pygame.transform.scale(pygame.image.load('./Images/Idle__003.png'),(width, height)))
        self.images.append(pygame.transform.scale(pygame.image.load('./Images/Idle__004.png'),(width, height)))
        self.images.append(pygame.transform.scale(pygame.image.load('./Images/Idle__005.png'),(width, height)))
        self.images.append(pygame.transform.scale(pygame.image.load('./Images/Idle__006.png'),(width, height)))
        self.images.append(pygame.transform.scale(pygame.image.load('./Images/Idle__007.png'),(width, height)))
        self.images.append(pygame.transform.scale(pygame.image.load('./Images/Idle__008.png'),(width, height)))
        self.images.append(pygame.transform.scale(pygame.image.load('./Images/Idle__009.png'),(width, height)))

        self.index = 0

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

    def update(self):
        print("MY SPRITE UPDATE BEING CALLED")
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

    def move_right(self):
        self.speed_x = 5

    def move_left(self):
        self.speed_x = -5

    def move_up(self):
        self.speed_y = -5

    def move_down(self):
        self.speed_y = 5

    def stop(self):
        self.speed_x = 0


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite = MySprite()
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
