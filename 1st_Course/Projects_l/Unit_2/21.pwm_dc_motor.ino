#define motorPin 3
#define joystickX A0

void setup() {
  pinMode(motorPin, OUTPUT);
}

void loop() {
  int joystickValue = analogRead(joystickX);
  int motorSpeed = map(joystickValue, 0, 1023, 0, 255);  // Map joystick value to motor speed
  
  analogWrite(motorPin, motorSpeed);  // Control motor speed
  
  delay(50);
}
