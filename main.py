# Импорты
import cpp_wrapper
import pygame
import sys

#---------------------------------------------------------------------------------------------------
#объявления

pygame.init()

playerMovementSpeed = 3
programIsRunning = True

WIDTH, HEIGHT = cpp_wrapper.py_getScreenSize()
CursorX, CursorY = cpp_wrapper.py_getCursorPosition()
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame 0.0.1")
clock = pygame.time.Clock()

#---------------------------------------------------------------------------------------------------
#проверка на корректную загрузку
try:
    background = pygame.image.load("TestMap.png").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    
    player_img = pygame.image.load("DefaultPlayer.png").convert_alpha()
    player_img = pygame.transform.smoothscale(player_img, (80, 80))
    player_rect = pygame.Rect(100, 500, 80, 80)

except pygame.error as e:
    print(f"Ошибка загрузки изображения: {e}")
    sys.exit(1)

#---------------------------------------------------------------------------------------------------
#проверка на ивент
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

            
#---------------------------------------------------------------------------------------------------
#функция проверки на движение
def update_player():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_rect.y -= playerMovementSpeed
    if keys[pygame.K_s]:
        player_rect.y += playerMovementSpeed
    if keys[pygame.K_a]:
        player_rect.x -= playerMovementSpeed
    if keys[pygame.K_d]:
        player_rect.x += playerMovementSpeed

    player_rect.clamp_ip(screen.get_rect())

#---------------------------------------------------------------------------------------------------
#функция получения местоположения курсора на экране
def update_cursor_pos():
    global CursorX, CursorY
    CursorX, CursorY = cpp_wrapper.py_getCursorPosition()

#---------------------------------------------------------------------------------------------------
#Основной цикл
def main():
    try:
        while True:
            handle_events()
            update_player()
            update_cursor_pos()
            
            screen.blit(background, (0, 0))
            screen.blit(player_img, player_rect.topleft)
            
            pygame.display.flip()
            clock.tick(FPS)
            print({CursorX}, {CursorY})

    except Exception as e:
        print(f"Произошла ошибка: {e}")

#---------------------------------------------------------------------------------------------------
#Запуск основного цикла
main()

pygame.quit()