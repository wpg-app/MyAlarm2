from gpiozero import LED, Buzzer, Button
from time import sleep
from signal import pause
import datetime
import sys


btn=Button(6)
buzz=Buzzer(17)

def setStop():
    global stopped
    print stopped
    stopped=True

def _2beep():

    global stopped

    btn.when_pressed=setStop

    for count in range(0,6):
        if(stopped!=True):
            print("button pressed")
            buzz.on()
            sleep(0.2)
            buzz.off()
            sleep(0.2)    
            buzz.on()
            sleep(0.2)
            buzz.off()

            sleep(1)

def _6beep():
    for count in range(0,6):
        print "buzz"
        #buzz.toggle()
        buzz.on()
        sleep(0.2)
        buzz.off()

        sleep(0.5)



stopped=False;

'''
NOT WORKING
hour= unicode(datetime.datetime.now().time())
hour= hour[:-7]
#print hour
#sleep(1)
startBuzz="03:25:"
if(hour==startBuzz+"00"):
    while(1!=2):
        print hour+">>"+startBuzz+"09"
        hour= unicode(datetime.datetime.now().time())
        hour= hour[:-7]
        #aaa()
        print("button pressed")
'''

'''
ANOTHER ONE WAY OF GETTING TIME
date= unicode(datetime.datetime.now())
date= date[:-7]
'''

_now= datetime.datetime.now()
_alarmTime= datetime.datetime(2016,06,12,7,50,0)
#print (_alarmTime)
#sys.exit(">>")
_stopTime= _alarmTime+datetime.timedelta(0,0,0,0,10)

#print _now.strftime("%H:%M:%S")
#print _alarmTime.strftime("%H:%M:%S")
if(_now.strftime("%H:%M:%S")>_alarmTime.strftime("%H:%M:%S") and _now.strftime("%H:%M:%S")<_stopTime.strftime("%H:%M:%S")):
    _2beep()

#sleep(1)
