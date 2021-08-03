#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
  vector<string> croat = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
  int index;

  string word;
  cin >> word;
  for (int i = 0; i < croat.size(); i++){
    while (1){
      index = word.find(croat[i]);
      if (index == string::npos)
        break;
      word.replace(index, croat[i].length(), "#");
    }
  }
  cout << word.length();
}
