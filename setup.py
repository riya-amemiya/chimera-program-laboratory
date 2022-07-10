
from distutils.core import setup
from distutils.extension import Extension

from Cython.Distutils import build_ext

sourcesList = [
    Extension(
        name='calc',
        sources=["./lib/cython/main.pyx"],
        language='c++',
        include_dirs=['./lib/include', "./lib/go"],
        extra_compile_args=["-stdlib=libc++", "-Wdeprecated"],
        library_dirs=["./obj", "./target/release"],
        libraries=['main', "rs_library"],
    ),
    Extension(
        name='calc_go',
        sources=["./lib/cython/call_go.pyx"],
        language='c++',
        include_dirs=["./lib/go"],
        extra_compile_args=["-stdlib=libc++", "-Wdeprecated"],
        library_dirs=["./lib/go"],
        libraries=["go_main"],
    )
]

for i in sourcesList:
    setup(
        cmdclass=dict(build_ext=build_ext),
        ext_modules=[i]
    )
