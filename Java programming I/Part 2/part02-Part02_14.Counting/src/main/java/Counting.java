
import java.util.Scanner;

public class Counting {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int num = Integer.valueOf(scanner.nextLine());
        
        int count = 0;
        while (count <= num) {
            System.out.println(count);
            count += 1;
        }
    }
}
