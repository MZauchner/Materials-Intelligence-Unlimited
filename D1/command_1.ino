//22.01.2018

/*
 Signal to respond to: new rod ready to be released
 
 This program will let the actuator pushes the rod from the silo release
 to the sample tester, then retracts a little bit so as not to touch the rod during testing.
 
 This program drives a unipolar or bipolar stepper motor.
 The motor is attached to digital pins 8 - 11 of the Arduino.

 The motor should revolve such that the actuator moves 13cm away from the housing and 1cm back.
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
  // 13cm forward then 1cm backward

  myStepper.step(1300);
  myStepper.step(-100);
  exit(0);
}

