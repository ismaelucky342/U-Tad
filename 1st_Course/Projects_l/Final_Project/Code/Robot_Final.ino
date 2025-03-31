#include <IRremote.h>           // Librería para el control remoto IR
#include <Servo.h>              // Librería para controlar el servomotor
#include <LiquidCrystal.h>      // Librería para controlar la pantalla LCD

// Definición de pines para los componentes
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

int motor_speed = 80;           // Velocidad de los motores

// Códigos para los comandos del control remoto
const long forward_cmd = 16613503;
const long backward_cmd = 16617583;
const long right_cmd = 16605343;
const long left_cmd = 16589023;
const long stop_cmd = 16580863;
const long option1_cmd = 16582903;
const long option2_cmd = 16615543;
const long option3_cmd = 16599223;

// Declaración de objetos para controlar los componentes
IRrecv ir_receiver(IR_pin);
decode_results ir_results;
Servo servo_motor;
LiquidCrystal lcd(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7);

// Variables de control de los modos de operación del robot
bool manual_control = false;
bool obstacle_detection = false;
bool line_following = false;

void setup() {
  Serial.begin(9600);
  ir_receiver.enableIRIn();         // Iniciar la recepción de señales del control remoto
  servo_motor.attach(servo_pulse);  // Iniciar el servomotor
  servo_motor.write(90);            // Posicionar el servomotor en ángulo medio
  lcd.begin(16, 2);                  // Iniciar la pantalla LCD

  // Configuración de pines para motores, sensor ultrasónico y sensores de línea
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

// Función para medir la distancia con el sensor ultrasónico
int getDistance() {
  digitalWrite(trigger_pin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigger_pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger_pin, LOW);
  long duration = pulseIn(echo_pin, HIGH);
  return duration * 0.034 / 2;
}

// Función para mover el robot hacia adelante
void moveForward() {
  // Activar los motores para mover hacia adelante
  analogWrite(Enable_motor_left, motor_speed);
  analogWrite(Enable_motor_right, motor_speed);
  // Configurar dirección de los motores
  digitalWrite(motor_left_A, HIGH);
  digitalWrite(motor_left_B, LOW);
  digitalWrite(motor_right_A, LOW);
  digitalWrite(motor_right_B, HIGH);

  // Activar los segundos motores para mover hacia adelante (si es necesario)
  analogWrite(Enable_motor_left_2, motor_speed);
  analogWrite(Enable_motor_right_2, motor_speed);
  // Configurar dirección de los segundos motores (si es necesario)
  digitalWrite(motor_left_2_A, HIGH);
  digitalWrite(motor_left_2_B, LOW);
  digitalWrite(motor_right_2_A, LOW);
  digitalWrite(motor_right_2_B, HIGH);
}

// Función para mover el robot hacia atrás
void moveBackward() {
  // Activar los motores para mover hacia atrás
  analogWrite(Enable_motor_left, motor_speed);
  analogWrite(Enable_motor_right, motor_speed);
  // Configurar dirección de los motores para mover hacia atrás
  digitalWrite(motor_left_A, LOW);
  digitalWrite(motor_left_B, HIGH);
  digitalWrite(motor_right_A, HIGH);
  digitalWrite(motor_right_B, LOW);

  // Activar los segundos motores para mover hacia atrás (si es necesario)
  analogWrite(Enable_motor_left_2, motor_speed);
  analogWrite(Enable_motor_right_2, motor_speed);
  // Configurar dirección de los segundos motores para mover hacia atrás (si es necesario)
  digitalWrite(motor_left_2_A, LOW);
  digitalWrite(motor_left_2_B, HIGH);
  digitalWrite(motor_right_2_A, HIGH);
  digitalWrite(motor_right_2_B, LOW);
}

// Función para girar el robot hacia la izquierda
void turnLeft() {
  // Activar los motores para permitir el giro hacia la izquierda
  analogWrite(Enable_motor_left, motor_speed);
  analogWrite(Enable_motor_right, motor_speed);
  // Configurar dirección de los motores para girar hacia la izquierda
  digitalWrite(motor_left_A, LOW);
  digitalWrite(motor_left_B, HIGH);
  digitalWrite(motor_right_A, LOW);
  digitalWrite(motor_right_B, HIGH);

  // Activar los segundos motores para permitir el giro hacia la izquierda (si es necesario)
  analogWrite(Enable_motor_left_2, motor_speed);
  analogWrite(Enable_motor_right_2, motor_speed);
  // Configurar dirección de los segundos motores para girar hacia la izquierda (si es necesario)
  digitalWrite(motor_left_2_A, LOW);
  digitalWrite(motor_left_2_B, HIGH);
  digitalWrite(motor_right_2_A, LOW);
  digitalWrite(motor_right_2_B, HIGH);
}
// Función para girar el robot hacia la derecha
void turnRight() {
  // Activar los motores para permitir el giro hacia la derecha
  analogWrite(Enable_motor_left, motor_speed);
  analogWrite(Enable_motor_right, motor_speed);
  // Configurar dirección de los motores para girar hacia la derecha
  digitalWrite(motor_left_A, HIGH);
  digitalWrite(motor_left_B, LOW);
  digitalWrite(motor_right_A, HIGH);
  digitalWrite(motor_right_B, LOW);

  // Activar los segundos motores para permitir el giro hacia la derecha (si es necesario)
  analogWrite(Enable_motor_left_2, motor_speed);
  analogWrite(Enable_motor_right_2, motor_speed);
  // Configurar dirección de los segundos motores para girar hacia la derecha (si es necesario)
  digitalWrite(motor_left_2_A, HIGH);
  digitalWrite(motor_left_2_B, LOW);
  digitalWrite(motor_right_2_A, HIGH);
  digitalWrite(motor_right_2_B, LOW);
}


void stopMotors() //parar motores
{
  digitalWrite(Enable_motor_left, LOW);
  digitalWrite(Enable_motor_right, LOW);
  digitalWrite(Enable_motor_left_2, LOW);
  digitalWrite(Enable_motor_right_2, LOW);
}

int lookRight() //servo con sensor mira izquierda y calcula distancia
{
  servo_motor.write(50);
  delay(500);
  int distance = getDistance();
  delay(100);
  servo_motor.write(115);
  return distance;
}

int lookLeft()//servo con sensor mira derecha y calcula distancia
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
  // Verifica si se ha recibido una señal IR
  if (ir_receiver.decode(&ir_results))
  {
    // Verifica el comando recibido
    if (ir_results.value == option1_cmd)
    {
      // Modo manual: control directo del robot por el usuario
      manual_control = true;
      obstacle_detection = false; // Desactiva otros modos
      line_following = false;
      lcd.clear();
      lcd.print("Modo Manual");

      // Bucle de control manual
      while (manual_control)
      {
        // Verifica si se recibe un comando IR mientras se está en modo manual
        if (ir_receiver.decode(&ir_results))
        {
          // Ejecuta acciones según el comando IR recibido
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
            break; // Sal del bucle si se selecciona otro modo
          }
          ir_receiver.resume(); // Reanuda la recepción de señales IR
        }
      }
    }
    else if (ir_results.value == option2_cmd)
    {
      // Modo de evitación de obstáculos: el robot detecta y evita obstáculos
      manual_control = false; // Desactiva otros modos
      obstacle_detection = true;
      line_following = false;
      lcd.clear();
      lcd.print("Evitar Obstaculos");

      // Bucle de detección y evitación de obstáculos
      while (obstacle_detection)
      {
        int distance = getDistance(); // Obtiene la distancia a un obstáculo
        if (distance <= 30)
        {
          // Si hay un obstáculo cercano, el robot lo evita
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
          // Si no hay obstáculos cercanos, el robot avanza
          moveForward();
        }

        // Verifica si se recibe un comando IR para cambiar de modo
        if (ir_receiver.decode(&ir_results))
        {
          if (ir_results.value == option1_cmd || ir_results.value == option3_cmd)
          {
            break; // Sal del bucle si se selecciona otro modo
          }
          ir_receiver.resume(); // Reanuda la recepción de señales IR
        }
      }
    }
    else if (ir_results.value == option3_cmd)
    {
      // Modo de seguimiento de línea: el robot sigue una línea en el suelo
      manual_control = false; // Desactiva otros modos
      obstacle_detection = false;
      line_following = true;
      lcd.clear();
      lcd.print("Seguir Linea");

      // Bucle de seguimiento de línea
      while (line_following)
      {
        int sensor_value = analogRead(line_sensor); // Lee el valor del sensor de línea

        if (sensor_value >= 80)
        {
          moveForward(); // Avanza si la línea está debajo del sensor
        }
        else
        {
          // Si la línea no está debajo del sensor, el robot realiza una maniobra para recapturarla
          stopMotors();
          delay(100);
          turnRight(); // O turnLeft() dependiendo de tu configuración
          delay(300);
        }

        // Verifica si se recibe un comando IR para cambiar de modo
        if (ir_receiver.decode(&ir_results))
        {
          if (ir_results.value == option1_cmd || ir_results.value == option2_cmd)
          {
            break; // Sal del bucle si se selecciona otro modo
          }
          ir_receiver.resume(); // Reanuda la recepción de señales IR
        }
      }
    }
  }
}
