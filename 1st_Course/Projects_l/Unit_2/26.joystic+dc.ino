#include <Servo.h>

#define motor1Pin1 6
#define motor1Pin2 7
#define motor2Pin1 8
#define motor2Pin2 9
#define servoPin 10
#define joystickX A0
#define joystickY A1

Servo steeringServo;

void setup() {
  pinMode(motor1Pin1, OUTPUT);
  pinMode(motor1Pin2, OUTPUT);
  pinMode(motor2Pin1, OUTPUT);
  pinMode(motor2Pin2, OUTPUT);
  steeringServo.attach(servoPin);  // Attach servo to pin 10
  Serial.begin(9600);
}

void loop() {
  int xValue = analogRead(joystickX);  // Read X-axis of the joystick
  int yValue = analogRead(joystickY);  // Read Y-axis of the joystick
  
  // Map joystick values to motor speed and direction
  int motorSpeed1 = map(yValue, 0, 1023, -255, 255);
  int motorSpeed2 = motorSpeed1;

  // Control motors based on joystick Y value
  if (motorSpeed1 > 0) {
    digitalWrite(motor1Pin1, HIGH);
    digitalWrite(motor1Pin2, LOW);
    digitalWrite(motor2Pin1, HIGH);
    digitalWrite(motor2Pin2, LOW);
  } else if (motorSpeed1 < 0) {
    digitalWrite(motor1Pin1, LOW);
    digitalWrite(motor1Pin2, HIGH);
    digitalWrite(motor2Pin1, LOW);
    digitalWrite(motor2Pin2, HIGH);
  } else {
    digitalWrite(motor1Pin1, LOW);
    digitalWrite(motor1Pin2, LOW);
    digitalWrite(motor2Pin1, LOW);
    digitalWrite(motor2Pin2, LOW);
  }

  // Map joystick X value to steering servo position
  int servoPosition = map(xValue, 0, 1023, 0, 180);
  steeringServo.write(servoPosition);  // Control steering
  
  delay(50);  // Delay to smooth movement
}
