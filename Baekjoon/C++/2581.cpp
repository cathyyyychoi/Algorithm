#include <iostream>
using namespace std;

int main(){
	int m, n;
	int sum = 0;
	int min = -1;
	int count = 0;

	cin >> m >> n;

	for (int i = m; i <= n; i++){
		for (int div = 1; div <= i; div++){
			if (i % div == 0)
				count++;
		}
		if (count == 2){
			if (min == -1)
				min = i;
			sum += i;
		}
		count = 0;
	}
	if (min == -1)
		cout << -1 << endl;
	else
		cout << sum << endl << min << endl;
}
