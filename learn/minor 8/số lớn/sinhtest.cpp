#include <random>
#include <iostream>
// #define MAX 100
#define A 5000
#define B 100000
#define C 1000000000
#define D 10000000000
int main()
{
    freopen("ACM.INP","r",stdin);
    freopen("ACM4.OUT","w",stdout);
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> distrib(A, B);
    std::uniform_int_distribution<> Distrib(C, D);
        std::cout << Distrib(gen) << " " << distrib(gen);
}