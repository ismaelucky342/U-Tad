int  BUTTON = 2; 
int  LED = 3; 
int  STATUS = LOW; 

void  setup()
{
  pinMode(BUTTON, INPUT);
  pinMode(LED, OUTPUT);
}

void  loop()
{
  while(digitalRead(BUTTON) == LOW){
    //empty
  }
  STATUS = digitalRead(LED);
  digitalWrite(LED, !STATUS); //OFF
  while (digitalRead(BUTTON) == HIGH){

  }
}