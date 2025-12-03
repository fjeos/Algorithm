import java.util.Scanner;
public class Main{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String line="";
        while(scan.hasNextLine()) {
            line = scan.nextLine();
            if(line.equals("")) {
                break;
            }
            else {
                 System.out.println(line);
            }
        }
    }
}