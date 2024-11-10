class Persona {
    String name; 
    int age; 

    public void talk() {
        System.out.println("Hello my name is " + name + " i'm " + age + " years old");
    }
}

public class program {
    public static void main(String[] args) {
        Persona persona1 = new Persona(); 
        persona1.name = "Juan"; 
        persona1.age = 30; 

        persona1.talk(); 
    }
}