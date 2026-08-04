package compoundinterestcalculator;

import java.util.Scanner;

public class CompoundInterestCalculator {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the deposit amount: ");
        double depositAmount = input.nextDouble();
        System.out.print("Enter the interest rate (without % sign): ");
        double interestRate = input.nextDouble();
        System.out.println("Enter the number of period: ");
        int numberOfPeriod = input.nextInt();
        System.out.print("Enter the maturity: ");
        int maturity = input.nextInt();
        
        interestRate /= 100;
        
        double lastAmount;
        double inParantheses = 1 + interestRate/numberOfPeriod;
        double exponent = numberOfPeriod * maturity;
        
        lastAmount = (depositAmount * (Math.pow(inParantheses, exponent)));
        System.out.println("Your expected last amount is " + lastAmount);
    }
    
}
