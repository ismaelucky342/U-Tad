#include <LiquidCrystal.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2; 


LiquidCrystal lcd(rs, en, d4, d5, d6, d7);


const int potPin = A0;

void setup() {
  lcd.begin(16, 2);

  lcd.print("Hello World");
}

void loop() {
  int potValue = analogRead(potPin);

  char character = map(potValue, 0, 1023, 32, 126);

  lcd.clear();

  lcd.setCursor(0, 0);
  lcd.print("Pot Value:");

  lcd.setCursor(0, 1);
  lcd.print(character);

  delay(100);
}
