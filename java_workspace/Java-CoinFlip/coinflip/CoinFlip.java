package coinflip;

import java.util.Random;

public class CoinFlip {

    public static void main(String[] args) {
        Random random = new Random();
        
        boolean isHeads = random.nextBoolean();
        if (isHeads == true) {
            System.out.println("Heads");
        } else {
            System.out.println("Tails");
        }
    }
    
}
