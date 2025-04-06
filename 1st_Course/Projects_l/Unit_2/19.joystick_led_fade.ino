#define joystickX A0
#define ledPin 9

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int xVal = analogRead(joystickX);
  int brightness = map(xVal, 0, 1023, 0, 255);  // Map joystick to brightness level
  
  analogWrite(ledPin, brightness);  // Set LED brightness
  
  delay(50);
}
