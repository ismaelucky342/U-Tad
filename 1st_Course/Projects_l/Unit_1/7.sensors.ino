int ldrPin = A0; // LDR connected to analog pin A0
int ldrValue = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  ldrValue = analogRead(ldrPin); // Read the LDR value
  Serial.println(ldrValue); // Print the value
  delay(500);
}
