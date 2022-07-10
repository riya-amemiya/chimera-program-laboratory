#pragma once
#include <cstdarg>
#include <cstdint>
#include <cstdlib>
#include <ostream>
#include <new>
namespace rs_to_py_lib {
extern "C" {

extern int32_t golang_factorial(int32_t n);

int32_t rs_call_golang_factorial(int32_t n);

int32_t rs_factorial(int32_t x);

} // extern "C"
}