#include <IRremote.h>
#include <Servo.h>

#define IR_pin 7

#define servo_pulse 13
#define triger 12
#define R A0
#define M A1
#define L A2

#define Enable_motor_right 5     
#define motor_right_A 6         
#define motor_right_B 3         
#define Enable_motor_left 9 
#define motor_left_A 8     
#define motor_left_B 10 
int motor_speed = 80;

const long forward = 16613503;      // button codes
const long backward = 16617583;
const long right = 16605343;
const long left = 16589023;
const long stop = 16580863;
const long option1 = 16582903;
const long option2 = 16615543;
const long option3 = 16599223;

IRrecv re(IR_pin); 
decode_results results; // declare code results

int distance =100;
Servo myservo;

bool control = false;
bool sensor = false;
bool line = false;

void setup()
{
  Serial.begin(9600);
  re.enableIRIn(); // initialize signal reception
  myservo.attach(13);
  myservo.write(90);
  
  pinMode(motor_right_A, OUTPUT);
  pinMode(motor_right_B, OUTPUT);
  pinMode(motor_left_A, OUTPUT);
  pinMode(motor_left_B, OUTPUT);
  pinMode(servo_pulse, OUTPUT);
  pinMode(triger, OUTPUT);
  
  pinMode(L, INPUT);
  pinMode(M, INPUT);
  pinMode(R, INPUT);
  
}


// returns distance from Ping))) sensor in cm
int getDistance(){
  
  int distance;
  unsigned long pulseduration = 0;
  // get the raw measurement data from Ping)))
  // set pin as output so we can send a pulse
  pinMode(triger, OUTPUT);
  digitalWrite(triger, LOW);
  delayMicroseconds(5);
  digitalWrite(triger, HIGH);         // send the 5uS pulse out to activate Ping)))
  delayMicroseconds(10);
  digitalWrite(triger, LOW);
  pinMode(triger, INPUT);             // change the digital pin to input to read the incoming pulse
  pulseduration = pulseIn(triger, HIGH);// measure the length of the incoming pulse  
  pulseduration = pulseduration/2;      // divide the pulse length in half
  distance = int(pulseduration/29);
  delayMicroseconds(50);
  
  return distance;
}


void forward()//vol+ -> forward
{
  analogWrite(Enable_motor_left, motor_speed);
  analogWrite(Enable_motor_right, motor_speed);
  
  digitalWrite(motor_left_A, HIGH);
  digitalWrite(motor_left_B, LOW);
  digitalWrite(motor_right_A, LOW);
  digitalWrite(motor_right_B, HIGH);
}

void backward()//vol- -> backward
{
  analogWrite(Enable_motor_left, motor_speed);
  analogWrite(Enable_motor_right, motor_speed);
  
  digitalWrite(motor_left_A, LOW);
  digitalWrite(motor_left_B, HIGH);
  digitalWrite(motor_right_A, HIGH);
  digitalWrite(motor_right_B, LOW);
}

void left()// >> -> left
{
  analogWrite(Enable_motor_left, motor_speed);
  analogWrite(Enable_motor_right, motor_speed);
  
  digitalWrite(motor_left_A, LOW);
  digitalWrite(motor_left_B, HIGH);
  digitalWrite(motor_right_A, LOW);
  digitalWrite(motor_right_B, HIGH);
}

void right()// << -> right
{
  analogWrite(Enable_motor_left, motor_speed);
  analogWrite(Enable_motor_right, motor_speed);
  
  digitalWrite(motor_left_A, HIGH);
  digitalWrite(motor_left_B, LOW);
  digitalWrite(motor_right_A, HIGH);
  digitalWrite(motor_right_B, LOW);
}

void stop()// stop
{
  digitalWrite(Enable_motor_left, LOW);
  digitalWrite(Enable_motor_right, LOW);
}

int lookRight(){
  
    myservo.write(50); 
    delay(500);
    int distance = getDistance();
    delay(100);
    myservo.write(115);
    return distance;
}

int lookLeft(){
  
    myservo.write(170); 
    delay(500);
    int distance = getDistance();
    delay(100);
    myservo.write(115);
    return distance;
    
}

void loop(){
  if(re.decode(&results)){//if any code is received
    if(results.value == option1){
      bool control = true;
      bool sensor = false;
      bool line = false;

      while(control == true){
        if(re.decode(&results)){
          if(results.value == forward){
            forward();
          }
          else if(results.value == backward){
            backward();
          }
          else if(results.value == right){
            right();
          }
          else if(results.value == left){
            left();
          }
          else if(results.value == stop){
            stop();
          }
          else if(results.value == option2 || results.value == option3 ){
            break;
          }
          re.resume();
        }
      }
    }else if(results.value == option2){
      bool control = false;
      bool sensor = true;
      bool line = false;
      while(sensor == true){
        int distanceR = 0;
        int distanceL =  0;
        delay(100);
        if(distance<=30){
          stop();
          delay(100);
          backward();
          delay(300);
          stop();
          delay(200);
          distanceR = lookRight();
          delay(200);
          distanceL = lookLeft();
          delay(200);
        
            if(distanceR >= distanceL){
              right();
              stop();
            }
            else{
              left();
              stop();
            }
        }else{
          forward();
        }
        
        distance = getDistance();
        
        if(re.decode(&results)){
          if(results.value == option1 || results.value == option3 ){
            break;
          }
          re.resume(); 
        }
      }
    }else if(results.value == option3){
        bool control = false;
        bool sensor = false;
        bool line = true;
        while(line == true){
            int FD = analogRead(R);
            int Meio = analogRead(M);
            int FE = analogRead(L);
          
            if(Meio >= 80 && FD >= 80){
              left();
            }

            else if(Meio >= 80 && FE >= 80){
              right();
            }

            else if(Meio >= 80){
              forward();
            }
          
            if(re.decode(&results)){
              if(results.value == option1 || results.value == option2 ){
                break;
              }
            re.resume(); 
          } 
        } 
  }
}
}
