"""Motor controller module."""

try:
    from machine import Pin, PWM
except ImportError:  # pragma: no cover - MicroPython only
    Pin = PWM = None


class MotorController:
    """Controls two motors with basic speed settings."""

    def __init__(self, config):
        self.left_pin_num = config.get("left_pin", 0)
        self.right_pin_num = config.get("right_pin", 1)
        self.left_speed = 0.0
        self.right_speed = 0.0
        if PWM:
            self.left_pwm = PWM(Pin(self.left_pin_num))
            self.right_pwm = PWM(Pin(self.right_pin_num))
            self.left_pwm.freq(1000)
            self.right_pwm.freq(1000)
        else:
            self.left_pwm = None
            self.right_pwm = None

    def _apply(self):
        if self.left_pwm:
            duty = int(min(max(self.left_speed, 0.0), 1.0) * 65535)
            self.left_pwm.duty_u16(duty)
        if self.right_pwm:
            duty = int(min(max(self.right_speed, 0.0), 1.0) * 65535)
            self.right_pwm.duty_u16(duty)

    def tick(self, inbox, send_mail):
        if inbox:
            msg = inbox.pop(0)
            if msg.get("type") == "set_speed":
                self.left_speed = float(msg.get("left", 0.0))
                self.right_speed = float(msg.get("right", 0.0))
                self._apply()
            elif msg.get("type") == "report":
                send_mail(
                    "core",
                    {
                        "type": "report_speed",
                        "left": self.left_speed,
                        "right": self.right_speed,
                    },
                )
