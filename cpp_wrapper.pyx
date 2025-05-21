# Объявление сишных функций для последующей работы
cdef extern from "cpp_functions.h":
    int getWindowPropetries(int Weight, int Height)

# Объявление питоновского говна на основе сишной хуеты для использования
def Py_getWindowPropetries(int Weight, int Height):
    return getWindowPropetries(int Weight, int Height)
