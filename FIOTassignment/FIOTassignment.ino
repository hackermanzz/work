
#include <SoftwareSerial.h>
#define DEBUG true
SoftwareSerial ESP01(2, 3); // RX, TX
String apiKey = "4X2W404OMDG6LHM2";

void setup() {
  pinMode(13, OUTPUT); // Red TL
  pinMode(12, OUTPUT); // Amber TL
  pinMode(11, OUTPUT); // Green TL
  pinMode(10, OUTPUT); // Red Man
  pinMode(9, OUTPUT); // Green Man
  pinMode(8, OUTPUT); // Buzzer
  pinMode(7, INPUT); // Push Button
  Serial.begin(9600);
  while (!Serial){
    
    }
    Serial.println("Starting");
    ESP01.begin(9600);

}
void sendToCloud(){
  Serial.println("send to cloud start");
  Serial.println();
  sendData("AT+RST\r\n",2000,DEBUG);
  sendData("AT+CWMODE=1\r\n",2000,DEBUG);
  sendData("AT+CWJAP=\"eee-iot\",\"pHAhA946Yogo\"\r\n",4000,DEBUG);  
  sendData("AT+CIPMUX=0\r\n",2000,DEBUG);

  String data = String(1); // convert to string  

  String cmd = "AT+CIPSTART=\"TCP\",\"";
  cmd += "184.106.153.149"; // Thingspeak.com's IP address  
  // ********************** Change this!
  cmd += "\",80\r\n";
  sendData(cmd,2000,DEBUG);

  // Prepare GET string
  String getStr = "GET /update?api_key=";
  getStr += apiKey;
  getStr +="&field1=";
  getStr += data;
  getStr += "\r\n";

  // Send data length & GET string
  ESP01.print("AT+CIPSEND=");
  ESP01.println (getStr.length());
  Serial.print("AT+CIPSEND=");
  Serial.println (getStr.length());  
  delay(500);
  if( ESP01.find( ">" ) )
  {
    Serial.print(">");
    sendData(getStr,2000,DEBUG);
  }
  // Close connection, wait a while before repeating...
  sendData("AT+CIPCLOSE",16000,DEBUG); // thingspeak needs 15 sec delay between updates
  Serial.println("send to cloud end");
  Serial.println(getStr);
}

  

void yellowButton(){
  delay(2000);
  digitalWrite(11, LOW);
  digitalWrite(12,HIGH);
  delay(3000);
  digitalWrite(12, LOW);
}

void whenButtonIsNotPressed(){
  digitalWrite(11, HIGH); // Green TL always on by default, unless button is pressed.
  digitalWrite(10, HIGH); // Red man always on by default, unless button is pressed.
  }
void whenButtonIsPressed(){ 
  digitalWrite(11, LOW); 
  digitalWrite(13, HIGH); 
  delay(1000);
  for(int i = 0; i<20; i++){
     digitalWrite(10, LOW); // Red man turns off for the duration of the pedastrian crossing
     digitalWrite(9, HIGH); // Green man turns on for a split second
     digitalWrite(8, HIGH); // Buzzer buzzes for a split second
     delay(500);
     digitalWrite(9, LOW); // Green man turns off to create a blinking effect
     digitalWrite(8, LOW); // Buzzer stops to create a blinking effect
     delay(500);
      }
      digitalWrite(10, HIGH);
      delay(1500);
      digitalWrite(13, LOW);
  sendToCloud();
  }
void loop() {
  if(digitalRead(7) == LOW) {
    whenButtonIsNotPressed(); // Run this function when the button is not pressed
    }
  if (digitalRead(7) == HIGH){
    yellowButton(); // When the button is pressed there will be a delay before the yellow light turns on and transitions into Red light
    whenButtonIsPressed(); // Run this function when the button is pressed
    }

}
String sendData(String command, const int timeout, boolean debug)
{
    String response = "";
    ESP01.print(command);
    long int time = millis();

    while( (time+timeout) > millis())
    {
      while(ESP01.available())
      {
        // "Construct" response from ESP01 as follows 
         // - this is to be displayed on Serial Monitor. 
        char c = ESP01.read(); // read the next character.
        response+=c;
      }  
    }

    if(debug)
    {
      Serial.print(response);
    }
    
    return (response);
}
