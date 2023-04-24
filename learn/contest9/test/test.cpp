#include <random>
#include <iostream>
#define MAX 40
#define A 7
#define B 10
int main()
{
    freopen("ACM.INP","r",stdin);
    freopen("ACM000000001.OUT","w",stdout);
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> distrib(A, B);

    std::cout << MAX << std::endl;
    
    for (int n = 0; n < MAX; ++n) {
        std::cout << distrib(gen) << "\n";
    }
}