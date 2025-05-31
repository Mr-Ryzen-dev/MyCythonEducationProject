//подключение библиотек
#ifndef CPP_FUNCTIONS_H
#define CPP_FUNCTIONS_H

#include <iostream>
#include <windows.h>
#include <cmath>

//объявление функций
std::pair<int, int> getScreenSize();
// Функция получения свойств окна
// Возвращает ширину и высоту окна в виде пары

std::pair<int, int> getCursorPosition();
// Возвращает координаты курсора в виде пары

double getBasePlayerRotation(double player_x, double player_y, double mouse_x, double mouse_y);
// Возвращает угол поворота, на который надо повернуть пешку

std::pair<int, int> PawnMove(int x, int y, double angle, int speed, int direction);
// Возвращает координаты на который надо сдвинуть пешку

#endif // CPP_FUNCTIONS_H
