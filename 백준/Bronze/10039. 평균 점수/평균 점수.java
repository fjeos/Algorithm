import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int scores[] = new int[5];

        for(int i = 0; i < 5; i++) {
            scores[i] = scanner.nextInt();
        }

        int sum = 0;
        for (int score : scores) {
            if (score < 40) {
                score = 40;
            }
            sum += score;
        }
        System.out.println(sum/5);

    }
}