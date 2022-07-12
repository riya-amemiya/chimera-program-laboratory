include "modules.pyx"
cpdef int py_c_factorial(int x):
    return c_factorial(x)

cpdef int py_c_rs_factorial(int x):
    return c_rs_factorial(x)

cpdef int py_rs_factorial(int x):
    return rs_factorial(x)

cpdef int py_c_rs_call_golang_factorial(int n):
    return c_rs_call_golang_factorial(n)

cpdef int factorial(int n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

cpdef int py_rs_call_zig_factorial(int n):
    return rs_call_zig_factorial(n)

#