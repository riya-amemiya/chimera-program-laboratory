def factorial(n)
    if n == 0
    return 1
    else
    return n * factorial(n-1)
    end
end
for _ in 0..1000000 do
    puts factorial(10)
end