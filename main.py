# Импорты
import cpp_wrapper
import pygame
import sys
import math

#---------------------------------------------------------------------------------------------------
#объявления
pygame.init()

playerMovementSpeed = 4
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

    class PlayerPawn:
        def __init__(self, x, y, image):
            self.original_image = image
            self.image = image
            self.rect = self.image.get_rect(center=(x, y))
            self.position = (x, y)
            self.x = x
            self.y = y  

        def rotate(self):
            # Получаем координаты курсора
            mouse_x, mouse_y = cpp_wrapper.py_getCursorPosition()
            
            # Вычисляем угол через C++ функцию
            angle = cpp_wrapper.py_getBasePlayerRotation(
                self.x, self.y, mouse_x, mouse_y
            )+180
            
            # Поворачиваем изображение
            self.image = pygame.transform.rotate(self.original_image, angle)
            self.rect = self.image.get_rect(center=self.position)

    player_pawn = PlayerPawn(100, 500, player_img)

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
    
    if keys[pygame.K_w]:  # Исправлены квадратные скобки
        player_pawn.y -= playerMovementSpeed
    if keys[pygame.K_s]:  # Исправлены квадратные скобки
        player_pawn.y += playerMovementSpeed
    if keys[pygame.K_a]:  # Исправлены квадратные скобки
        player_pawn.x -= playerMovementSpeed
    if keys[pygame.K_d]:  # Исправлены квадратные скобки
        player_pawn.x += playerMovementSpeed
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    # Обновляем позицию после изменения координат
    player_pawn.position = (player_pawn.x, player_pawn.y)
    player_pawn.rect.center = player_pawn.position
    player_pawn.rect.clamp_ip(screen.get_rect())


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
            player_pawn.rotate()  # Добавляем поворот

            screen.blit(background, (0, 0))
            screen.blit(player_pawn.image, player_pawn.rect.topleft)  # Исправленный вызов
            
            pygame.display.flip()
            clock.tick(FPS)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

#---------------------------------------------------------------------------------------------------
#Запуск основного цикла
main()

pygame.quit()