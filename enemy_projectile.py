import os
import pygame as pg

class Enemy_Projectile(pg.sprite.Sprite):
    def __init__(self, shipLocation, player):
        super(Enemy_Projectile, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'shot.png')).convert_alpha()
        self.image = pg.transform.flip(self.image, True, False)     # Flip the image of the bullet
        self.rect = self.image.get_rect()
        self.rect.centerx = shipLocation.rect.centerx - 20
        self.rect.centery = shipLocation.rect.centery 
        self.player = player
        self.fireSound = pg.mixer.Sound("./assets/fire.wav")
        self.fireSound.play()
        self.explosionSound = pg.mixer.Sound("./assets/explosion.wav")

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        # If the enemy projectile misses the player, remove it from the screen
        self.rect.x -= 1000 * delta
        if self.rect.x < 0:
            self.kill()
        # If an enemy projectile hits the player, subtract 1 from their health
        collision = pg.sprite.collide_mask(self, self.player)
        if collision:
            self.player.health -= 1
            self.explosionSound.play()
            self.kill()

