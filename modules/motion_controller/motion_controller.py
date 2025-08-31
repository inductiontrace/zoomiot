"""Motion controller module."""


def _direction_to_speeds(direction, speed):
    if direction == "forward":
        return speed, speed
    if direction == "backward":
        return -speed, -speed
    if direction == "left":
        return -speed, speed
    if direction == "right":
        return speed, -speed
    return 0.0, 0.0


class MotionController:
    """Translates movement requests into motor commands."""

    def __init__(self, config):
        self.default_speed = float(config.get("default_speed", 0.5))

    def tick(self, inbox, send_mail):
        if inbox:
            msg = inbox.pop(0)
            if msg.get("type") == "drive":
                speed = float(msg.get("speed", self.default_speed))
                direction = msg.get("direction", "forward")
                left, right = _direction_to_speeds(direction, speed)
                send_mail(
                    "motor_controller",
                    {"type": "set_speed", "left": left, "right": right},
                )
