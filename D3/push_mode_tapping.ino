#include <Servo.h>

Servo head_rotate;

//Pin assignments
int solenoid_switch = 3; //solenoid control signal pin
int servo_pin = 9; //servo control signal pin

//operating variables
int impact_time;
int head_pos;
int delay_time;
int strike_repeats;
int strike_power;
int centre_val = 82; //this is the central position - has to be calibrated on each assembly

void setup() {
pinMode(solenoid_switch, OUTPUT);
Serial.begin(115200);
head_rotate.attach(servo_pin); 
head_rotate.write(centre_val); 
}

void loop() {
if (Serial.available()){
  String input = Serial.readString();
  Serial.println(input);
  sscanf(input.c_str(), "%d %d %d %d", &impact_time, &head_pos, &delay_time, &strike_power);
  head_rotate.write(head_pos);
  delay(delay_time);
  analogWrite(solenoid_switch, strike_power);
  delay(impact_time);
  digitalWrite(solenoid_switch, LOW);
  delay(delay_time);
  head_rotate.write(centre_val);
}
}

