#include <iostream>
using namespace std;

// 동적 계획법
int main(){
    int M, N;
    int dp[10000];
    int sum = 0;
    int minnum = 10000;
    
    cin >> M >> N;
    
    for (int i = 1; i < N; i++)
        dp[i] = i * i;
    
    for (int i = 1; i <= N; i++){
        if (M <= dp[i] && dp[i] <= N){
            sum += dp[i];
            minnum = min(minnum, dp[i]);
        }
    }
    if (sum == 0){
        cout << "-1" << endl;
    }
    else{
        cout << sum << "\n";
        cout << minnum << endl;
    }
}
