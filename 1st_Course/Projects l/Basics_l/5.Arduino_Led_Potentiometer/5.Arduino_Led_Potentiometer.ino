int LED = 3; 
int B; 
int POT = 0; 


void setup() {
  pinMode(LED, OUTPUT);
  //digital inputs do not require initialization
}

void loop() {
  B = analogRead(POT) / 4;
  analogWrite(LED, B);


}
