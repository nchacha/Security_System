#!/usr/bin/python
import picamera
from time import sleep

#creating an instance 
camera = picamera.PiCamera()

#taking a picture
camera.capture('image.jpg')

#recording video for 3 seconds
camera.start_recording("video.h264")
sleep(6)
camera.stop_recording()
