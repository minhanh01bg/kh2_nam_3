#include <random>
#include <iostream>
// #define MAX 100
#define A 3
#define B 5
#define C 0
#define D 9

using namespace std;

int main()
{
    freopen("ACM.INP", "r", stdin);
    freopen("ACM4.OUT", "w", stdout);
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> distrib(A, B);
    std::uniform_int_distribution<> Distrib(C, D);
    int n = 10;
    cout << n << endl;
    for (int i = 0; i < n; i++)
        std::cout << distrib(gen) << " " << Distrib(gen)<<endl;
}