int thermistorPin = A0;
int thermistorValue;
float temperature;

void setup() {
  Serial.begin(9600);
}

void loop() {
  thermistorValue = analogRead(thermistorPin);
  temperature = (1 / (log(1 / (1023. / thermistorValue - 1)) / 3950 + 1.0 / 298.15) - 273.15); // Using Steinhart–Hart equation
  
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" C");
  
  delay(1000);
}
