#include <IRremote.h>

const int motorPin = 9;
const int recv_pin = 11;
IRrecv irrecv(recv_pin);
decode_results results;

void setup() {
  pinMode(motorPin, OUTPUT);
  Serial.begin(9600);
  irrecv.enableIRIn();
}

void loop() {
  if (irrecv.decode(&results)) {
    long int decCode = results.value;
    Serial.println(decCode, DEC);

    if (decCode == 0xFF18E7) {  // Example remote button code
      digitalWrite(motorPin, HIGH);  // Turn motor on
    }
    if (decCode == 0xFF4AB5) {  // Another example remote button code
      digitalWrite(motorPin, LOW);   // Turn motor off
    }
    
    irrecv.resume();  // Receive the next value
  }
}
