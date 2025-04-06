#include <ShiftOutX.h>

ShiftOutX display(4, 3);  // Using shift register on pins 4 and 3
int buttonPin = 7;
int buttonState = 0;
int counter = 0;

void setup() {
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
  display.setDigitCount(4);  // Set 4-digit display
}

void loop() {
  buttonState = digitalRead(buttonPin);

  // If button is pressed, increment the counter
  if (buttonState == HIGH) {
    counter++;
    if (counter > 9999) {
      counter = 0;  // Reset the counter after 9999
    }
    delay(200);  // Debounce delay
  }

  // Display the counter on the 7-segment display
  display.display(counter);
}
