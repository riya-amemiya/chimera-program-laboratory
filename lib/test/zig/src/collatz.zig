export fn collatz(n: i128) i128 {
    if (n <= 1) {
        return 1;
    }
    if (@rem(n, 2) == 0) {
        return collatz(@divExact(n, 2));
    } else {
        return collatz(3 * n + 1);
    }
}
const std = @import("std");

pub fn main() anyerror!void {
    const stdout = std.io.getStdOut().writer();
    try stdout.print("{}", .{collatz(1000000000000000000)});
}
