#include <IRremote.h>

const int recv_pin = 11;
IRrecv irrecv(recv_pin);
decode_results results;

void setup() {
  Serial.begin(9600);
  irrecv.enableIRIn();
}

void loop() {
  if (irrecv.decode(&results)) {
    long int decCode = results.value;
    Serial.println(decCode, DEC);
    irrecv.resume();  // Receive the next value
  }
}
