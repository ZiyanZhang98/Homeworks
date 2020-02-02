import java.util.Scanner;
/**
 * The ticket class includes methods to read, print ticket numbers, and a method to specify the prize money.
 * @author: Ziyan Zhang (118104188)
 */


public class Tickets{
    private static int[] lotto;
    private static final int[] winning_num = {1, 4, 6, 7, 21, 30};
    private static int goal = 0;

    private Tickets(int[] lotto) {
        this.lotto = lotto;
    }

    public static void printNumbers(){
        /**
         * the printNumbers method prints an instance of ticket numbers
         */
        System.out.print("Numbers: ");
        for (int i = 0; i < lotto.length; i++){
            System.out.println(lotto[i]);
        }
    }

    public static void printPrizeMoney() {
        /**
         * the printPrizeMoney method prints the prize of the (current) ticket instance
         */
        for (int i = 0; i < lotto.length; i++) {
            for (int j = 0; j < winning_num.length; j++) {
                if (lotto[i] == winning_num[j]) {
                    goal += 1;
                }
            }
        }
        switch (goal) {
            case 3:
                System.out.println("3 numbers correct: 3 Euro");
                break;
            case 4:
                System.out.println("4 numbers correct: 30 Euro");
                break;
            case 5:
                System.out.println("5 numbers correct: 30 000 Euro");
                break;
            case 6:
                System.out.println("6 numbers correct: 1 000 000 Euro");
                break;
            default:
                System.out.println("0 number correct: 0 Euro");
        }
    }

    public static boolean is_valid(int[] arr, int number){
        /**
         * the is_valid method checks if a number is in the array and returns true/false
         */
        for(int i = 0; i < arr.length; i++){
            if (arr[i] == number){
                System.err.println("invalid input!");
                return false;
            }
        }
        if (number >= 1 && number <= 42){
            return true;
        }
        System.out.print("invalid input!");
        return false;
    }

    public static int[] readTicketNumbers(){
        /**
         * the readTicketNumbers method reads integers and returns an int array which is qualified to our restriction
         */
        int[] arr = new int[6];
        int sum = 0;
        Scanner obj = new Scanner(System.in);
        System.out.println("please enter your lotto numbers:");
        while (sum < 6) {
            int new_num = obj.nextInt();
            if (is_valid(arr, new_num)) {
                arr[sum] = new_num;
                sum += 1;
            }
        }
        return arr;
    }

    public static void main(String[] args) {
        /**
         * the main method creates an int array and a ticket object which implements method printNumbers and printPrizeMoney.
         */
        int[] lotto = Tickets.readTicketNumbers();
        Tickets tic = new Tickets(lotto);
        tic.printNumbers();
        tic.printPrizeMoney();
    }
}
