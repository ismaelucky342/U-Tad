#define trigPin 9
#define echoPin 10
#define motorPin 6

long duration;
int distance;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(motorPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Send a pulse to the ultrasonic sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Read the duration of the pulse
  duration = pulseIn(echoPin, HIGH);
  
  // Calculate the distance (in cm)
  distance = duration * 0.034 / 2;
  
  // Display the distance on the serial monitor
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  
  // Control the motor based on distance
  if (distance < 20) {
    digitalWrite(motorPin, HIGH);  // Motor ON if object is closer than 20 cm
  } else {
    digitalWrite(motorPin, LOW);   // Motor OFF if object is farther than 20 cm
  }

  delay(500);
}
