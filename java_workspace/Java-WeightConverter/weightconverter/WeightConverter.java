package weightconverter;
import java.util.Scanner;
public class WeightConverter {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double weight;
        double newWeight;
        int choice;
        
        System.out.println("---WEIGHT CONVENTOR---");
        System.out.println("1-) lbs to kg"); //lbs*0,453
        System.out.println("2-) kg to lbs"); //kg*2,204
        System.out.print("Select: ");
        choice = input.nextInt();
        
        if (choice <= 0 || choice > 2) {
            System.out.println("Invalid input!");
        } else if (choice == 1) {
            System.out.print("Enter the weight you want to convert: ");
            weight = input.nextDouble();
            System.out.println("Converting lbs to kg");
            newWeight = weight*=0.453;
            System.out.printf("Result is: %.2f", newWeight);
        } else if (choice == 2) {
            System.out.print("Enter the weight you want to convert: ");
            weight = input.nextDouble();
            System.out.println("Converting kg to lbs");
            newWeight = weight*=2.204;
            System.out.printf("Result is: %.2f", newWeight);
        } else {
            System.out.println("Something went wrong!");
        }
    }
    
}
