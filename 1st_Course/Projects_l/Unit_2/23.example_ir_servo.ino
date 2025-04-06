#include <IRremote.h>
#include <Servo.h>

const int recv_pin = 11;
IRrecv irrecv(recv_pin);
decode_results results;
Servo myServo;

void setup() {
  myServo.attach(9);  // Attach servo to pin 9
  Serial.begin(9600);
  irrecv.enableIRIn();  // Start the receiver
}

void loop() {
  if (irrecv.decode(&results)) {
    long int decCode = results.value;
    Serial.println(decCode, DEC);  // Print the IR code for debugging

    // Check the IR code and set servo position
    if (decCode == 0xFF18E7) {  // Button 1 on the remote
      myServo.write(0);  // Move servo to 0 degrees
    } else if (decCode == 0xFF4AB5) {  // Button 2 on the remote
      myServo.write(45);  // Move servo to 45 degrees
    } else if (decCode == 0xFF10EF) {  // Button 3 on the remote
      myServo.write(90);  // Move servo to 90 degrees
    } else if (decCode == 0xFF5AA5) {  // Button 4 on the remote
      myServo.write(135);  // Move servo to 135 degrees
    } else if (decCode == 0xFF42BD) {  // Button 5 on the remote
      myServo.write(180);  // Move servo to 180 degrees
    }
    
    irrecv.resume();  // Receive the next value
  }
}
