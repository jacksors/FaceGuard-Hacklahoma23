import cv2
import twiliostuff as ts
import serial
import time
from arduino import Arduino

def detected(identity: str, face: cv2.Mat):
    cv2.imwrite("test.png", face)
    #send text with name and image 
    #communicate with lock to unlock door
    try:
        Arduino.unlock()
        ts.sendText(identity, ts.uploadimg("test.png", "face"), "")
    except serial.SerialException as e:
        print(e)
