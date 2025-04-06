int ledPin = 9; // PWM pin

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  for (int brightness = 0; brightness <= 255; brightness++) {
    analogWrite(ledPin, brightness); // Increase brightness
    delay(10); // Wait for 10 milliseconds
  }
  
  for (int brightness = 255; brightness >= 0; brightness--) {
    analogWrite(ledPin, brightness); // Decrease brightness
    delay(10); // Wait for 10 milliseconds
  }
}
