extern "C" {
    fn golang_factorial(n: i32) -> i32;
}

#[no_mangle]
pub extern "C" fn rs_call_golang_factorial(n: i32) -> i32 {
    return unsafe { golang_factorial(n) };
}

#[no_mangle]
pub extern "C" fn rs_factorial(x: i32) -> i32 {
    if x <= 0 {
        return 1;
    }
    return rs_factorial(x - 1) * x;
}
