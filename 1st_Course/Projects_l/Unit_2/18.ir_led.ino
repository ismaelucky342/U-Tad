#include <IRremote.h>

const int ledPin = 13;
const int recv_pin = 11;
IRrecv irrecv(recv_pin);
decode_results results;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  irrecv.enableIRIn();
}

void loop() {
  if (irrecv.decode(&results)) {
    long int decCode = results.value;
    Serial.println(decCode, DEC);
    
    if (decCode == 0xFF18E7) {  // Example button code to turn on LED
      digitalWrite(ledPin, HIGH);
    }
    if (decCode == 0xFF4AB5) {  // Example button code to turn off LED
      digitalWrite(ledPin, LOW);
    }
    
    irrecv.resume();
  }
}
