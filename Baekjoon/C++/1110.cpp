#include <iostream>
using namespace std;

int main(){
	int num, temp;
	int front, back;
	int count = 0;

	cin >> num;
	temp = num;

	if (num < 0 || num > 99)
		return 0;

	while (1){
		front = num / 10;
		back = num % 10;
		num = back * 10 + ((front + back) % 10);
		count++;

		if (num == temp){
			cout << count << endl;
			break;
		}
	}

	return 0;
}
