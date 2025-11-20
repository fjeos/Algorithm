import java.util.Scanner;
public class Main{
    public static void main(String[] args) {
       Scanner scan = new Scanner(System.in);
       int sum=0,i; 
       int N = scan.nextInt();
       String a = scan.next();
       scan.close();
       
       for(i=0; i<N; i++) {
    	   sum+= a.charAt(i)-'0';
       }
       System.out.println(sum);    }
}