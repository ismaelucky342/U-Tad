#include <LiquidCrystal.h>

LiquidCrystal lcd(2,3,9,10,11,12);
int sensor; 
float temperature; 

void setup(){
  lcd.begin(16,2);
}

void loop()
{
  lcd.clear();
  lcd.print("Temperatura: ");
  sensor = analogRead(A0);
  temperature = ((sensor * 5000.0)/1023)/10; 
  lcd.setCursor(0, 1);
  lcd.print(temperature);
  delay(1000);
}