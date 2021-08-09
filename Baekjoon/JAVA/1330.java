import java.util.Scanner;
//기본적으로 import해서 사용

public class Main{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    //scanner 객체 생성
    //System.in을 사용하여 기보드 입력 값을 읽고 원하는 타입으로 변환하여 리턴

    final int A = sc.nextInt();
    final int B = sc.nextInt();
    //nextInt: 다음 토큰을 int 타입으로 리턴

    if (A > B)
      System.out.println(">");
    else if (A < B)
      System.out.println("<");
    else
      System.out.println("==");
  }
}
