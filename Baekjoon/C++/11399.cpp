#include <iostream>
#include <algorithm>
using namespace std;

int main(void){
  int N;
  int person[1000];
  int time = 0;
  
  cin >> N;
  
  for (int i = 0; i < N; i++)
    cin >> person[i];
  
  sort(person, person + N); 
  
  for (int i = 0; i < N; i++)
    for (int j = 0; j <= i; j++)
      time += person[j];
  
  cout << time << '\n';
  return 0;
}
