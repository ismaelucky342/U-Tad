int sensorPin = A0; // LM35 is connected to analog pin A0
float temperature = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(sensorPin); // Read the sensor value
  temperature = sensorValue * (5.0 / 1023.0) * 100; // Convert to Celsius
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" °C");
  
  delay(1000); // Wait for 1 second before reading again
}
