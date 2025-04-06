#include <Servo.h>

int potPin = A0;         // Potentiometer connected to A0
int potValue = 0;         // Variable to store potentiometer value
int servoAngle = 0;       // Variable to store servo angle

Servo myServo;            // Create a Servo object

void setup() {
  myServo.attach(9);      // Servo motor is connected to pin 9
  Serial.begin(9600);     // Begin serial communication for debugging
}

void loop() {
  potValue = analogRead(potPin);      // Read potentiometer value (0 to 1023)
  servoAngle = map(potValue, 0, 1023, 0, 180); // Map potentiometer value to servo angle (0-180 degrees)
  
  myServo.write(servoAngle);   // Set the servo angle
  
  Serial.print("Potentiometer Value: ");
  Serial.print(potValue);
  Serial.print("\t Servo Angle: ");
  Serial.println(servoAngle);
  
  delay(50); // Wait for 50ms
}
