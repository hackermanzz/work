import RPi.GPIO as GPIO
import dht11
import time
import datetime
import requests
from time import sleep
#GUI(Graphics User Interface)
from tkinter import * # import everything
import time

top=Tk() # Create
LightBulb_On = PhotoImage(file="LED_off.gif")
LightBulb_Off = PhotoImage(file="LED_on.gif")


def toggle_LED(State):
    
    if State == 0:
        State = State + 1 # At this moment State == 1
        C.itemconfig(Light_IMG, image =LightBulb_On)
        time.sleep(2)
    else:
        State = State - 1
        C.itemconfig(Light_IMG, image =LightBulb_Off)
        time.sleep(2)
    print("The state of the light bulb is" , State)
    top.after(1000,toggle_LED)





instance = dht11.DHT11(pin=21) #read data using pin 21
GPIO.setwarnings(False)
class enviroment:
    def TemperatureAndHumi(self):
        try:
            while True: #keep reading, unless keyboard is pressed
                result = instance.read() # using the sensor
                if result.is_valid(): #print datetime & sensor values
                    timing = datetime.datetime.now()
                    timing = timing.strftime("%d-%m-%Y_%H:%M:%S")
                    print("Last valid input: " + timing)
                    print("Temperature: %-3.1f C" % result.temperature)
                    print("Humidity: %-3.1f %%" % result.humidity)
                    Temperature = result.temperature
                    Humidity = result.humidity
                sleep(0.5) #short delay between reads
                return Temperature , Humidity
                # uploading sensors data
                
        except KeyboardInterrupt:
            print("Cleanup")
            GPIO.cleanup()
            return Temperature,Humidity





def Use_sensors():
    result = []
    env = enviroment()
    
    #while True:
    temp, humid = env.TemperatureAndHumi()

    result.append(temp)
    result.append(humid)
    return result

def getMositure():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4,GPIO.IN)
    if GPIO.input(4):
        toggle_LED(0)
        return 1
    else:
        toggle_LED(1)
        return 0

def waterThePlant():
    # Code is based on the pump
    GPIO.setup(7,GPIO.OUT)
    GPIO.output(7 , )
    time.sleep(1)
    GPIO.output(7 , GPIO.HIGH)



# Flow of the program


def sendToCloud(resultList):
    print("Uploading sample...")
    temperature = resultList[0]
    Humidity = resultList[1]
    resp=requests.get("https://api.thingspeak.com/update?api_key=###########################&field1=%s&field2=%s" %(temperature,Humidity))





while True: # infinite loop
    resultList = Use_sensors() # [temp , humid]
    if getMositure() == 0:
        waterThePlant() # lightbulb
    else:
        print(datetime.datetime.now())
    sendToCloud(resultList)

    C= Canvas(top , width= 200, height=128)
    Light_IMG= C.create_image(0,0,image=LightBulb_Off,anchor=NW)
    C.pack() # at this point in time , the canvas only has an off lightbulb
    top.after(0, toggle_LED)
    top.mainloop()


main()
