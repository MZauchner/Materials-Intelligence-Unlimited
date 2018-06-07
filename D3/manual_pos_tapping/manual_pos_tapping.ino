#include <Servo.h>

Servo head_rotate;

//Pin assignments
int solenoid_switch = 13; //solenoid control signal pin
int servo_pin = 2; //servo control signal pin

//operating variables
int impact_time;
int head_pos;
int repeats;

void setup() {
  pinMode(solenoid_switch, OUTPUT);
  Serial.begin(115200);
  head_rotate.attach(servo_pin);
}

void loop() {
  if (Serial.available()){
    String input = Serial.readString();
    Serial.println(input);
    sscanf(input.c_str(), "%d %d %d", &impact_time, &head_pos, &repeats);
    if (head_pos != -1){
     head_rotate.write(head_pos); 
    }
    delay(500);
    for (int i = 0; i < repeats; i++){
      digitalWrite(solenoid_switch, HIGH);
      delay(impact_time);
      digitalWrite(solenoid_switch, LOW); 
      delay(50); //hard-coded value to allow for sample ring-down between strikes
    }
  }
}
