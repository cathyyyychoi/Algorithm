#include<iostream>
#include<string>
using namespace std;

int list[26];

int main() {
	string str;
	cin >> str;
  
	for (int i = 0; i < str.size(); i++) {
		list[str[i] - 97]++;
	}
  
	for (int i = 0; i < 26; i++) {
		cout << list[i]<<" ";
	}
  
}
