#include <Servo.h>
#include <Wire.h>
#include "rgb_lcd.h"

rgb_lcd lcd;

const int colorR = 255;
const int colorG = 0;
const int colorB = 0;

Servo myservo;

int powerPin = 7;
int servoPin = 9;
String authorized = "";
 
void setup() 
{ 
  //set up the LCD's number of comlumns and rows
  lcd.begin(16, 2);

  lcd.setRGB(0, 0, 255);
  
  lcd.print("hello world");
	
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
              lcd.setRGB(0, 255, 0);
    } else if (authorized == "off") {
      digitalWrite(powerPin, HIGH);
	    Serial.println("Not authorized\n");
              lcd.setRGB(255, 0, 0);
    }  
  }
  myservo.write(0);
  delay(15);
}
