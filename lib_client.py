#!/usr/bin/env python3
#-*-coding:utf-8-*-
import time

def unlock():
    pass

def unbook(chamber,con):
    con.send(f"UNBOOK {chamber}".encode())


class Rasp:
    def __init__(self,gpio,button_pin = 13,led_pin=37):
        self.GPIO = gpio
        self.button = 13
        self.led1 = 35
        self.led2 = 37
        self.GPIO.setup(self.button, self.GPIO.IN)
        self.GPIO.setup(self.led, self.GPIO.OUT)
        self.startBlink()
        
    def state(self):
        return self.GPIO.input(self.button)
    
    def light1_on(self):
        self.GPIO.output(self.led1, self.GPIO.HIGH)
    def light1_off(self):
        self.GPIO.output(self.led1, self.GPIO.LOW)
    def light2_on(self):
        self.GPIO.output(self.led2, self.GPIO.HIGH)
    def light2_off(self):
        self.GPIO.output(self.led2, self.GPIO.LOW)
        
    def startBlink(self):
        for i in range(3):
            self.light()
            time.sleep(0.1)
