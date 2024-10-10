import java.util.Scanner;
public class Main{
    public static void main(String args[])
    {
Scanner sc=new Scanner(System.in);
float bs=sc.nextFloat();
float hra=sc.nextFloat();
float da=sc.nextFloat();
double pf=bs*(12.0f/100);
double gs=bs+hra+da+pf;
System.out.println(pf);
System.out.println(gs);

    }
}