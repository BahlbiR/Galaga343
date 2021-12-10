import os
import pygame as pg


# Complete me! - TODO
class Enemy(pg.sprite.Sprite):
    move = False
    def __init__(self, position):
        super(Enemy, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'Ship2.png')).convert_alpha()
        self.image = pg.transform.flip(self.image, True, False)     # Flip the image of the ships to face the player
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(topleft = (position[0], position[1]))       
        Enemy.move = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        # once the ships hit the top of the screen, move them down
        if self.rect.top < 0:
            Enemy.move = False
        # once the ships hit the bottom of the screen, move them up
        if self.rect.bottom > 768:
            Enemy.move = True
        if Enemy.move:
            self.speedy = 300 * delta
            self.rect.y -= self.speedy
        else:
            self.speedy = 300 * delta 
            self.rect.y += self.speedy
            
    
   