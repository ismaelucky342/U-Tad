#include <IRremote.h>
#include <Servo.h>
#include <LiquidCrystal.h>

#define IR_pin 7
#define trigger_pin 12
#define echo_pin 11
#define line_sensor A0

#define Enable_motor_right 5
#define motor_right_A 6
#define motor_right_B 3
#define Enable_motor_left 9
#define motor_left_A 8
#define motor_left_B 10

#define Enable_motor_right_2 11
#define motor_right_2_A 4
#define motor_right_2_B 2
#define Enable_motor_left_2 12
#define motor_left_2_A 13
#define motor_left_2_B 14

#define servo_pulse 13

#define lcd_rs 2
#define lcd_en 3
#define lcd_d4 4
#define lcd_d5 5
#define lcd_d6 6
#define lcd_d7 7

const int led1 = 8;
const int led2 = 9;

int motor_speed = 80;

const long forward_cmd = 16613503;
const long backward_cmd = 16617583;
const long right_cmd = 16605343;
const long left_cmd = 16589023;
const long stop_cmd = 16580863;
const long option1_cmd = 16582903;
const long option2_cmd = 16615543;
const long option3_cmd = 16599223;

IRrecv ir_receiver(IR_pin);
decode_results ir_results;

Servo servo_motor;
LiquidCrystal lcd(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7);

bool manual_control = false;
bool obstacle_detection = false;
bool line_following = false;

void setup()
{
  Serial.begin(9600);
  ir_receiver.enableIRIn();
  servo_motor.attach(servo_pulse);
  servo_motor.write(90);
  lcd.begin(16, 2);

  pinMode(motor_right_A, OUTPUT);
  pinMode(motor_right_B, OUTPUT);
  pinMode(motor_left_A, OUTPUT);
  pinMode(motor_left_B, OUTPUT);
  pinMode(trigger_pin, OUTPUT);
  pinMode(echo_pin, INPUT);

  pinMode(line_sensor, INPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);

  pinMode(motor_right_2_A, OUTPUT);
  pinMode(motor_right_2_B, OUTPUT);
  pinMode(motor_left_2_A, OUTPUT);
  pinMode(motor_left_2_B, OUTPUT);
}

int getDistance()
{
  digitalWrite(trigger_pin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigger_pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger_pin, LOW);
  long duration = pulseIn(echo_pin, HIGH);
  return duration * 0.034 / 2;
}

void moveForward()
{
  analogWrite(Enable_motor_left, motor_speed);
  analogWrite(Enable_motor_right, motor_speed);
  digitalWrite(motor_left_A, HIGH);
  digitalWrite(motor_left_B, LOW);
  digitalWrite(motor_right_A, LOW);
  digitalWrite(motor_right_B, HIGH);

  analogWrite(Enable_motor_left_2, motor_speed);
  analogWrite(Enable_motor_right_2, motor_speed);
  digitalWrite(motor_left_2_A, HIGH);
  digitalWrite(motor_left_2_B, LOW);
  digitalWrite(motor_right_2_A, LOW);
  digitalWrite(motor_right_2_B, HIGH);
}

void moveBackward()
{
  analogWrite(Enable_motor_left, motor_speed);
  analogWrite(Enable_motor_right, motor_speed);
  digitalWrite(motor_left_A, LOW);
  digitalWrite(motor_left_B, HIGH);
  digitalWrite(motor_right_A, HIGH);
  digitalWrite(motor_right_B, LOW);

  analogWrite(Enable_motor_left_2, motor_speed);
  analogWrite(Enable_motor_right_2, motor_speed);
  digitalWrite(motor_left_2_A, LOW);
  digitalWrite(motor_left_2_B, HIGH);
  digitalWrite(motor_right_2_A, HIGH);
  digitalWrite(motor_right_2_B, LOW);
}

void turnLeft()
{
  analogWrite(Enable_motor_left, motor_speed);
  analogWrite(Enable_motor_right, motor_speed);
  digitalWrite(motor_left_A, LOW);
  digitalWrite(motor_left_B, HIGH);
  digitalWrite(motor_right_A, LOW);
  digitalWrite(motor_right_B, HIGH);

  analogWrite(Enable_motor_left_2, motor_speed);
  analogWrite(Enable_motor_right_2, motor_speed);
  digitalWrite(motor_left_2_A, LOW);
  digitalWrite(motor_left_2_B, HIGH);
  digitalWrite(motor_right_2_A, LOW);
  digitalWrite(motor_right_2_B, HIGH);
}

void turnRight()
{
  analogWrite(Enable_motor_left, motor_speed);
  analogWrite(Enable_motor_right, motor_speed);
  digitalWrite(motor_left_A, HIGH);
  digitalWrite(motor_left_B, LOW);
  digitalWrite(motor_right_A, HIGH);
  digitalWrite(motor_right_B, LOW);

  analogWrite(Enable_motor_left_2, motor_speed);
  analogWrite(Enable_motor_right_2, motor_speed);
  digitalWrite(motor_left_2_A, HIGH);
  digitalWrite(motor_left_2_B, LOW);
  digitalWrite(motor_right_2_A, HIGH);
  digitalWrite(motor_right_2_B, LOW);
}

void stopMotors()
{
  digitalWrite(Enable_motor_left, LOW);
  digitalWrite(Enable_motor_right, LOW);
  digitalWrite(Enable_motor_left_2, LOW);
  digitalWrite(Enable_motor_right_2, LOW);
}

int lookRight()
{
  servo_motor.write(50);
  delay(500);
  int distance = getDistance();
  delay(100);
  servo_motor.write(115);
  return distance;
}

int lookLeft()
{
  servo_motor.write(170);
  delay(500);
  int distance = getDistance();
  delay(100);
  servo_motor.write(115);
  return distance;
}

void loop()
{
  if (ir_receiver.decode(&ir_results))
  {
    if (ir_results.value == option1_cmd)
    {
      manual_control = true;
      obstacle_detection = false;
      line_following = false;
      lcd.clear();
      lcd.print("Modo Manual");

      while (manual_control)
      {
        if (ir_receiver.decode(&ir_results))
        {
          if (ir_results.value == forward_cmd)
          {
            moveForward();
            lcd.setCursor(0, 1);
            lcd.print("Adelante  ");
          }
          else if (ir_results.value == backward_cmd)
          {
            moveBackward();
            lcd.setCursor(0, 1);
            lcd.print("Atras     ");
          }
          else if (ir_results.value == right_cmd)
          {
            turnRight();
            lcd.setCursor(0, 1);
            lcd.print("Derecha   ");
          }
          else if (ir_results.value == left_cmd)
          {
            turnLeft();
            lcd.setCursor(0, 1);
            lcd.print("Izquierda ");
          }
          else if (ir_results.value == stop_cmd)
          {
            stopMotors();
            lcd.setCursor(0, 1);
            lcd.print("Detenido  ");
          }
          else if (ir_results.value == option2_cmd || ir_results.value == option3_cmd)
          {
            break;
          }
          ir_receiver.resume();
        }
      }
    }
    else if (ir_results.value == option2_cmd)
    {
      manual_control = false;
      obstacle_detection = true;
      line_following = false;
      lcd.clear();
      lcd.print("Evitar Obstaculos");

      while (obstacle_detection)
      {
        int distance = getDistance();
        if (distance <= 30)
        {
          stopMotors();
          delay(100);
          moveBackward();
          delay(300);
          stopMotors();
          delay(200);
          int distance_right = lookRight();
          delay(200);
          int distance_left = lookLeft();
          delay(200);

          if (distance_right >= distance_left)
          {
            turnRight();
            stopMotors();
          }
          else
          {
            turnLeft();
            stopMotors();
          }
        }
        else
        {
          moveForward();
        }

        if (ir_receiver.decode(&ir_results))
        {
          if (ir_results.value == option1_cmd || ir_results.value == option3_cmd)
          {
            break;
          }
          ir_receiver.resume();
        }
      }
    }
    else if (ir_results.value == option3_cmd)
    {
      manual_control = false;
      obstacle_detection = false;
      line_following = true;
      lcd.clear();
      lcd.print("Seguir Linea");

      while (line_following)
      {
        int sensor_value = analogRead(line_sensor);

        if (sensor_value >= 80)
        {
          moveForward();
        }
        else
        {
          stopMotors();
          delay(100);
          turnRight(); // O turnLeft() dependiendo de tu configuración
          delay(300);
        }

        if (ir_receiver.decode(&ir_results))
        {
          if (ir_results.value == option1_cmd || ir_results.value == option2_cmd)
          {
            break;
          }
          ir_receiver.resume();
        }
      }
    }
  }
}
