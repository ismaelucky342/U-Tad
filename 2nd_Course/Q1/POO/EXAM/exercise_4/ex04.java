/*
 * Definition: Polymorphism is a fundamental concept in object-oriented programming
 * that allows entities in a program to be treated generically. In other words,
 * an object of a class can be treated as an object of its superclass.
 */

import java.util.ArrayList;
import java.util.List;

/* Flying interface */
interface Flyable {
    void fly();
}

/* Airplane class */
class Airplane implements Flyable {
    @Override
    public void fly() {
        System.out.println("The airplane flies through the sky"); // fly method for the Airplane class
    }
}

/* Bird class */
class Bird implements Flyable {
    @Override
    public void fly() {
        System.out.println("The bird flies through the sky"); // fly method for the Bird class
    }
}
