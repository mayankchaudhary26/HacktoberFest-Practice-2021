import java.util.Scanner;
public class Fibonacci_Series {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int count = 3;
        int num1 = 0;
        int num2 = 1;
        System.out.print("Enter the number of terms you want: ");
        int terms = input.nextInt();
        System.out.println(0);
        System.out.println(1);
        while (count<=terms){
            int temp = num1 + num2;
            num1 = num2;
            num2 = temp;
            System.out.println(num2);
            count = count + 1;
        }
    }
}