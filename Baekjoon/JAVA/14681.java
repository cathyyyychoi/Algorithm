import java.util.Scanner;
//기본적으로 import해서 사용

public class Main{
  public static void main(String[] args){
    Scanner num = new Scanner(System.in);

    int X = num.nextInt();
    int Y = num.nextInt();

    if (X > 0){
      if (Y > 0){
        System.out.print(1);
      }
      else {
        System.out.print(4);
      }
    }

    else{
      if (Y > 0){
        System.out.print(2);
      }
      else{
        System.out.print(3);
      }
    }
  }
}
