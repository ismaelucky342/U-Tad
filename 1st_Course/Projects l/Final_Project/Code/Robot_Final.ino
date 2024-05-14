#include <IRremote.h>
#include <Servo.h>

#define IR_pin 7

#define servo_pulse 13
#define trigger_pin 12
#define right_line_sensor A0
#define middle_line_sensor A1
#define left_line_sensor A2

#define Enable_motor_right 5
#define motor_right_A 6
#define motor_right_B 3
#define Enable_motor_left 9
#define motor_left_A 8
#define motor_left_B 10
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

bool manual_control = false;
bool obstacle_detection = false;
bool line_following = false;

void setup() {
  Serial.begin(9600);
  ir_receiver.enableIRIn();
  servo_motor.attach(servo_pulse);
  servo_motor.write(90);

  pinMode(motor_right_A, OUTPUT);
  pinMode(motor_right_B, OUTPUT);
  pinMode(motor_left_A, OUTPUT);
  pinMode(motor_left_B, OUTPUT);
  pinMode(trigger_pin, OUTPUT);

  pinMode(left_line_sensor, INPUT);
  pinMode(middle_line_sensor, INPUT);
  pinMode(right_line_sensor, INPUT);
}

int getDistance() {
  unsigned long pulse_duration = 0;
  pinMode(trigger_pin, OUTPUT);
  digitalWrite(trigger_pin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigger_pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger_pin, LOW);
  pinMode(trigger_pin, INPUT);
  pulse_duration = pulseIn(trigger_pin, HIGH);
  pulse_duration = pulse_duration / 2;
  int distance = int(pulse_duration / 29);
  delayMicroseconds(50);
  return distance;
}

void moveForward() {
  analogWrite(Enable_motor_left, motor_speed);
  analogWrite(Enable_motor_right, motor_speed);
  digitalWrite(motor_left_A, HIGH);
  digitalWrite(motor_left_B, LOW);
  digitalWrite(motor_right_A, LOW);
  digitalWrite(motor_right_B, HIGH);
}

void moveBackward() {
  analogWrite(Enable_motor_left, motor_speed);
  analogWrite(Enable_motor_right, motor_speed);
  digitalWrite(motor_left_A, LOW);
  digitalWrite(motor_left_B, HIGH);
  digitalWrite(motor_right_A, HIGH);
  digitalWrite(motor_right_B, LOW);
}

void turnLeft() {
  analogWrite(Enable_motor_left, motor_speed);
  analogWrite(Enable_motor_right, motor_speed);
  digitalWrite(motor_left_A, LOW);
  digitalWrite(motor_left_B, HIGH);
  digitalWrite(motor_right_A, LOW);
  digitalWrite(motor_right_B, HIGH);
}

void turnRight() {
  analogWrite(Enable_motor_left, motor_speed);
  analogWrite(Enable_motor_right, motor_speed);
  digitalWrite(motor_left_A, HIGH);
  digitalWrite(motor_left_B, LOW);
  digitalWrite(motor_right_A, HIGH);
  digitalWrite(motor_right_B, LOW);
}

void stopMotors() {
  digitalWrite(Enable_motor_left, LOW);
  digitalWrite(Enable_motor_right, LOW);
}

int lookRight() {
  servo_motor.write(50);
  delay(500);
  int distance = getDistance();
  delay(100);
  servo_motor.write(115);
  return distance;
}

int lookLeft() {
  servo_motor.write(170);
  delay(500);
  int distance = getDistance();
  delay(100);
  servo_motor.write(115);
  return distance;
}

void loop() {
  if (ir_receiver.decode(&ir_results)) {
    if (ir_results.value == option1_cmd) {
      manual_control = true;
      obstacle_detection = false;
      line_following = false;

      while (manual_control) {
        if (ir_receiver.decode(&ir_results)) {
          if (ir_results.value == forward_cmd) {
            moveForward();
          } else if (ir_results.value == backward_cmd) {
            moveBackward();
          } else if (ir_results.value == right_cmd) {
            turnRight();
          } else if (ir_results.value == left_cmd) {
            turnLeft();
          } else if (ir_results.value == stop_cmd) {
            stopMotors();
          } else if (ir_results.value == option2_cmd || ir_results.value == option3_cmd) {
            break;
          }
          ir_receiver.resume();
        }
      }
    } else if (ir_results.value == option2_cmd) {
      manual_control = false;
      obstacle_detection = true;
      line_following = false;

      while (obstacle_detection) {
        int distance = getDistance();
        if (distance <= 30) {
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

          if (distance_right >= distance_left) {
            turnRight();
            stopMotors();
          } else {
            turnLeft();
            stopMotors();
          }
        } else {
          moveForward();
        }

        if (ir_receiver.decode(&ir_results)) {
          if (ir_results.value == option1_cmd || ir_results.value == option3_cmd) {
            break;
          }
          ir_receiver.resume();
        }
      }
    } else if (ir_results.value == option3_cmd) {
      manual_control = false;
      obstacle_detection = false;
      line_following = true;

      while (line_following) {
        int right_sensor_value = analogRead(right_line_sensor);
        int middle_sensor_value = analogRead(middle_line_sensor);
        int left_sensor_value = analogRead(left_line_sensor);

        if (middle_sensor_value >= 80 && right_sensor_value >= 80) {
          turnLeft();
        } else if (middle_sensor_value >= 80 && left_sensor_value >= 80) {
          turnRight();
        } else if (middle_sensor_value >= 80) {
          moveForward();
        }

        if (ir_receiver.decode(&ir_results)) {
          if (ir_results.value == option1_cmd || ir_results.value == option2_cmd) {
            break;
          }
          ir_receiver.resume();
        }
      }
    }
  }
}
