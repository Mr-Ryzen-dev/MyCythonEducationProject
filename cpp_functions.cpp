//Реализации c++ функций

#include "cpp_functions.h"

std::pair<int, int> getScreenSize() {
    const int width = GetSystemMetrics(SM_CXSCREEN);
    const int height = GetSystemMetrics(SM_CYSCREEN);

    return (width == -1 || height == -1) ? std::make_pair(-1, -1)
     : std::make_pair(width, height);
}
// Реализация получения свойств окна

std::pair<int, int> getCursorPosition() {

    POINT p;

    if (!GetCursorPos(&p)) {
        // Возвращаем (-1, -1) в случае ошибки
        return {-1, -1};
    }

    return std::make_pair(p.x, p.y);

}
// Реализация получения местоположения курсора

constexpr double PI = 3.14159265358979323846;
constexpr double RAD_TO_DEG = 180.0 / PI;
constexpr double FULL_CIRCLE = 360.0;

double getBasePlayerRotation(double player_x, double player_y,
     double mouse_x, double mouse_y) {
    
    // Вычисляем разницу координат
    double difference_x = mouse_x - player_x;
    double difference_y = mouse_y - player_y;
    
    // Корректируем угол, чтобы он был в диапазоне 0-360 градусов
    double angle = std::atan2(difference_y, difference_x) * RAD_TO_DEG;

    angle = std::fmod(angle + 180.0 + FULL_CIRCLE, FULL_CIRCLE);
    
    return -angle;
    
}