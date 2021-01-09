#!/usr/bin/python3

# This script takes a picture using the raspberry pi camera and saves it to a path based on the time

from picamera import PiCamera
from time import sleep
import os
import datetime

outputDirBase = "/home/pi/camera"

def takePicture(output):
    camera.start_preview()
    sleep(5)
    camera.capture(output)
    camera.stop_preview()
    sleep(1)

def buildOutputPath(date):
    path = "{}/{}/{}/{}".format(outputDirBase, date.year, date.month, date.day)
    os.makedirs(path)
    path = "{}/image_{}.jpg".format(path, date.hour)
    return path

date = datetime.datetime.utcnow()
path = buildOutputPath(date)
camera = PiCamera()
takePicture(path)
