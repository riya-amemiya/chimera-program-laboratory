function factorial(x) {
    if (x <= 0) {
        return 1;
    }
    return factorial(x - 1) * x;
}
for (let _ = 0; _ < 1000000; _++) {
    console.log(factorial(10));
}