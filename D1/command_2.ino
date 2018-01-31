//22.01.2018

/*
 Signal to respond to : the sample testing has completed 
 
 This program will let the actuator pushes the rod from the test holder to the conveyor belt,
 then retracts back all the way to the original position. 
 
 This program drives a unipolar or bipolar stepper motor.
 The motor is attached to digital pins 8 - 11 of the Arduino.

 The motor should revolve such that the actuator moves 8cm away from the housing and 20cm back.
 The motor then stops. 

 */

#include <Stepper.h>

const int stepsPerRevolution = 1500;  // change this to fit the number of steps per revolution

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 10, 9, 11);

void setup() {
  // set the speed at 10 rpm:
  myStepper.setSpeed(10);
  // initialize the serial port:
  Serial.begin(9600);
}

void loop() {
  // 8cm forward then 20cm backward

  myStepper.step(800);
  myStepper.step(-2000);
  exit(0);
}
