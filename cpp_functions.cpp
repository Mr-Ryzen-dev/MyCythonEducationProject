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
    
    // Получаем позицию курсора
    if (!GetCursorPos(&p)) {
        return std::make_pair(-1, -1); // Возвращаем значение ошибки
    }
    
    return std::make_pair(p.x, p.y);
}
// Реализация получения местоположения курсора

double getBasePlayerRotation(double player_x, double player_y, double mouse_x, double mouse_y) {
    const double PI = 3.14159265358979323846;
    
    // Вычисляем разницу координат
    double difference_x = mouse_x - player_x;
    double difference_y = mouse_y - player_y;
    
    // В atan2 аргументы должны быть в порядке (y, x)
    double angle_radians = std::atan2(difference_y, difference_x);
    
    // Переводим радианы в градусы
    double angle_degrees = angle_radians * 180.0 / PI;
    
    // Корректируем угол, чтобы он был в диапазоне 0-360 градусов
    angle_degrees = angle_degrees + 180.0;
    while (angle_degrees >= 360.0) {
        angle_degrees -= 360.0;
    }
    while (angle_degrees < 0.0) {
        angle_degrees += 360.0;
    }
    
    return -angle_degrees;
}