#define IN1 3
#define IN2 4
#define ENA 5

void setup() {
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(ENA, OUTPUT);
  
  analogWrite(ENA, 255);  // Set motor speed
}

void loop() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW); // Motor moving forward
  delay(2000);

  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH); // Motor moving backward
  delay(2000);
}
