# Импорты
import cpp_wrapper
import pygame
import sys
import math

#---------------------------------------------------------------------------------------------------
#объявления
pygame.init()

developer_mode = 1

playerMovementSpeed = 4
programIsRunning = True

if(developer_mode):
    WIDTH, HEIGHT = 1000, 1000
else:
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
    
    player_pawn = pygame.Rect(100, 500, 80, 80)

except pygame.error as e:
    print(f"Ошибка загрузки изображения: {e}")
    sys.exit(1)

#---------------------------------------------------------------------------------------------------
#Обработка событий
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

#---------------------------------------------------------------------------------------------------
#функция получения координат персонажа
def get_player_cords():
    global player_x, player_y
    player_x, player_y = player_pawn.center

#---------------------------------------------------------------------------------------------------
#функция проверки на движение
def update_player():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pawn.y -= playerMovementSpeed
    if keys[pygame.K_s]:
        player_pawn.y += playerMovementSpeed
    if keys[pygame.K_a]:
        player_pawn.x -= playerMovementSpeed
    if keys[pygame.K_d]:
        player_pawn.x += playerMovementSpeed

    player_pawn.clamp_ip(screen.get_rect())

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
            screen.blit(player_img, player_pawn.topleft)
            
            pygame.display.flip()
            clock.tick(FPS)

            get_player_cords()

            CursorX, CursorY = cpp_wrapper.py_getCursorPosition()
            angle = cpp_wrapper.py_getBasePlayerRotation(player_x, player_y, CursorX, CursorY)

            print({angle})

    except Exception as e:
        print(f"Произошла ошибка: {e}")

#---------------------------------------------------------------------------------------------------
#Запуск основного цикла
main()

pygame.quit()