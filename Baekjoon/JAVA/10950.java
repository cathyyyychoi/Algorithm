import java.util.Scanner;
//기본적으로 import해서 사용

public class Main{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);

    int T = sc.nextInt();
    int arr[] = new int[T];

    for (int i = 0 ; i < T; i++){
      int A = sc.nextInt();
      int B = sc.nextInt();
      arr[i] = A + B;
    }

    sc.close();

    for (int print : arr)
      System.out.println(print);
  }
}
