int relayPin = 8; // Relay control pin

void setup() {
  pinMode(relayPin, OUTPUT);
}

void loop() {
  digitalWrite(relayPin, HIGH); // Turn on relay (and connected device)
  delay(1000); // Wait for 1 second
  digitalWrite(relayPin, LOW);  // Turn off relay (and connected device)
  delay(1000); // Wait for 1 second
}
