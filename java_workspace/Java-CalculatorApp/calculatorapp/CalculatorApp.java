package calculatorapp;

import java.util.Scanner;

public class CalculatorApp {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double number;
        double secondNumber;
        double result = 0;
        int operation;
        System.out.println("---CALCULATOR APP---");
        System.out.print("Number: ");
        number = input.nextDouble();
        result += number;
        
        while (true) {
            System.out.println("Operations: \n1-) +\n2-) -\n3-) *\n4-) /\n0-) Exit");
            System.out.print("Select Operation: ");
            operation = input.nextInt();
            if (operation == 0) {
                break;
            }
            System.out.print("Number: ");
            secondNumber = input.nextDouble();
            
            if (operation == 1) {
                result += secondNumber;
                System.out.println("Current result is: " + result);
            } else if (operation == 2) {
                result -= secondNumber;
                System.out.println("Current result is: " + result);
            } else if (operation == 3) {
                result *= secondNumber;
                System.out.println("Current result is: " + result);
            } else if (operation == 4) {
                if (secondNumber == 0) {
                    System.out.println("Number can't be divided by 0!");
                    continue;
                }
                result /= secondNumber;
                System.out.println("Current result is: " + result);
            } else{
                System.out.println("Invalid input!");
            }
        }
    }
    
}
