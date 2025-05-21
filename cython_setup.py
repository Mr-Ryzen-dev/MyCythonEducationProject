# НИ ПРИ КАКИХ ОБСТОЯТЕЛЬСТВАХ НЕ ТРОГАТЬ ЭТУ ХУЙНЮ
# ЭТО ТЕБЕ НЕ ПИТОНА ДУШИТЬ

# Тут импорты сишных функций проходят
# Просто этот файл ставишь в качестве заголовочного и функцию пикаешь

from setuptools import setup
from Cython.Build import cythonize
from distutils.extension import Extension # type: ignore

extension = Extension(
    'cpp_wrapper',
    sources=['cpp_wrapper.pyx', 'cpp_functions.cpp'],
    include_dirs=['.'],
    extra_compile_args=['/std:c++17'],
    language='c++',
    zip_safe=False
)

setup(
    name='cpp_wrapper',
    ext_modules=cythonize(extension)
)
