#include <Adafruit_NeoPixel.h>

// Definiciones de pines
const int motorEnablePin = 9;
const int motorInputPin1 = 2;
const int motorInputPin2 = 3;
const int potPin = A0;
const int buttonPin = 4;
const int LED_PIN = 6;
const int LED_COUNT = 10;

bool motorState = false;
int buttonState;
int lastButtonState = LOW;
unsigned long lastDebounceTime = 0;
unsigned long debounceDelay = 50;

// Inicialización de la tira de LEDs
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  pinMode(motorEnablePin, OUTPUT);
  pinMode(motorInputPin1, OUTPUT);
  pinMode(motorInputPin2, OUTPUT);
  pinMode(buttonPin, INPUT);

  digitalWrite(motorEnablePin, LOW);
  Serial.begin(9600);

  strip.begin();
  strip.show(); // Inicializa todos los LEDs apagados
}

void loop() {
  int reading = digitalRead(buttonPin);

  // Manejo del debounce del botón
  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading != buttonState) {
      buttonState = reading;
      if (buttonState == HIGH) {
        motorState = !motorState; // Alterna el estado del motor
      }
    }
  }

  if (motorState) {
    int potValue = analogRead(potPin);
    int speed = map(potValue, 0, 1023, -255, 255); // Mapea el valor del potenciómetro a -255 a 255
    int numLEDs = map(abs(speed), 0, 255, 0, LED_COUNT); // Mapea la velocidad a la cantidad de LEDs

    // Actualiza los LEDs según la velocidad y el sentido de giro
    for (int i = 0; i < LED_COUNT; i++) {
      if (i < numLEDs) {
        if (speed > 0) {
          strip.setPixelColor(i, strip.Color(0, 255, 0)); // Verde
        } else {
          strip.setPixelColor(i, strip.Color(255, 0, 0)); // Rojo
        }
      } else {
        strip.setPixelColor(i, strip.Color(0, 0, 0)); // Apagado
      }
    }
    strip.show();

    // Control del motor
    if (speed > 0) {
      digitalWrite(motorInputPin1, HIGH);
      digitalWrite(motorInputPin2, LOW);
      analogWrite(motorEnablePin, speed);
    } else if (speed < 0) {
      digitalWrite(motorInputPin1, LOW);
      digitalWrite(motorInputPin2, HIGH);
      analogWrite(motorEnablePin, -speed);
    } else {
      analogWrite(motorEnablePin, 0);
    }
  } else {
    analogWrite(motorEnablePin, 0);
    for (int i = 0; i < LED_COUNT; i++) {
      strip.setPixelColor(i, strip.Color(0, 0, 0)); // Apaga todos los LEDs
    }
    strip.show();
  }

  lastButtonState = reading;
}
