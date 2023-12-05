// This program translates a value that is read from a potentiometer into a PWM value
// to drive a motor using the Pololu Simple Motor Controller.
#include <Servo.h> 

Servo motor;

// constants won't change.
#define PIN_POTENTIOMETER 2
#define PIN_PWM 9

void setup() {
  motor.attach(PIN_PWM);
}

void loop() {
  int potValue = analogRead(PIN_POTENTIOMETER);
  int speed = map(potValue, 0, 1023, 0, 180);
 
 
   if( speed==90) motor.write(LOW);
   
  delay(30);
  motor.write(speed);
  
  delay(300);
}
