import serial
import time

class Arduino:
    is_unlocked = False
    objectnum = 0
    serial = None
    
    @staticmethod
    def __init__():
        Arduino.objectnum += 1
        print(Arduino.objectnum)
        
    @staticmethod
    def unlock():
        if not Arduino.is_unlocked:
            try:
                if Arduino.serial is None:
                    Arduino.serial = serial.Serial('COM3') # COMxx   format on Windows
                    Arduino.serial.baudrate = 115200  # set Baud rate 
                    Arduino.serial.bytesize = 8     # Number of data bits = 8
                    Arduino.serial.parity   ='N'    # No parity
                    Arduino.serial.stopbits = serial.STOPBITS_ONE     #
                if not Arduino.serial.is_open: 
                    Arduino.serial.open()
                time.sleep(3)
                Arduino.is_unlocked = True
                Arduino.serial.write(b'A')
                print("Unlocked")
                time.sleep(10)
                Arduino.lock()
                Arduino.serial.close()
            except serial.SerialException as e:
                print(e)
        
    @staticmethod
    def lock():
        print("Locked")
        Arduino.serial.write(b'B')
        Arduino.is_unlocked = False