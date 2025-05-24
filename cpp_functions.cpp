
//Реализации c++ функций

#include "cpp_functions.h"

std::pair<int, int> getScreenSize() {
    int width = GetSystemMetrics(SM_CXSCREEN);
    int height = GetSystemMetrics(SM_CYSCREEN);

    if (width == -1 || height == -1) {
        return std::make_pair(-1, -1);
    }

    return std::make_pair(width, height);
}
// Реализация получения свойств окна

std::pair<int, int> getCursorPosition() {
    POINT p;

    if (!GetCursorPos(&p)) {
        return std::make_pair(-1, -1); // Возвращаем значение ошибки
    }

    return std::make_pair(p.x, p.y);
}
// Реализация получения местоположения курсора