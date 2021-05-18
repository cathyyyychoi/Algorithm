#include <iostream>
using namespace std;

int main()
{
	int a, b;

	cin >> a >> b;
	cout << a * (b % 10) << endl;    //3번에 해당하는 코드
	cout << a*((b / 10)%10) << endl;  //4번에 해당하는 코드
	cout << a * (b / 100) << endl;   //5번에 해당하는 코드
	cout << a * b << endl;            //6번에 해당하는 코드

	return 0;
}
