def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


for i in range(1000000):
    print(factorial(10))
