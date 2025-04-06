int redPin = 9;    // Red pin of the RGB LED
int greenPin = 10; // Green pin of the RGB LED
int bluePin = 11;  // Blue pin of the RGB LED

int buttonRed = 2;    // Button to control red color
int buttonGreen = 3;  // Button to control green color
int buttonBlue = 4;   // Button to control blue color

void setup() {
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  
  pinMode(buttonRed, INPUT);
  pinMode(buttonGreen, INPUT);
  pinMode(buttonBlue, INPUT);
}

void loop() {
  if (digitalRead(buttonRed) == HIGH) {
    digitalWrite(redPin, HIGH);   // Turn on red
  } else {
    digitalWrite(redPin, LOW);    // Turn off red
  }
  
  if (digitalRead(buttonGreen) == HIGH) {
    digitalWrite(greenPin, HIGH); // Turn on green
  } else {
    digitalWrite(greenPin, LOW);  // Turn off green
  }
  
  if (digitalRead(buttonBlue) == HIGH) {
    digitalWrite(bluePin, HIGH);  // Turn on blue
  } else {
    digitalWrite(bluePin, LOW);   // Turn off blue
  }
}
