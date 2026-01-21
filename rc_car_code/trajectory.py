from machine import Pin, PWM

class Trajectory:
    def __init__(self, IN3=3, IN4=4, ENB=5, PWM_freq=1000):
        self.IN3 = Pin(IN3, Pin.OUT)
        self.IN4 = Pin(IN4, Pin.OUT)
        self.ENB = PWM(Pin(ENB))
        self.ENB.freq(PWM_freq)

        self.min_pwm = 35000
        self.max_pwm = 65535
        self.default_pwm = 45000

        self.speed_percent = int(
            (self.default_pwm - self.min_pwm) * 100 /
            (self.max_pwm - self.min_pwm)
        )

        self.current_pwm = self.default_pwm
        self.direction = "stop"

        self.ENB.duty_u16(self.current_pwm)

    def _apply_pwm(self):
        if self.direction == "stop":
            self.ENB.duty_u16(0)
        else:
            self.ENB.duty_u16(self.current_pwm)

    def set_speed(self, percent):
        percent = max(0, min(100, percent))
        self.speed_percent = percent

        if percent == 0:
            self.current_pwm = 0
        else:
            self.current_pwm = int(
                self.min_pwm +
                (percent / 100) * (self.max_pwm - self.min_pwm)
            )

        self._apply_pwm()

    def forward(self):
        self.direction = "forward"
        self.IN3.value(1)
        self.IN4.value(0)
        self._apply_pwm()

    def backward(self):
        self.direction = "backward"
        self.IN3.value(0)
        self.IN4.value(1)
        self._apply_pwm()

    def stop(self):
        self.direction = "stop"
        self.IN3.value(0)
        self.IN4.value(0)
        self.ENB.duty_u16(0)

