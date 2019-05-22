import java.util.Scanner;
public class Leapy
{
  public static void main (String[]args)
  {
    int year;
    Scanner sc = new Scanner (System.in);
      year = sc.nextInt ();
    if (year % 4 == 0)
      System.out.println ("yes");
    else
        System.out.println ("no");
  }
}
