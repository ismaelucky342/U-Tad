/* Generic class Box */

class Box<T> {

    private T content; // Generic type variable

    // Getter
    public T getContent() {
        return content;
    }

    // Setter
    public void setContent(T content) {
        this.content = content;
    }
}

/* Main class that implements the main method */

public class Exercise2 {

    public static void main(String[] args) {
        Box<String> stringBox = new Box<>(); // Box of type String
        stringBox.setContent("Hello World"); // Assign content
        System.out.println(stringBox.getContent()); // Display content

        Box<Integer> integerBox = new Box<>(); // Box of type Integer
        integerBox.setContent(42); // Assign content
        System.out.println(integerBox.getContent()); // Display content
    }
}
