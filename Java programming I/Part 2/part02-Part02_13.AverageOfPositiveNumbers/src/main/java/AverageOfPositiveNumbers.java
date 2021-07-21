
import java.util.Scanner;

public class AverageOfPositiveNumbers {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int total = 0;
        int count = 0;
        
        while (true) {
            
            int number = Integer.valueOf(scanner.nextLine());
            
            if (number == 0) {
                System.out.println("Cannot calculate the average");
                break;
            }else {
                if (number >0) {
                    total += number;
                    count += 1;                
                }
            }
        }
        double average = (double) total / count;
        System.out.println(average);

    }
}
