#define motorPin 3

void setup() {
  pinMode(motorPin, OUTPUT);
}

void loop() {
  for (int speed = 0; speed <= 255; speed++) {
    analogWrite(motorPin, speed);  // Increase motor speed
    delay(20);
  }
  for (int speed = 255; speed >= 0; speed--) {
    analogWrite(motorPin, speed);  // Decrease motor speed
    delay(20);
  }
}
