#include <iostream>
using namespace std;

int check(int num) {
    int num1, num10, num100;
    int count = 0;

    if (num < 100) {
        cout << num << endl;
    }
    else{
        for (int i = 100; i <= num; i++) {
            num100 = i / 100;
            num10 = (i / 10) - ((i / 100) * 10);
            num1 = i % 10;
            if ((num100 - num10) == (num10 - num1)) {
                count++;
            }
        }
        cout << count+99 << endl;
    }

    return 0;
}

int main() {
    int N = 0;
    cin >> N;

    check(N);
}
