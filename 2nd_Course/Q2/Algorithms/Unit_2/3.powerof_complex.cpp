// Exercise 2: Power of a complex number

#include <iostream>

using namespace std;

class Complex {
    private:
        double real;
        double imaginary;

    public:
        // Standard constructor
        Complex(double r, double i) {
            real = r;
            imaginary = i;
        }

        // Copy constructor
        Complex(const Complex &other) {
            real = other.real;
            imaginary = other.imaginary;
        }

        // Method to multiply two complex numbers
        Complex multiply(const Complex &other) const {
            double newReal = (real * other.real) - (imaginary * other.imaginary);
            double newImaginary = (real * other.imaginary) + (imaginary * other.real);
            return Complex(newReal, newImaginary);
        }

        // Recursive function to calculate the power of a complex number
        Complex power(int exponent) const {
            if (exponent == 0) return Complex(1, 0); // Base case: any number raised to 0 is 1
            if (exponent == 1) return *this; // Base case: power of 1 is the same number

            // Divide and conquer: reduce the exponent by half to improve efficiency
            Complex half = power(exponent / 2);
            Complex result = half.multiply(half);

            // If the exponent is odd, multiply once more by the base number
            if (exponent % 2 != 0) {
                result = result.multiply(*this);
            }

            return result;
        }

        // Method to display the complex number
        void display() const {
            cout << real;
            if (imaginary >= 0)
                cout << " + " << imaginary << "i" << endl;
            else
                cout << " - " << -imaginary << "i" << endl;
        }
};

int main() {
    double real, imaginary;
    int exponent;

    // Ask the user to input a complex number
    cout << "Enter the real part of the complex number: ";
    cin >> real;
    cout << "Enter the imaginary part of the complex number: ";
    cin >> imaginary;
    cout << "Enter the exponent to which you want to raise the complex number: ";
    cin >> exponent;

    // Create an object of the Complex class
    Complex num(real, imaginary);

    // Calculate the power using the recursive function
    Complex result = num.power(exponent);

    // Display the result
    cout << "The result of (" << real << " + " << imaginary << "i)^" << exponent << " is: ";
    result.display();

    return 0;
}
