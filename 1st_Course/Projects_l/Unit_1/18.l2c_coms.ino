#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2); // LCD address and size (16x2)

void setup() {
  lcd.begin(); // Initialize the LCD
  lcd.print("Hello, World!"); // Print a message
}

void loop() {
  // Nothing to do here
}
