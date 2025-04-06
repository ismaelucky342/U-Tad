#define buttonPin 2
#define ledPin 13

enum State { OFF, ON };
State currentState = OFF;

void setup() {
  pinMode(buttonPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int buttonState = digitalRead(buttonPin);
  
  if (buttonState == HIGH) {
    if (currentState == OFF) {
      currentState = ON;
      digitalWrite(ledPin, HIGH);  // Turn on the LED
    } else {
      currentState = OFF;
      digitalWrite(ledPin, LOW);   // Turn off the LED
    }
    delay(200);  // Debounce delay
  }
}
