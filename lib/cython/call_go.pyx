
cdef extern from "../go/libgo_main.h":
    cdef int golang_factorial(int n)

cpdef int py_golang_factorial(int n):
    return golang_factorial(n)