#include <random>
#include <iostream>
#define MAX 100
#define A 5000000
#define B 10000000
int main()
{
    freopen("ACM.INP","r",stdin);
    freopen("ACM16.OUT","w",stdout);
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> distrib(A, B);

    std::cout << MAX << std::endl;
    
    for (int n = 0; n < MAX; ++n)
        std::cout << distrib(gen) << " ";
}