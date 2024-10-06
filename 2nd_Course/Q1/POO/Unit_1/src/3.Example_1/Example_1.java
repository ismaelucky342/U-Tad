public class Example_1 {
    private int x; //member 

    //constructor
    public Example_1(int x) {
        this.x = x; 
    }

    //local var method 
    public void printSum(int y) {
        int sum = x + y; 
        System.out.println("The sum is: " + sum); 
    }
}