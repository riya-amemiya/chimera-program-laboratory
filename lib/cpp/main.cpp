#include "main.hpp"

#include <iostream>
namespace cpp_main_lib
{
    int c_factorial(int x)
    {
        if (x <= 0)
        {
            return 1;
        }
        return c_factorial(x - 1) * x;
    }
    int c_rs_factorial(int x) { return rs_to_py_lib::rs_factorial(x); }
    int c_rs_call_golang_factorial(int n) { return rs_to_py_lib::rs_call_golang_factorial(n); }
} // namespace cpp_main_lib
