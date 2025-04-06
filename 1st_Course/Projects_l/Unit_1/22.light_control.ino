int ldrPin = A0;        // LDR connected to analog pin A0
int relayPin = 7;       // Relay connected to digital pin 7
int ldrValue = 0;       // LDR value (light intensity)
int threshold = 500;    // Threshold for light level to turn on/off the relay

void setup() {
  pinMode(relayPin, OUTPUT);   // Set relay pin as output
  Serial.begin(9600);          // Start serial communication
}

void loop() {
  ldrValue = analogRead(ldrPin);   // Read the LDR value
  
  if (ldrValue < threshold) {
    digitalWrite(relayPin, HIGH);  // Turn on relay (light)
  } else {
    digitalWrite(relayPin, LOW);   // Turn off relay (light)
  }

  Serial.print("LDR Value: ");
  Serial.print(ldrValue);
  Serial.print("\t Light Status: ");
  if (ldrValue < threshold) {
    Serial.println("On");
  } else {
    Serial.println("Off");
  }

  delay(500); // Delay for 500ms
}
