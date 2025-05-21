# Объявление сишных функций для последующей работы
#cython: language_level=3

from libcpp.pair cimport pair

cdef extern from "cpp_functions.h":
    pair[int, int] getWindowProperties()  # Исправлен синтаксис объявления pair

def py_getWindowProperties():
    cdef pair[int, int] result = getWindowProperties()  # Исправлен синтаксис объявления pair
    return result.first, result.second
