# НИ ПРИ КАКИХ ОБСТОЯТЕЛЬСТВАХ НЕ ТРОГАТЬ ЭТО ГОВНО

from setuptools import setup
from Cython.Build import cythonize
from distutils.extension import Extension # type: ignore

extension = Extension(
    'cpp_wrapper',
    sources=['cpp_wrapper.pyx', 'cpp_functions.cpp'],
    include_dirs=['.'],
    extra_compile_args=['/std:c++17'],
    libraries=['user32'],
    language='c++',
    zip_safe=False
)

setup(
    name='cpp_wrapper',
    ext_modules=cythonize(extension)
)
