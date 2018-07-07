#include <Servo.h> 
 
Servo myservo;

int ledPin = 6;
int motionPin = 4;
int motionVal = 0;
int pirState = LOW;
int powerPin = 7;
int servoPin = 9;
String authorized = "";
 
void setup() 
{ 
  Serial.begin(9600);
  pinMode(powerPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(motionPin, INPUT);
  myservo.attach(servoPin);
} 
 
 
void loop() 
{
  motionVal = digitalRead(motionPin);
  if(Serial.available())
  {
  
  	if(motionVal == HIGH)
  	{
		digitalWrite(ledPin, HIGH);
		if(pirState == LOW)
		{
			Serial.println("Motion detected\n");
			pirState = HIGH;
		}
  	}
  	else
  	{
		digitalWrite(ledPin, LOW);
		if(pirState == HIGH)
		{
			Serial.println("Motion stopped\n");
			pirState = LOW;
		}
  	}	
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
