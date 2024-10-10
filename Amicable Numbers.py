import java.util.Scanner;
public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        int sum = 0;
        int sum1 = 0;
        for(int i = 1;i<x;i++){
            if(x%i==0){
                sum+=i;
            }
        }
        for(int i = 1;i<y;i++){
            if(y%i == 0){
                sum1+=i;
            }
        }
        if(x == sum1 && y == sum){
            System.out.println("Amicable");
        }
        else{
            System.out.println("Not Amicable");
        }
    }
}