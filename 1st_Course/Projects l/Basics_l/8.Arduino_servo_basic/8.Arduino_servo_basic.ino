#include <Servo.h>

Servo servo1; 

int PINSERVO = 2; 
int PULSEMIN = 1000; 
int PULSEMAX = 2000; 

void setup() {
  servo1.attach(PINSERVO, PULSEMIN, PULSEMAX);

}

void loop() {
  servo1.write(0);
  delay(2000);
  servo1.write(360);
  delay(2000);
}
