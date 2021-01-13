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
    path = "{}/{}/{:0>2d}/{:0>2d}".format(outputDirBase, date.year, date.month, date.day)
    if not os.path.exists(path):
        os.makedirs(path)
    path = "{}/image_{}_{:0>2d}_{:0>2d}_{:0>2d}.jpg".format(path, date.year, date.month, date.day, date.hour)
    return path

date = datetime.datetime.utcnow()
path = buildOutputPath(date)
camera = PiCamera()
camera.resolution = (1024, 768)
takePicture(path)
