
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"

Adafruit_MotorShield AFMS = Adafruit_MotorShield();

Adafruit_DCMotor *myMotor = AFMS.getMotor(4);
 
void setup() {
  AFMS.begin();
  Serial.begin(9600);           
  Serial.println("Motor test!");
  
  myMotor->setSpeed(120);     
}
 
void loop() 
{
  if(Serial.available()){
  int input=Serial.parseInt();
  Serial.println(input) ;
  if (input == 1 ){      //accept
    myMotor->run(RELEASE);      
  delay(1000);
    myMotor->run(BACKWARD);      
  delay(5500);
    myMotor->run(RELEASE);    
  delay(1000);
  }
  
  if (input == 2 ){      //reject
    myMotor->run(RELEASE);      
  delay(1000);
    myMotor->run(BACKWARD);      
  delay(2000);
   myMotor->run(RELEASE);      
  delay(1000);
    myMotor->run(FORWARD);   
  delay(500);
    myMotor->run(RELEASE);    
  delay(1000);
  }
}
}
