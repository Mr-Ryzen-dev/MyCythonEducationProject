from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

extension = Extension(
    'cpp_wrapper',
    sources=['cpp_wrapper.pyx', 'cpp_functions.cpp'],  # Исправлено форматирование
    include_dirs=[np.get_include(), '.'],  # Исправлено форматирование
    extra_compile_args=['/std:c++17'],  # Исправлено форматирование
    libraries=['user32', 'gdi32'],  # Исправлено форматирование
    language='c++',
    extra_link_args=['/SUBSYSTEM:WINDOWS']
)

setup(
    name='cpp_wrapper',
    ext_modules=cythonize([extension]),  # Обернули extension в список
    zip_safe=False
)
