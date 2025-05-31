# Импорты
import cpp_wrapper
import pygame
import sys
import math
import random

#---------------------------------------------------------------------------------------------------
#объявления
pygame.init()


playerMovementSpeed = 4
programIsRunning = True

WIDTH, HEIGHT = cpp_wrapper.py_getScreenSize()

CursorX, CursorY = cpp_wrapper.py_getCursorPosition()
FPS = 60

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
    
    bot_img_raw = pygame.image.load("мент.png").convert_alpha()
    bot_img = pygame.transform.smoothscale(bot_img_raw, (60, 60)) 
    
    
    class PlayerPawn:
        def __init__(self, x, y, image):
            self.original_image = image
            self.image = image
            self.rect = self.image.get_rect(center=(x, y))
            self.position = (x, y)
            self.speed = playerMovementSpeed
            self.x = x
            self.y = y  
            self.angle = 0

            self.update_position()

        def update_position(self):
        # Синхронизируем все координаты
            self.rect.center = (self.x, self.y)
            self.position = (self.x, self.y)

        def getplayerpos(self):

            return self.x, self.y

        def getAngle(self):
            # Получаем координаты курсора
            mouse_x, mouse_y = cpp_wrapper.py_getCursorPosition()
            
            # Вычисляем угол через C++ функцию
            return cpp_wrapper.py_getBasePlayerRotation(
                self.x, self.y, mouse_x, mouse_y
            )+180

        def rotate(self):

            angle = player_pawn.getAngle()
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
#функция получения местоположения курсора на экране
def update_cursor_pos():
    """Обновляет позицию курсора с проверкой на ошибки"""
    global CursorX, CursorY
    try:
        CursorX, CursorY = cpp_wrapper.py_getCursorPosition()
        CursorX, CursorY = int(CursorX), int(CursorY)  # Гарантируем целые числа
    except (TypeError, ValueError) as e:
        print(f"Ошибка получения позиции курсора: {e}")
        CursorX, CursorY = 0, 0  # Значения по умолчанию

def move():
    """Обрабатывает движение игрока с улучшенной логикой"""
    keys = pygame.key.get_pressed()
    angle = player_pawn.getAngle()
    x, y = map(int, player_pawn.getplayerpos())  # Гарантируем целые координаты
    
    # Инициализация смещения
    dx, dy = 0, 0
    
    # Обработка управления с учетом одновременного нажатия клавиш
    if keys[pygame.K_w]:
        new_pos = cpp_wrapper.py_PawnMove(x, y, angle, playerMovementSpeed, 3)
        if new_pos: dx += new_pos[0] - x; dy += new_pos[1] - y
    if keys[pygame.K_s]:
        new_pos = cpp_wrapper.py_PawnMove(x, y, angle, playerMovementSpeed, 4)
        if new_pos: dx += new_pos[0] - x; dy += new_pos[1] - y
    if keys[pygame.K_a]:
        new_pos = cpp_wrapper.py_PawnMove(x, y, angle, playerMovementSpeed, 1)
        if new_pos: dx += new_pos[0] - x; dy += new_pos[1] - y
    if keys[pygame.K_d]:
        new_pos = cpp_wrapper.py_PawnMove(x, y, angle, playerMovementSpeed, 2)
        if new_pos: dx += new_pos[0] - x; dy += new_pos[1] - y
    
    # Нормализация диагонального движения
    if dx != 0 and dy != 0:
        dx *= 0.7071  # 1/sqrt(2)
        dy *= 0.7071
    
    # Обновление позиции
    newx, newy = x + int(dx), y + int(dy)
    
    if (newx, newy) != (x, y):
        player_pawn.x, player_pawn.y = newx, newy
        player_pawn.update_position()  # Должен обновлять rect и position
    
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

#---------------------------------------------------------------------------------------------------      
#Боты
class BotPawn:
    def __init__(self, x, y, image):
        self.original_bot_img = image
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.position = (x, y)
        self.x = x
        self.y = y
        self.angle = 0
        self.direction = [random.choice([-1, 0, 1]), random.choice([-1, 0, 1])]

    def move(self):
        if random.randint(0, 100) < 5:
            self.direction = [random.choice([-1, 0, 1]), random.choice([-1, 0, 1])]

        self.x += self.direction[0] * 2
        self.y += self.direction[1] * 2

        self.x = max(0, min(WIDTH, self.x))
        self.y = max(0, min(HEIGHT, self.y))

        self.position = (self.x, self.y)
        self.rect.center = self.position

    def rotate(self):
        dx, dy = self.direction
        angle = 0
        if dx != 0 or dy != 0:
            angle = math.degrees(math.atan2(-dy, dx))
        self.image = pygame.transform.rotate(self.original_bot_img, angle)
        self.rect = self.image.get_rect(center=self.position)

#---------------------------------------------------------------------------------------------------
# Инициализация объектов
bots = [
    BotPawn(300, 100, bot_img),
    BotPawn(500, 400, bot_img),
    BotPawn(700, 300, bot_img),
    BotPawn(200, 500, bot_img)
]

#---------------------------------------------------------------------------------------------------
#Основной цикл
def main():
    try:
        while True:
            handle_events()
            player_pawn.rotate()  # Добавляем поворот
            move()

            for bot in bots:
                bot.move()
                bot.rotate()

            screen.blit(background, (0, 0))
            screen.blit(player_pawn.image, player_pawn.rect.topleft)  # Исправленный вызов

            for bot in bots:
                screen.blit(bot.image, bot.rect.topleft)
            
            pygame.display.flip()
            clock.tick(FPS)

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        pygame.quit()
        sys.exit(1)

        
#---------------------------------------------------------------------------------------------------
#Запуск основного цикла
if __name__ == "__main__":
    main()

pygame.quit()