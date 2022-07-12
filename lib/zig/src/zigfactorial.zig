export fn zig_factorial(n: i32) i32 {
    if (n == 0) {
        return 1;
    } else {
        return n * zig_factorial(n - 1);
    }
}
