#define transistorPin 8
#define loadPin 9

void setup() {
  pinMode(transistorPin, OUTPUT);
  pinMode(loadPin, OUTPUT);
}

void loop() {
  digitalWrite(transistorPin, HIGH);  // Switch on transistor to allow current flow
  digitalWrite(loadPin, HIGH);        // Turn on the load (e.g., LED or motor)
  delay(2000);
  
  digitalWrite(transistorPin, LOW);   // Switch off transistor, cutting current to load
  digitalWrite(loadPin, LOW);         // Turn off the load
  delay(2000);
}
