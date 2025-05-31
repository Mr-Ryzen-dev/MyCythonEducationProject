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
constexpr double DIAGONAL_CORRECTION = 0.70710678118;

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

enum class MovementDirection {
    LEFT = 1,   // Влево
    RIGHT = 2,  // Вправо
    FORWARD = 3,// Вперед
    BACKWARD = 4// Назад
};

std::pair<int, int> PawnMove(int x, int y, double angle, int speed, int direction) {
    // Преобразуем угол в радианы один раз
    const double radians = angle * PI / 180.0;
    
    // Предварительно вычисляем тригонометрические функции
    const double cos_angle = std::cos(radians);
    const double sin_angle = std::sin(radians);
    
    double dx = 0.0;
    double dy = 0.0;

    switch (static_cast<MovementDirection>(direction)) {
        case MovementDirection::LEFT: // Движение влево
            dx = -speed * sin_angle;
            dy = speed * cos_angle;
            break;
        
        case MovementDirection::RIGHT: // Движение вправо
            dx = speed * sin_angle;
            dy = -speed * cos_angle;
            break;
        
        case MovementDirection::FORWARD: // Движение вперед
            dx = speed * cos_angle;
            dy = -speed * sin_angle; // Учитываем инвертированную ось Y
            break;
        
        case MovementDirection::BACKWARD: // Движение назад
            dx = -speed * cos_angle;
            dy = speed * sin_angle;
            break;
        
        default:
            std::cerr << "Unknown direction: " << direction << std::endl;
            return {x, y};
    }

    // Возвращаем новые координаты с приведением к целым числам
    return {
        x + static_cast<int>(std::round(dx)),
        y + static_cast<int>(std::round(dy))
    };
}