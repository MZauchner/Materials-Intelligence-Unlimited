/* 
This is the Arduino command code for D1 stepper motor which pushes the rod from the silos into the test holder, wait for the 
test to finish, then push the rod into the conveyor belt. 

The code contains adds-on Adafruit Motorshield code.

Once the code is uploaded, open the Serial Monitor. Input "1" to push the rod from the silos into the test holder, and "2" to 
push the rod from the test holder on to the conveyor belt. 
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

int Dword;
void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Stepper test!");

  AFMS.begin();  // create with the default frequency 1.6KHz
  //AFMS.begin(1000);  // OR with a different frequency, say 1KHz
  
  myMotor->setSpeed(300);  // 10 rpm   
}

void loop() {
  Dword=Serial.read();
   if (Dword =='1')
  {
  Serial.println("Command 1 on");
  myMotor->step(744, FORWARD, DOUBLE); 
   myMotor->step(50, BACKWARD, DOUBLE); 
   delay(Serial.available());
}
 if (Dword =='2')
  {
  Serial.println("Command 2 on");
  myMotor->step(450, FORWARD, DOUBLE); 
  myMotor->step(1144, BACKWARD, DOUBLE);
   delay(Serial.available());
}
}
