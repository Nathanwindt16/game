import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super(Character, self).__init__()
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


