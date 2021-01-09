#!/usr/bin/python3

# This script polls the temperature of the pi and turns on a connected fan when the temperature exceeds a threshold

import RPi.GPIO as GPIO
import os
import time
import datetime

pin = 4
threshold = 70 
filePath = "/home/pi/logs/fanLog.txt"

file = open(filePath, mode="a", buffering=1)
sleepInterval = 60
fanEnabled = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
GPIO.setwarnings(True)

def getTemperature():
    res = os.popen('/opt/vc/bin/vcgencmd measure_temp').readline()
    return float((res.replace("temp=","").replace("'C\n","")))

def toggleFan(status):
    global fanEnabled
    GPIO.output(4, status)
    fanEnabled = status

def log(input):
    date = str(datetime.datetime.utcnow())
    file.write(str(date) + " " + input + "\n")

try:
    toggleFan(False)
    while True:
        log("Checking...")
        temp = getTemperature()
        if temp > threshold:
            if not fanEnabled:
                log("Turning on fan, temperature=" + str(temp))
                toggleFan(True)
            else:
                log("Temperature=" + str(temp))
        elif fanEnabled:
            log("Turning off fan, temperature=" + str(temp))
            toggleFan(False)
        time.sleep(sleepInterval)
except:
    log("Closing")
    GPIO.cleanup()
