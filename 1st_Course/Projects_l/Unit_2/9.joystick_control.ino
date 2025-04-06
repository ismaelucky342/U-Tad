#define joystickX A0
#define joystickY A1

void setup() {
  Serial.begin(9600);
}

void loop() {
  int xVal = analogRead(joystickX);
  int yVal = analogRead(joystickY);
  
  Serial.print("X: ");
  Serial.print(xVal);
  Serial.print(" Y: ");
  Serial.println(yVal);
  
  delay(100);
}
