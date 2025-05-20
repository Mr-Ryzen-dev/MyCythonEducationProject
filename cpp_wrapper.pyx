# Объявление сишных функций для последующей работы
cdef extern from "cpp_functions.h":
    int relos(int a)

# Объявление питоновского говна на основе сишной хуеты для использования
def py_relos(int a):
    return relos(a)
