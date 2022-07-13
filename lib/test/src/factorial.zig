export fn zig_factorial(n: i32) i32 {
    if (n == 0) {
        return 1;
    } else {
        return n * zig_factorial(n - 1);
    }
}
const std = @import("std");

pub fn main() anyerror!void {
    const stdout = std.io.getStdOut().writer();
    var i: i32 = 0;
    while (i <= 100000) {
        try stdout.print("{}\n", .{zig_factorial(10)});
        i += 1;
    }
}
