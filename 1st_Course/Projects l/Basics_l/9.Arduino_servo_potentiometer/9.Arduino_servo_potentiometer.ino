#include <Servo.h>

Servo servo1; 

int PINSERVO = 2; 
int PULSEMIN = 700; 
int PULSEMAX = 2350; 
int POTVALUE; 
int ANGLE; 
int POT = 0; 

void setup() {
  servo1.attach(PINSERVO, PULSEMIN, PULSEMAX);

}

void loop() {
  POTVALUE = analogRead(POT); 
  ANGLE = map(POTVALUE, 0, 1023, 0, 180);
  servo1.write(ANGLE);
  delay(20);
}


