import java.util.Scanner;
public class Main{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);

        float x=sc.nextFloat();
        float y=sc.nextFloat();
        float z=(float)x*y;
        System.out.printf("%.2f\n",z);
    }
}