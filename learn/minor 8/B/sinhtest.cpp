#include <random>
#include <iostream>
 
int main()
{
    freopen("ACM.INP","r",stdin);
    freopen("ACM9.OUT","w",stdout);
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> distrib(9, 1000);
    for (int n=0; n<10; ++n)
        std::cout << distrib(gen) << ' ';
}