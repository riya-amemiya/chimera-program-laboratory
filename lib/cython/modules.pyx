
cdef extern from "../include/main.hpp" namespace "cpp_main_lib":
    cdef int c_factorial(int x)

cdef extern from "../include/main.hpp" namespace "cpp_main_lib":
    cdef int c_rs_factorial(int x)

cdef extern from "../include/rs.hpp" namespace "rs_to_py_lib":
    cdef int rs_factorial(int x)

cdef extern from "../include/main.hpp" namespace "cpp_main_lib":
    cdef int c_rs_call_golang_factorial(int n)

