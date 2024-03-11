int LED = 3; 
int B; 

void setup() {
  pinMode(LED, OUTPUT);
}

void loop() {
  for (B = 0; B < 256; B++){
    analogWrite(LED, B);
    delay(15);
  }
  for (B = 255; B > 0; B--){
    analogWrite(LED, B);
    delay(15);
  }
}
