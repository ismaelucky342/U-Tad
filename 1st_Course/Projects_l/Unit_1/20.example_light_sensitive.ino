int ldrPin = A0;        // LDR is connected to analog pin A0
int ledPin = 9;          // LED is connected to digital pin 9
int ldrValue = 0;        // Variable to store LDR value
int brightness = 0;      // Variable to store LED brightness

void setup() {
  pinMode(ledPin, OUTPUT);   // Set the LED pin as an output
  Serial.begin(9600);        // Begin serial communication for debugging
}

void loop() {
  ldrValue = analogRead(ldrPin);     // Read the LDR value (0 to 1023)
  brightness = map(ldrValue, 0, 1023, 0, 255); // Map LDR value to LED brightness (0-255)
  
  analogWrite(ledPin, brightness);   // Set the LED brightness
  
  Serial.print("LDR Value: ");
  Serial.print(ldrValue);
  Serial.print("\t LED Brightness: ");
  Serial.println(brightness);
  
  delay(100);  // Wait for 100ms
}
