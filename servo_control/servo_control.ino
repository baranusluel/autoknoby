// Sweep
// by BARRAGAN <http://barraganstudio.com> 
// This example code is in the public domain.


#include <Servo.h> 
 
Servo myservo;  // create servo object to control a servo 
                // a maximum of eight servo objects can be created 

int powerPin = 7;
int servoPin = 9;
String authorized = "";
 
void setup() 
{ 
  Serial.begin(9600);
  pinMode(powerPin, OUTPUT);
  myservo.attach(servoPin);
} 
 
 
void loop() 
{
  if (Serial.available()) {
    authorized = Serial.readString();
    if (authorized == "on") {
      digitalWrite(powerPin, LOW);
      Serial.println("Authorized");
    } else if (authorized == "off") {
      digitalWrite(powerPin, HIGH);
      Serial.println("Not authorized");
    }
  }
  myservo.write(0);
  delay(100);
} 
