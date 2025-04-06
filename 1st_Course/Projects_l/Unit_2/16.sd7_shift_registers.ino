#include <ShiftOutX.h>

ShiftOutX display(4, 3);  // Using shift register on pins 4 and 3

void setup() {
  Serial.begin(9600);
  display.setDigitCount(4);
}

void loop() {
  for (int i = 0; i < 10000; i++) {
    display.display(i);
    delay(1000);
  }
}
