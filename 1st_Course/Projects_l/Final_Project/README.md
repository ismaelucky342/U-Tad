# Projects l - Final Project

## Overview

This project represents my final project in robotics. It features a robot with multiple operation modes: manual control, obstacle avoidance, and line-following. Controlled via an infrared (IR) remote, the robot is equipped with various sensors to navigate its environment, follow a line on the ground, and avoid obstacles. The project uses an Arduino board, which is connected to a range of components such as motors, sensors, an LCD, and a servo for steering.

The robot system is versatile and can be extended with additional features, making it a great platform for experimenting with robotics and sensor integration. The robot has been printed using an **Anycubic i3 Mega** 3D printer, and the files used for printing are available in a specific folder on my project.

## Components

1. **IR Remote Control**: The robot receives commands from an IR remote for controlling its movement in different modes.
2. **Servo Motor**: Responsible for steering and scanning for obstacles.
3. **Ultrasonic Sensor**: Measures the distance to objects in front of the robot, used for obstacle avoidance.
4. **Motors**: Control the movement of the robot, enabling forward, backward, left, and right motions.
5. **Line Sensor**: Detects lines on the ground for enabling the line-following mode.
6. **LCD**: Displays the current mode of the robot and provides status feedback.
7. **LEDs**: Show visual feedback on the robot's status (e.g., in manual mode or obstacle avoidance mode).

## Wiring

- **IR Receiver**: Pin 7
- **Ultrasonic Sensor**:
    - Trigger Pin: 12
    - Echo Pin: 11
- **Line Sensor**: Analog Pin A0
- **Motor Driver Pins**:
    - Motor Right: Pins 6, 5, 3
    - Motor Left: Pins 8, 9, 10
    - Motor Right 2: Pins 4, 2
    - Motor Left 2: Pins 13, 14
- **Servo Motor**: Pin 13
- **LCD**: Pins 2, 3, 4, 5, 6, 7

## Modes of Operation

### 1. **Manual Control Mode**

- **IR Commands**:
    - **Forward**: Move the robot forward.
    - **Backward**: Move the robot backward.
    - **Left**: Turn the robot left.
    - **Right**: Turn the robot right.
    - **Stop**: Stop all movement.

In this mode, the LCD displays **"Modo Manual"**.

### 2. **Obstacle Avoidance Mode**

- The robot detects obstacles using the ultrasonic sensor. If an obstacle is detected (distance ≤ 30 cm), the robot stops, moves backward, and then turns based on the detected obstacle's location (left or right). If no obstacle is detected, it continues moving forward.

In this mode, the LCD displays **"Evitar Obstaculos"**.

### 3. **Line Following Mode**

- The robot follows a line on the ground using the line sensor. If the line is detected, the robot moves forward. If the line is lost, the robot will turn to find the line again.

In this mode, the LCD displays **"Seguir Linea"**.

## Functions

### `getDistance()`

- Measures the distance to an object using the ultrasonic sensor.

### `moveForward()`, `moveBackward()`, `turnLeft()`, `turnRight()`

- Functions to control the movement of the robot in different directions.

### `stopMotors()`

- Stops the robot's motors.

### `lookRight()`, `lookLeft()`

- Functions to control the servo and scan for obstacles on the robot's right and left sides.

### `setup()`

- Initializes the robot's components, including the IR receiver, motors, ultrasonic sensor, LCD, and servo.

### `loop()`

- The main control loop that checks for IR commands and handles the robot's operation modes.

## IR Remote Commands

- **Forward**: Moves the robot forward.
- **Backward**: Moves the robot backward.
- **Right**: Turns the robot right.
- **Left**: Turns the robot left.
- **Stop**: Stops the robot's movement.
- **Option 1**: Switches to manual control mode.
- **Option 2**: Switches to obstacle avoidance mode.
- **Option 3**: Switches to line-following mode.

## Libraries Used

1. **IRremote**: Library for IR communication.
2. **Servo**: Library for controlling the servo motor.
3. **LiquidCrystal**: Library for controlling the LCD screen.

## Extras

This robot has been designed to demonstrate core functionalities in robotics, such as manual control, obstacle avoidance, and line-following. The integration of sensors with an IR remote control creates an interactive system that is easy to expand with additional features. Furthermore, the robot is equipped with feedback systems like the LCD and LEDs to provide real-time status updates.

It was a more than exciting final project!

![image](https://github.com/ismaelucky342/U-Tad/assets/153450550/62bc16fd-1d63-401e-962d-b090cad59bdc)