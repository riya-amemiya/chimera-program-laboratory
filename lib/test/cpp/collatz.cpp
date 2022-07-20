#include <iostream>
long collatz(long x)
{
    if (x <= 0)
    {
        return 1;
    }
    if (x % 2 == 0)
    {
        return collatz(x / 2);
    }
    return collatz(3 * x + 1);
}
int main()
{
    std::cout << collatz(100'0000'0000'0000'0000) << std::endl;
    return 0;
}