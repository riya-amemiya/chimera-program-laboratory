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
#[link(name = "zig", kind = "static")]
extern "C" {
    fn zig_factorial(x: i32) -> i32;
}
#[no_mangle]
pub extern "C" fn rs_call_zig_factorial(x: i32) -> i32 {
    return unsafe { zig_factorial(x) };
}

#[test]
fn test_rs_call_zig_factorial() {
    assert_eq!(rs_call_zig_factorial(5), 120);
}
