# НИ ПРИ КАКИХ ОБСТОЯТЕЛЬСТВАХ НЕ ТРОГАТЬ ЭТУ ХУЙНЮ
from setuptools import setup
from Cython.Build import cythonize
from distutils.extension import Extension

extension = Extension(
    'cpp_wrapper',
    sources=['cpp_wrapper.pyx', 'cpp_functions.cpp'],
    include_dirs=['.'],
    extra_compile_args=['/std:c++17'],
    language='c++'
)

setup(
    name='cpp_wrapper',
    ext_modules=cythonize(extension)
)
