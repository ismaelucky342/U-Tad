// Pushbutton debounce with a capacitor
int buttonPin = 2;
int ledPin = 13;
int buttonState = 0;
int lastButtonState = 0;
unsigned long lastDebounceTime = 0;
unsigned long debounceDelay = 50;

void setup() {
  pinMode(buttonPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int reading = digitalRead(buttonPin);
  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading != buttonState) {
      buttonState = reading;
      if (buttonState == HIGH) {
        digitalWrite(ledPin, HIGH); // Turn the LED on
      } else {
        digitalWrite(ledPin, LOW); // Turn the LED off
      }
    }
  }
  lastButtonState = reading;
}
