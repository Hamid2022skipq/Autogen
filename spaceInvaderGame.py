import pygame
import sys
from pygame.locals import *  # noqa
import time

# Game Initialization
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
ENEMY_SIZE = 30
BULLET_SIZE = 15
ENEMY_SPACING = 10

# Set up some colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the player
player = pygame.Rect(WIDTH // 2, HEIGHT - PLAYER_SIZE -
                     10, PLAYER_SIZE, PLAYER_SIZE)

# Set up the enemies
enemies = [pygame.Rect(i*(ENEMY_SIZE+ENEMY_SPACING), j*(ENEMY_SIZE+ENEMY_SPACING), ENEMY_SIZE, ENEMY_SIZE)
           for i in range(WIDTH//(ENEMY_SIZE+ENEMY_SPACING)) for j in range(3)]

# Set up the bullets
bullets = []

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Game Loop
last_enemy_time = time.time()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:  # noqa
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:     # noqa
            if event.key == K_SPACE:     # noqa
                bullets.append(pygame.Rect(player.x + PLAYER_SIZE //
                               2, player.y, BULLET_SIZE, BULLET_SIZE))

    # Player Movement
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:  # noqa
        player.x -= 3
    if keys[K_RIGHT]:  # noqa
        player.x += 3

    # Bullet Movement
    for bullet in bullets:
        bullet.y -= 5
        if bullet.y < 0:
            bullets.remove(bullet)

    # Collision Detection
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

    # Add new enemies
    if time.time() - last_enemy_time > 5:
        enemies += [pygame.Rect(i*(ENEMY_SIZE+ENEMY_SPACING), 0, ENEMY_SIZE, ENEMY_SIZE)
                    for i in range(WIDTH//(ENEMY_SIZE+ENEMY_SPACING))]
        last_enemy_time = time.time()

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, player)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)

    # Update the display
    pygame.display.flip()
