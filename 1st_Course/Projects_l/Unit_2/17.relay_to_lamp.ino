#define relayPin 7

void setup() {
  pinMode(relayPin, OUTPUT);
}

void loop() {
  digitalWrite(relayPin, HIGH);  // Turn on the device
  delay(3000);                   // Keep it on for 3 seconds
  digitalWrite(relayPin, LOW);   // Turn off the device
  delay(3000);                   // Keep it off for 3 seconds
}
