// Костя, сюда блять даже не лезь
// Прошу

#include "cpp_functions.h"
#include <iostream>
#include <utility>
#include <windows.h>

std::pair<int, int> getWindowProperties() {
    int weight = GetSystemMetrics(SM_CXSCREEN);
    int height = GetSystemMetrics(SM_CYSCREEN);
    return std::make_pair(weight, height);
}

