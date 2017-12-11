//2017.11.28

/*
 Stepper Motor Control - manual steps control with Serial Monitor input

 This program drives a unipolar or bipolar stepper motor.
 The motor is attached to digital pins 8 - 11 of the Arduino.

 The motor should revolve depending on the number put in Serial Monitor Command. 
 Positive number for clockwise and negative number for anti-clockwise. 

 Begin by clicking on Serial Monitor button. 

 */

#include <Stepper.h>

const int stepsPerRevolution = 1600;  // change this to fit the number of steps per revolution

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 10, 9, 11);

void setup() {
  // set the speed at 20 rpm:
  myStepper.setSpeed(24);
  // initialize the serial port:
  Serial.begin(9600);
  Serial.println("Enter steps per revolution or 'x' to clear");
}

void loop() {
  // step one revolution  in one direction:
 if (Serial.available())
  {
    int steps = Serial.parseInt();
    myStepper.step(steps);
}
}

