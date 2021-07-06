#include <iostream>
using namespace std;

bool check(int num){
    if (num < 100)
        return true;
    int num1, num2, num3;
    num1 = a % 100;
    num2 = a % 100 / 10;
    num3 = a / 100;

    if ((num3 - num2) == (num2 - num1))
        return true;
    return false;
}

int main(){
    int N;
    int count = 0;
    cin >> N;
    for (int i = 1; i <= N; i++){
        if (check(i))
            count++;
    }
}
