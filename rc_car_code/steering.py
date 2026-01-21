from machine import Pin, PWM
import time

class steeringWheel:
    def __init__(self, IN1=0, IN2=1, ENA=2, PWM_freq=1000, PWM_value=50000):
        self.IN1 = Pin(IN1, Pin.OUT)
        self.IN2 = Pin(IN2, Pin.OUT)
        self.ENA = PWM(Pin(ENA))
        self.ENA.freq(PWM_freq)
        self.PWM_value = PWM_value
        self.direction = "Middle"

    def steerLeft(self):
        self.IN1.value(0)
        self.IN2.value(1)
        self.ENA.duty_u16(self.PWM_value)
        self.direction = "Left"

    def steerRight(self):
        self.IN1.value(1)
        self.IN2.value(0)
        self.ENA.duty_u16(self.PWM_value)
        self.direction = "Right"

    def steerMiddle(self):
        if self.direction == "Right":
            self.IN1.value(0)
            self.IN2.value(1)
            self.ENA.duty_u16(40000)
            time.sleep(0.25)
            
        elif self.direction == "Left":
            self.IN1.value(1)
            self.IN2.value(0)
            self.ENA.duty_u16(40000)
            time.sleep(0.25)
            
        self.IN1.value(0)
        self.IN2.value(0)
        self.ENA.duty_u16(0)
        self.direction = "Middle"

