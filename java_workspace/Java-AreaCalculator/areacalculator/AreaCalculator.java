package areacalculator;

import java.util.Scanner;

public class AreaCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("---AREA CALCULATOR---");
        
        System.out.println("Select which shape do you want to calculate");
        System.out.println("Options: 1-Circle, 2-Square, 3-Triangle");
        System.out.print("Your choice: ");
        int format = input.nextInt();
        
        switch (format) {
            case 1:
                System.out.print("Enter radius: ");
                double radius = input.nextDouble();
                double circleArea = Math.PI * Math.pow(radius, 2);
                System.out.println("Area of circle is: " + circleArea);
                break;
                
            case 2:
                System.out.print("Enter side: ");
                double side = input.nextDouble();
                double squareArea = Math.pow(side, 2);
                System.out.println("Area of square is: " + squareArea);
                break;
                
            case 3:
                System.out.print("Enter base: ");
                double base = input.nextDouble();
                System.out.print("Enter height: ");
                double height = input.nextDouble();
                double triangleArea = (base*height) / 2;
                System.out.println("Area of triangle is: " + triangleArea);
                break;
                
            default:
                System.out.println("You made an invalid selection!");
                System.out.println("App will close now.");
        }
        
    }
    
}
