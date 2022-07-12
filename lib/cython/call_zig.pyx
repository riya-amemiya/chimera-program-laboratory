cdef extern from "../zig/zig-out/lib/lib.zig.h":
    cdef int zig_factorial(int n)
cpdef int py_zig_factorial(int n):
    return zig_factorial(n)