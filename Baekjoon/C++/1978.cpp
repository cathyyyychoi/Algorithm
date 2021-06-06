#include <iostream>
using namespace std;

int main(){
  int size;
  cin >> size;
  int count = size;

  for (int i = 0 ; i < size; i++){
    int n;
    cin >> n;

    if (n == 1){
      count--;
      continue;
    }

    for (int j = 2 ; j < n - 1; j++){
      if (n % j == 0){
        count--;
        break;
      }
    }
  }
  cout << count;

  return 0;
}
