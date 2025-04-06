#include <LiquidCrystal.h>

#define thermistorPin A0  // Thermistor connected to analog pin A0
#define B 3950  // B value for the thermistor
#define R0 10000  // Resistance of thermistor at 25°C
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  lcd.begin(16, 2);  // Initialize LCD (16x2 display)
  lcd.print("Temperature:");
}

void loop() {
  int rawValue = analogRead(thermistorPin);  // Read the thermistor value
  float resistance = (1023.0 / rawValue) - 1.0;
  resistance = R0 * resistance;

  // Calculate the temperature in Celsius
  float temperature = 1.0 / (log(resistance / R0) / B + 1.0 / 298.15) - 273.15;

  // Display temperature on the LCD
  lcd.setCursor(0, 1);
  lcd.print(temperature);
  lcd.print(" C");
  
  delay(1000);  // Wait for 1 second
}
