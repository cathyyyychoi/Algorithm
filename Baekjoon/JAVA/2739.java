import java.util.Scanner;

public class Main{
  public static void main(String[] args){
    Scanner in = new Scanner(System.in);

    int num = in.nextInt();
    in.close();

    for (int i = 1; i <= 9; i++){
      System.out.println(num + " * " + i + " = " + (num * i));
    }
  }
}
