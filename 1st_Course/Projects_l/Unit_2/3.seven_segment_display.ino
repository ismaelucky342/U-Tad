int segmentPins[] = {2, 3, 4, 5, 6, 7, 8};  // Pin numbers connected to 7-segment display segments
int number[] = {0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F}; // 7-segment digits (0-9)

void setup() {
  for (int i = 0; i < 7; i++) {
    pinMode(segmentPins[i], OUTPUT);
  }
}

void loop() {
  for (int i = 0; i < 10; i++) {
    displayNumber(i);
    delay(1000);
  }
}

void displayNumber(int num) {
  int segments = number[num];
  for (int i = 0; i < 7; i++) {
    digitalWrite(segmentPins[i], (segments >> i) & 1);
  }
}
