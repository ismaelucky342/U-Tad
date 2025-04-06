#include <Servo.h>

Servo myServo;
int servoPin = 9;

void setup() {
  myServo.attach(servoPin); // Attach the servo to pin 9
}

void loop() {
  myServo.write(0);   // Move servo to 0 degrees
  delay(1000);
  myServo.write(90);  // Move servo to 90 degrees
  delay(1000);
  myServo.write(180); // Move servo to 180 degrees
  delay(1000);
}
