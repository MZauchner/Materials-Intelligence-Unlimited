/* 
This is a test sketch for the Adafruit assembled Motor Shield for Arduino v2
It won't work with v1.x motor shields! Only for the v2's with built in PWM
control

For use with the Adafruit Motor Shield v2 
---->	http://www.adafruit.com/products/1438
*/


#include <Wire.h>
#include <Adafruit_MotorShield.h>

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
// Or, create it with a different I2C address (say for stacking)
// Adafruit_MotorShield AFMS = Adafruit_MotorShield(0x61); 

// Connect a stepper motor with 200 steps per revolution (1.8 degree)
// to motor port #2 (M3 and M4)
Adafruit_StepperMotor *myMotor = AFMS.getStepper(200, 2);


void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("start");

  AFMS.begin();  // create with the default frequency 1.6KHz
  
  myMotor->setSpeed(10);  // 10 rpm   
}

void loop() {

  String replay;
  replay = Serial.readString();
  
  
  if ( replay == "rotate"){
  myMotor->step(200, FORWARD, MICROSTEP); 
  Serial.println("rotate 360 degrees");
  replay = "stop";
  }

  if(replay == "forward"){
   myMotor->step(20, FORWARD, MICROSTEP); 
  Serial.println("forward 36 degrees");
  replay = "stop";
  }

  if(replay == "backward"){
   myMotor->step(20, BACKWARD, MICROSTEP);
  Serial.println("backward 36 degrees");
  replay = "stop";
  }
}
