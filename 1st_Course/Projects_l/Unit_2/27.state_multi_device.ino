#define buttonPin 2
#define motorPin 6
#define ledPin 13

enum State { OFF, ON, MOTOR };
State currentState = OFF;

void setup() {
  pinMode(buttonPin, INPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(motorPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int buttonState = digitalRead(buttonPin);
  
  // If button is pressed, change state
  if (buttonState == HIGH) {
    if (currentState == OFF) {
      currentState = ON;
      digitalWrite(ledPin, HIGH);  // Turn on the LED
      digitalWrite(motorPin, LOW); // Keep motor off
    } else if (currentState == ON) {
      currentState = MOTOR;
      digitalWrite(ledPin, LOW);   // Turn off the LED
      digitalWrite(motorPin, HIGH);  // Turn on the motor
    } else if (currentState == MOTOR) {
      currentState = OFF;
      digitalWrite(ledPin, LOW);   // Turn off the LED
      digitalWrite(motorPin, LOW); // Turn off the motor
    }
    delay(200);  // Debounce delay
  }
}
