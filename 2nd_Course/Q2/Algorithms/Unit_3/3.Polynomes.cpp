#include <iostream>
#include <list>
#include <cmath>

class Polynomial {
private:
    std::list<std::pair<int, int>> terms; // Pair of coefficient and exponent

public:
    void addTerm(int coefficient, int exponent) {
        for (auto& term : terms) {
            if (term.second == exponent) {
                term.first += coefficient;
                return;
            }
        }
        terms.emplace_back(coefficient, exponent);
    }

    void display() const {
        for (auto it = terms.begin(); it != terms.end(); ++it) {
            if (it != terms.begin() && it->first > 0) std::cout << " + ";
            std::cout << it->first << "x^" << it->second;
        }
        std::cout << std::endl;
    }

    Polynomial operator+(const Polynomial& other) const {
        Polynomial result = *this;
        for (const auto& term : other.terms) {
            result.addTerm(term.first, term.second);
        }
        return result;
    }

    Polynomial operator-(const Polynomial& other) const {
        Polynomial result = *this;
        for (const auto& term : other.terms) {
            result.addTerm(-term.first, term.second);
        }
        return result;
    }

    double evaluate(double x) const {
        double result = 0.0;
        for (const auto& term : terms) {
            result += term.first * std::pow(x, term.second);
        }
        return result;
    }
};

int main() {
    Polynomial p1, p2;

    p1.addTerm(3, 2); // 3x^2
    p1.addTerm(5, 1); // 5x^1
    p1.addTerm(2, 0); // 2

    p2.addTerm(4, 2); // 4x^2
    p2.addTerm(-5, 1); // -5x^1
    p2.addTerm(1, 0); // 1

    std::cout << "Polynomial 1: ";
    p1.display();

    std::cout << "Polynomial 2: ";
    p2.display();

    Polynomial sum = p1 + p2;
    std::cout << "Sum: ";
    sum.display();

    Polynomial difference = p1 - p2;
    std::cout << "Difference: ";
    difference.display();

    double x = 2.0;
    std::cout << "Evaluation of Polynomial 1 at x = " << x << ": " << p1.evaluate(x) << std::endl;

    return 0;
}