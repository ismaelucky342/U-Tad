int TRIG = 10; 
int ECO = 9; 
int LED = 3; 
int TIME;
int DISTANCE; 

void setup() {
  pinMode(TRIG, OUTPUT);
  pinMode(ECO, INPUT);
  pinMode(LED, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  digitalWrite(TRIG, HIGH);
  delay(1);
  digitalWrite(TRIG, LOW);
  TIME = pulseIn(ECO, HIGH);
  DISTANCE = TIME / 58.2; //sensor recomended time 
  Serial.println(DISTANCE); //distance cm in new line 
  delay(200);
}
