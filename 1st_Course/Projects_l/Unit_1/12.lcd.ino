#include <LiquidCrystal.h>

// Initialize the LCD with the pins connected to RS, E, D4, D5, D6, D7
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  lcd.begin(16, 2); // Initialize the LCD (16 columns, 2 rows)
  lcd.print("Hello, World!"); // Print a message
}

void loop() {
  // Nothing to do here, the message is static
}
