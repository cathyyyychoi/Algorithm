#include <iostream>
using namespace std;

int d(int n){
  int sum[5] = { 0 };

  sum[0] = n / 10000;
	sum[1] = (n % 10000) / 1000;
	sum[2] = (n  % 1000) / 100;
	sum[3] = (n % 100) / 10;
	sum[4] = (n % 10);

	int result = n + sum[0] + sum[1] + sum[2] + sum[3] + sum[4];

	return result;
}

int main(){
  bool check[10001] = { 0 };
  int n = 1;

  while (1){
    int t = d(n);
    if (n >= 10000)
      break;
    if (t <= 10000)
      check[t] = 1;

    n++;
  }

  for (int i = 0; i < 10000; i++){
    if (check[i] == 0)
      cout << i << endl;
  }
  return 0;
}
