int tiltPin = 2; // Tilt sensor connected to pin 2
int tiltState = 0;

void setup() {
  pinMode(tiltPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  tiltState = digitalRead(tiltPin); // Read the tilt sensor state
  if (tiltState == HIGH) {
    Serial.println("Tilt Detected");
  } else {
    Serial.println("No Tilt");
  }
  delay(500);
}
