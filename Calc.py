import calc
import calc_go
import calc_zig


class Calc:
    def __init__(self) -> None:
        pass

    def __delattr__(self, _: str) -> None:
        pass

    def py_c_factorial(self, x: int) -> int:
        return calc.py_c_factorial(x)

    def py_c_rs_factorial(self, x: int) -> int:
        return calc.py_c_rs_factorial(x)

    def py_rs_factorial(self, x: int) -> int:
        return calc.py_rs_factorial(x)

    def py_c_rs_call_golang_factorial(self, n: int) -> int:
        return calc.py_c_rs_call_golang_factorial(n)

    def factorial(self, n: int) -> int:
        return calc.factorial(n)

    def py_golang_factorial(self, n: int) -> int:
        return calc_go.py_golang_factorial(n)

    def py_rs_call_zig_factorial(self, n: int) -> int:
        return calc.py_rs_call_zig_factorial(n)

    def py_zig_factorial(self, n: int) -> int:
        return calc_zig.py_zig_factorial(n)
