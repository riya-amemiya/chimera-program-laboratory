def collatz(number: int) -> int:
    if number <= 0:
        return 1
    if number % 2 == 0:
        return collatz(number // 2)
    else:
        return collatz(3 * number + 1)


print(collatz(1000000000000000000))
