fn factorial(n: i64) -> i64 {
    if n <= 0 {
        return 1;
    }
    return factorial(n - 1) * n;
}
fn main() {
    for _ in 0..100000 {
        println!("{}", factorial(10));
    }
}
