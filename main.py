#!/usr/bin/env python3

import pygame as pg
import pygame.freetype
import os
from enemy import Enemy
from player import Player
from projectile import Projectile
from enemy_projectile import Enemy_Projectile
from pygame.locals import *
import time
import random


def main():
    # Startup pygame
    pg.init()

    # Get a screen object
    screen = pg.display.set_mode([1024, 768])

    # Background
    background = pg.image.load("./assets/background.png").convert_alpha()
    background = pg.transform.scale(background, (1024, 768))
    
    # Create a player
    player = Player()

    # Create enemy and projectile Groups
    enemies = pg.sprite.Group()
    projectiles = pg.sprite.Group()
    enemy_projectiles = pg.sprite.Group()

    # Add hoard of enemy spaceships
    for i in range(500, 1000, 75):
        for j in range(100, 600, 50):
            enemy = Enemy((i, j))
            enemies.add(enemy)

    # Start sound - Load background music and start it
    # playing on a loop 
    pg.mixer.music.load('./assets/cpu-talk.mp3')
    pg.mixer.music.play(-1, 0.0)

    # Get font setup
    pg.freetype.init()
    font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./assets", "PermanentMarker-Regular.ttf")
    font_size = 64
    font = pg.freetype.Font(font_path, font_size)
    # Tuple for FONTCOLOR 
    FONTCOLOR = (255, 255, 0)
    # Startup the main game loop
    running = True
    # Keep track of time
    delta = 0
    # Make sure we can't fire more than once every 250ms
    shotDelta = 250
    enemyShotDelta = 250
    # Frame limiting
    fps = 60
    clock = pg.time.Clock()
    clock.tick(fps)
    # Setup score variable
    score = 0
    while running:
        
        # First thing we need to clear the events.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.USEREVENT + 1:
                score += 100

        keys = pg.key.get_pressed()

        if keys[K_s] or keys[K_DOWN]:
            player.down(delta)
        if keys[K_w] or keys[K_UP]:
            player.up(delta)
        if keys[K_SPACE]:
            if shotDelta >= .25:
                projectile = Projectile(player.rect, enemies)
                projectiles.add(projectile) 
                shotDelta = 0
        #Every second, randomly select an enemy ship to fire at the enemy
        if enemyShotDelta >= 1:   
                randShip = random.choice(enemies.sprites())
                if randShip:
                    enemy_projectile = Enemy_Projectile(randShip, player)
                enemy_projectiles.add(enemy_projectile)
                enemyShotDelta = 0
        

        # Ok, events are handled, let's update objects!
        player.update(delta)
        for enemy in enemies:
            enemy.update(delta)
        for projectile in projectiles:
            projectile.update(delta)
        for enemy_projectile in enemy_projectiles:
            enemy_projectile.update(delta)

        # Objects are updated, now let's draw!
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))     # Add the background image
        player.draw(screen)
        enemies.draw(screen)
        projectiles.draw(screen)
        enemy_projectiles.draw(screen)
        font.render_to(screen, (10, 10), "Score: " + str(score), FONTCOLOR, None, size=64)
        font.render_to(screen, (700, 10), "Health: " + str(player.health), FONTCOLOR, None, size=64)

        # When drawing is done, flip the buffer.
        pg.display.flip()

        # Time between previous frame and current frame
        delta = clock.tick(fps) / 1000.0
        shotDelta += delta
        enemyShotDelta += delta
        
        # if the player kills all enemies, play a victory sound
        if score == 7000:
            pg.mixer.music.stop()
            victory_sound = pg.mixer.Sound("./assets/Victory!.wav")
            pg.mixer.Sound.play(victory_sound)
            #pause for 5 seconds to allow the entire Victory sound to play
            time.sleep(5)
            running = False
            
        # if the player runs out of lives, play a lose sound
        if player.health == 0:
            pg.mixer.music.stop()
            victory_sound = pg.mixer.Sound("./assets/Lose.wav")
            pg.mixer.Sound.play(victory_sound)
            #pause for 5 seconds to allow the entire Victory sound to play
            time.sleep(3)
            running = False


# Startup the main method to get things going.
if __name__ == "__main__":
    main()
    pg.quit()
