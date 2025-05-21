# main.py
import cpp_wrapper

cpp_wrapper.py_relos()

import pygame

pygame.init()

WIDTH,HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Супер игра")
clock = pygame.time.Clock()

background = pygame.image.load("карта.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

player_img = pygame.image.load("ВАЖНО.png").convert_alpha()
player_img = pygame.transform.smoothscale(player_img, (80, 80))
player_rect = pygame.Rect(100, 500, 80, 80)
player_vel_y = 0


while True:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_rect.x -= SPEED
    if keys[pygame.K_s]:
        player_rect.x += SPEED
    if keys[pygame.K_a]:
        player_rect.y -= SPEED
    if keys[pygame.K_d]:
        player_rect.x += SPEED


    pygame.display.flip()

pygame.quit()
