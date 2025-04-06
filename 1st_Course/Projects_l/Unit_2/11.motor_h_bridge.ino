#define IN1 3
#define IN2 4
#define IN3 5
#define IN4 6
#define ENA 9
#define ENB 10

void setup() {
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  
  analogWrite(ENA, 255);  // Motor speed
  analogWrite(ENB, 255);  // Motor speed
}

void loop() {
  // Forward rotation
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  delay(2000);

  // Reverse rotation
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  delay(2000);
}
