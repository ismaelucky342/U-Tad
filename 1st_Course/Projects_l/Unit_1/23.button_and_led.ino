int buttonPin = 2;   // Pushbutton connected to pin 2
int ledPin = 13;     // LED connected to pin 13
int buttonState = 0; // Current button state
int lastButtonState = 0; // Previous button state
unsigned long lastDebounceTime = 0; // Last time button state changed
unsigned long debounceDelay = 50;   // Debounce delay in milliseconds

void setup() {
  pinMode(buttonPin, INPUT);  // Set button pin as input
  pinMode(ledPin, OUTPUT);    // Set LED pin as output
  Serial.begin(9600);         // Begin serial communication
}

void loop() {
  int reading = digitalRead(buttonPin);  // Read the button state
  
  // Check if the button state has changed
  if (reading != lastButtonState) {
    lastDebounceTime = millis();  // Record the time of the state change
  }
  
  if ((millis() - lastDebounceTime) > debounceDelay) {
    // If the button state has changed after the debounce delay, update the button state
    if (reading != buttonState) {
      buttonState = reading;
      
      if (buttonState == HIGH) {
        digitalWrite(ledPin, HIGH);  // Turn on the LED
      } else {
        digitalWrite(ledPin, LOW);   // Turn off the LED
      }
    }
  }

  lastButtonState = reading;  // Update the previous button state
}
