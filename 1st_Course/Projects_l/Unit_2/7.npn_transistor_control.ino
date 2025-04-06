#define transistorPin 8
#define ledPin 9

void setup() {
  pinMode(transistorPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  digitalWrite(transistorPin, HIGH);  // Transistor on
  digitalWrite(ledPin, HIGH);         // LED on
  delay(1000);

  digitalWrite(transistorPin, LOW);   // Transistor off
  digitalWrite(ledPin, LOW);          // LED off
  delay(1000);
}
