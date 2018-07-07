#include <Servo.h> 
 
Servo myservo;

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
  if(Serial.available())
  {
    authorized = Serial.readString();
	  if (authorized == "on") {
      digitalWrite(powerPin, LOW);
	    Serial.println("Authorized\n");
    } else if (authorized == "off") {
      digitalWrite(powerPin, HIGH);
	    Serial.println("Not authorized\n");
    }  
  }
  myservo.write(0);
  delay(15);
}
