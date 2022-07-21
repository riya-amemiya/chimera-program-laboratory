#include <iostream>
int factorial(int x)
{
    if (x <= 0)
    {
        return 1;
    }
    return factorial(x - 1) * x;
}
int main()
{
    for (int i = 0; i < 1000000; i++)
    {
        std::cout << factorial(10) << std::endl;
    }

    return 0;
}