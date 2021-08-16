// long sum(int[] a)
// class 이름: Test
// a: 합을 구해야하는 정수 n개가 저장되어 있는 배열
// return: a에 포함되어 있는 정수 n개의 합

public class Test{
  long sum(int[] a){
    long ans = 0;

    for (int i = 0; i < a.length; i++){
      ans += a[i];
    }
    return ans;
  }
}
