#include <Servo.h>

#define joystickX A0
#define joystickY A1
Servo myServo;

void setup() {
  myServo.attach(9);  // Attach servo to pin 9
  Serial.begin(9600);
}

void loop() {
  int xVal = analogRead(joystickX);
  int yVal = analogRead(joystickY);
  
  int servoPosition = map(xVal, 0, 1023, 0, 180);  // Map joystick X to servo position
  
  myServo.write(servoPosition);  // Set servo position
  
  Serial.print("X: ");
  Serial.print(xVal);
  Serial.print(" Y: ");
  Serial.println(yVal);
  
  delay(50);
}
