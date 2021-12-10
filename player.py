import os
import pygame as pg


# Create a Player class that is a subclass of pygame.sprite.Sprite
# Load an image as such:
#        self.image = pg.image.load(os.path.join('assets', 'Ship6.png')).convert_alpha()
# The position is controlled by the rectangle surrounding the image.
# Set self.rect = self.image.get_rect().  Then make changes to the
# rectangle x, y or centerx and centery to move the object.

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'Ship6.png')).convert_alpha()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.health = 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        pass

    def up(self, delta):
        self.speedy = 300 * delta
        self.rect.y -= self.speedy

        # keep the ship within the window
        if self.rect.top < 0:
            self.rect.top = 0

    def down(self, delta):
        self.speedy = 300 * delta
        self.rect.y += self.speedy

        # keep the ship within the window
        if self.rect.bottom > 768:
            self.rect.bottom = 768