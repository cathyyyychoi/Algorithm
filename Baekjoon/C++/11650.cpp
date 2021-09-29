#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
    int num;
    cin >> num;
  
    vector<vector<int>> arr(num, vector<int>(2, 0));
    for(int i = 0; i < num; i++){
        cin >> arr[i][0];
        cin >> arr[i][1];
    }
    sort(arr.begin(), arr.end());

    for(int i = 0; i < arr.size(); i++){
        cout << arr[i][0] << " " << arr[i][1] << '\n';
    }

}
