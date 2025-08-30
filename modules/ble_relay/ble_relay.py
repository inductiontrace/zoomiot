"""BLE relay module."""


class BLERelay:
    """Forwards messages over BLE (placeholder implementation)."""

    def __init__(self, config):
        self.device_name = config.get("device_name", "rc-car")

    def tick(self, inbox, send_mail):
        if inbox:
            msg = inbox.pop(0)
            if msg.get("type") == "send":
                _payload = msg.get("payload", "")
                # Placeholder: would send over BLE
            elif msg.get("type") == "ble_in":
                send_mail("core", {"type": "ble_command", "payload": msg.get("payload", "")})
