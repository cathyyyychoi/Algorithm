import java.util.Scanner;
//기본적으로 import해서 사용

public class Main{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    //scanner 객체 생성
    //System.in을 사용하여 기보드 입력 값을 읽고 원하는 타입으로 변환하여 리턴

    int A = sc.nextInt();
    int B = sc.nextInt();
    int C = sc.nextInt();
    //nextInt: 다음 토큰을 int 타입으로 리턴
    //final이 붙는 경우 변경할 수 없는 상수값
    sc.close();
    //키보드 입력은 크게 상관 없지만, 파일 입출력의 경우 잘 닫아주기!

    System.out.println((A + B) % C);
    System.out.println((A % C + B % C) % C);
    System.out.println((A * B) % C);
    System.out.println((A % C * B % C) % C);
  }
}
