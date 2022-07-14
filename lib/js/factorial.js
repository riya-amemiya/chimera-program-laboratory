function factorial(x) {
    if (x <= 0) {
        return 1;
    }
    return factorial(x - 1) * x;
}
for (let i = 0; i < 100000; i++) {
    console.log(factorial(10));
}