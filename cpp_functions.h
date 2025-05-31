//подключение библиотек
#ifndef CPP_FUNCTIONS_H
#define CPP_FUNCTIONS_H

#include <iostream>
#include <windows.h>
#include <math.h>

//объявление функций
std::pair<int, int> getScreenSize();
// Функция получения свойств окна
// Возвращает ширину и высоту окна в виде пары

std::pair<int, int> getCursorPosition();
// Возвращает координаты курсора в виде пары

double getBasePlayerRotation(double player_x, double player_y, double mouse_x, double mouse_y);
// Возвращает угол поворота, на который надо повернуть пешку

#endif // CPP_FUNCTIONS_H
