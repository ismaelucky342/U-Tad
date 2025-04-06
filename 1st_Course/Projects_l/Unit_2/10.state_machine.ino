#define buttonPin 2
enum State { OFF, ON };
State currentState = OFF;

void setup() {
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  int buttonState = digitalRead(buttonPin);

  if (buttonState == HIGH) {
    if (currentState == OFF) {
      currentState = ON;
    } else {
      currentState = OFF;
    }
    delay(200);  // Debounce delay
  }

  Serial.print("Current State: ");
  Serial.println(currentState == OFF ? "OFF" : "ON");
}
