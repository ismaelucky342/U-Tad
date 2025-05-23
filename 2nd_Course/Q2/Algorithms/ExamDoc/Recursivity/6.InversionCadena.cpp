#include <iostream>
#include <string>

void invertirCadena(std::string& str, int inicio, int fin) {
    if (inicio >= fin) return;
    std::swap(str[inicio], str[fin]);
    invertirCadena(str, inicio + 1, fin - 1);
}

int main() {
    std::string s = "Recursividad";
    invertirCadena(s, 0, s.length() - 1);
    std::cout << s << "\n"; // dadivisruceR
    return 0;
}
