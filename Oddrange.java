import java.util.Scanner;
public class Oddrange
{    
public static void main(String[] args)
{
int start,end;
Scanner sc=new Scanner(System.in);        
start=sc.nextInt();
end=sc.nextInt();
for(int i=start+1;i<=end;i++)
{       
if(i%2!=0)
System.out.println(i);
}
}
}
