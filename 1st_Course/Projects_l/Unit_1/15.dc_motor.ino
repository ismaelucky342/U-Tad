int motorPin1 = 6; // Motor control pins
int motorPin2 = 7;
int enablePin = 5;

void setup() {
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(enablePin, OUTPUT);
}

void loop() {
  // Rotate motor in one direction
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, LOW);
  analogWrite(enablePin, 255); // Full speed
  delay(2000); // Run for 2 seconds
  
  // Rotate motor in the opposite direction
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, HIGH);
  analogWrite(enablePin, 255); // Full speed
  delay(2000); // Run for 2 seconds
  
  analogWrite(enablePin, 0); // Stop motor
  delay(1000); // Wait for 1 second
}
