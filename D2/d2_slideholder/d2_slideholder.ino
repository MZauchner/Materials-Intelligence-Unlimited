const int stepsPerRevolution = 2048;
char serialData;

#include <Stepper.h>
// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8,10,9,11); //note the modified sequence         

void setup() {
  // set the speed (needed to be reduced for the 28BYJ-48):
  myStepper.setSpeed(4);
  // initialize the serial port:
  Serial.begin(9600);
}


void loop() {
  if(Serial.available()>0){ //id data is available to read
     serialData = Serial.read();
     Serial.print(serialData);
        
        if(serialData == '1'){
            // step one revolution  in one direction:
            Serial.println("clockwise");
            myStepper.step(stepsPerRevolution/10);
            delay(2000);
            }
  
          if(serialData == '2'){
            // step one revolution in the other direction:
            Serial.println("counterclockwise");
            myStepper.step(-stepsPerRevolution/10);
              delay(2000); 
            }
            
          if(serialData == '3'){
            Serial.println("clockwise");
            myStepper.step(stepsPerRevolution/10);
            delay(2000);

            Serial.println("counterclockwise");
            myStepper.step(-stepsPerRevolution/10);
            delay(2000);
        }

  }
}
