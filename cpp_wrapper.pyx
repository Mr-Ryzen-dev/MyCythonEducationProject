# Объявление сишных функций в Cython
#cython: language_level=3

from libcpp.pair cimport pair

cdef extern from "windows.h":
    int GetSystemMetrics(int)
    int GetCursorPos(void*)
    bint GetCursorPos(POINT *)

ctypedef struct POINT:
    int x
    int y
    bint GetCursorPos(POINT *lpPoint)

cdef extern from "cpp_functions.h":
    pair[int, int] getScreenSize()
    pair[int, int] getCursorPosition()
    pair[double, double] PawnMove(double x, double y, double angle, double speed, char direction)
    double getBasePlayerRotation(double player_x, double player_y, double mouse_x, double mouse_y)

def py_getScreenSize():
    cdef pair[int, int] result = getScreenSize()
    return result.first, result.second

def py_getCursorPosition():
    cdef pair[int, int] result = getCursorPosition()
    return result.first, result.second

def py_getBasePlayerRotation(double player_x, double player_y, double mouse_x, double mouse_y):
    cdef double result = getBasePlayerRotation(player_x, player_y, mouse_x, mouse_y)
    return result

def py_PawnMove(double x, double y, double angle, double speed, char direction):
    cdef pair[double, double] result = PawnMove(x, y, angle, speed, direction)
    return result.first, result.second
