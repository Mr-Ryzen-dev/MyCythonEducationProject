# Импорты
import cpp_wrapper
import pygame

pygame.init()

playerMovementSpeed = 3
programIsRunning = True

WIDTH, HEIGHT = cpp_wrapper.py_getWindowProperties()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame 0.0.1")
clock = pygame.time.Clock()

background = pygame.image.load("TestMap.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


player_img = pygame.image.load("DefaultPlayer.png").convert_alpha()
player_img = pygame.transform.smoothscale(player_img, (80, 80))
player_rect = pygame.Rect(100, 500, 80, 80)

#---------------------------------------------------------------------------------------------------
#Основной цикл

while programIsRunning:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            programIsRunning = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        player_rect.y += (playerMovementSpeed * -1)
    if keys[pygame.K_s]:
        player_rect.y += playerMovementSpeed 
    if keys[pygame.K_a]:
        player_rect.x += (playerMovementSpeed * -1)
    if keys[pygame.K_d]:
        player_rect.x += playerMovementSpeed


    screen.blit(player_img, player_rect.topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()