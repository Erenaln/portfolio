package guessthenumber;

import java.util.Random;
import java.util.Scanner;

public class GuessTheNumber {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Random random = new Random();
        int number = random.nextInt(1,101);
        
        
        while (true) {            
            System.out.print("Guess a number between 1-100: ");
            int guess = input.nextInt();
            
            
            if (guess < 0) {
                System.out.println("Your guess is out of bounds!");
            } else if (guess > 100) {
                System.out.println("Your guess is out of bounds!");
            } else if (guess == number ) {
                System.out.println("Your guess is right! Congrats!");
                break;
            } else {
                System.out.println("Wrong");
            }
        }
    }
    
}
