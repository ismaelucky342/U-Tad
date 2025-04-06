#define relayPin 7

void setup() {
  pinMode(relayPin, OUTPUT);
}

void loop() {
  digitalWrite(relayPin, HIGH);  // Relay on (close the switch)
  delay(2000);

  digitalWrite(relayPin, LOW);   // Relay off (open the switch)
  delay(2000);
}
