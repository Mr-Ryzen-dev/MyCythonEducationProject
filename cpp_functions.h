//подключение библиотек
#ifndef CPP_FUNCTIONS_H
#define CPP_FUNCTIONS_H

#include <iostream>
#include <windows.h>
#include <cstdint>

//объявление функций
std::pair<int, int> getScreenSize();
// Функция получения свойств окна
// Возвращает ширину и высоту окна в виде пары

std::pair<int, int> getCursorPosition();
// Возвращает координаты курсора в виде пары

#endif // CPP_FUNCTIONS_H
